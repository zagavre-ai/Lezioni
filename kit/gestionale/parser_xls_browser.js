function parseXLS(u){ // u: Uint8Array -> array of rows (array of strings)
 const dv=new DataView(u.buffer,u.byteOffset,u.byteLength);
 const ss=1<<dv.getUint16(30,true),mss=1<<dv.getUint16(32,true);
 const nfat=dv.getUint32(44,true),dirStart=dv.getInt32(48,true),cut=dv.getUint32(56,true),mStart=dv.getInt32(60,true),nm=dv.getUint32(64,true),difStart=dv.getInt32(68,true),ndif=dv.getUint32(72,true);
 const sec=i=>512+i*ss;
 let difat=[];for(let i=0;i<109;i++)difat.push(dv.getInt32(76+i*4,true));
 let d=difStart;for(let k=0;k<ndif&&d>=0;k++){for(let i=0;i<ss/4-1;i++)difat.push(dv.getInt32(sec(d)+i*4,true));d=dv.getInt32(sec(d)+ss-4,true)}
 const fat=[];difat.slice(0,nfat).forEach(s=>{for(let i=0;i<ss/4;i++)fat.push(dv.getInt32(sec(s)+i*4,true))});
 const chain=s=>{const c=[];while(s>=0&&c.length<1e6){c.push(s);s=fat[s]}return c};
 const read=(s,len)=>{const c=chain(s),o=new Uint8Array(c.length*ss);c.forEach((x,i)=>o.set(u.subarray(sec(x),sec(x)+ss),i*ss));return len!=null?o.subarray(0,len):o};
 const dir=read(dirStart);const dd=new DataView(dir.buffer);const ents=[];
 for(let o=0;o<dir.length;o+=128){const nl=dd.getUint16(o+64,true);let n='';for(let i=0;i<nl/2-1;i++)n+=String.fromCharCode(dd.getUint16(o+i*2,true));ents.push({n,t:dir[o+66],s:dd.getInt32(o+116,true),z:dd.getUint32(o+120,true)})}
 const root=ents[0];const wb=ents.find(e=>/^(Workbook|Book)$/i.test(e.n));
 let W;if(wb.z<cut){const ms=read(root.s);const mfat=read(mStart);const mf=new DataView(mfat.buffer);const mfa=i=>mf.getInt32(i*4,true);let s=wb.s;const parts=[];while(s>=0){parts.push(ms.subarray(s*mss,s*mss+mss));s=mfa(s)}W=new Uint8Array(parts.length*mss);parts.forEach((p,i)=>W.set(p,i*mss));W=W.subarray(0,wb.z)}else W=read(wb.s,wb.z);
 const wv=new DataView(W.buffer,W.byteOffset,W.byteLength);
 // records
 const recs=[];for(let o=0;o+4<=W.length;){const t=wv.getUint16(o,true),l=wv.getUint16(o+2,true);recs.push({t,o:o+4,l});o+=4+l}
 const sst=[];const cells={};
 const rk=v=>{let x;if(v&2){x=v>>2}else{const b=new DataView(new ArrayBuffer(8));b.setInt32(4,v&0xfffffffc,true);x=b.getFloat64(0,true)}return v&1?x/100:x};
 for(let i=0;i<recs.length;i++){const r=recs[i];
  if(r.t===0xFC){ // SST with CONTINUE
   const segs=[[r.o,r.o+r.l]];let j=i+1;while(j<recs.length&&recs[j].t===0x3C){segs.push([recs[j].o,recs[j].o+recs[j].l]);j++}
   let si=0,p=segs[0][0]+8;const n=wv.getUint32(segs[0][0]+4,true);
   const need=()=>{if(p>=segs[si][1]){si++;p=segs[si][0];return true}return false};
   for(let k=0;k<n;k++){need();let cch=wv.getUint16(p,true);p+=2;let fl=W[p++];let rt=0,ext=0;if(fl&8){rt=wv.getUint16(p,true);p+=2}if(fl&4){ext=wv.getInt32(p,true);p+=4}
    let s='';let wide=fl&1;while(cch>0){if(p>=segs[si][1]){si++;p=segs[si][0];wide=W[p++]&1}
     const avail=wide?Math.floor((segs[si][1]-p)/2):segs[si][1]-p;const take=Math.min(avail,cch);
     for(let q=0;q<take;q++){s+=String.fromCharCode(wide?wv.getUint16(p,true):W[p]);p+=wide?2:1}cch-=take}
    let skip=rt*4+ext;while(skip>0){if(p>=segs[si][1]){si++;p=segs[si][0]}const a=Math.min(skip,segs[si][1]-p);p+=a;skip-=a}
    sst.push(s)}
  }
  const set=(row,col,v)=>{(cells[row]=cells[row]||{})[col]=v};
  if(r.t===0xFD)set(wv.getUint16(r.o,true),wv.getUint16(r.o+2,true),sst[wv.getUint32(r.o+6,true)]);
  if(r.t===0x203)set(wv.getUint16(r.o,true),wv.getUint16(r.o+2,true),wv.getFloat64(r.o+6,true));
  if(r.t===0x27E)set(wv.getUint16(r.o,true),wv.getUint16(r.o+2,true),rk(wv.getInt32(r.o+6,true)));
  if(r.t===0xBD){const row=wv.getUint16(r.o,true),c0=wv.getUint16(r.o+2,true);const n=(r.l-6)/6;for(let k=0;k<n;k++)set(row,c0+k,rk(wv.getInt32(r.o+4+k*6+2,true)))}
  if(r.t===0x204){const row=wv.getUint16(r.o,true),col=wv.getUint16(r.o+2,true),cch=wv.getUint16(r.o+6,true),f=W[r.o+8];let s='';for(let q=0;q<cch;q++)s+=String.fromCharCode(f&1?wv.getUint16(r.o+9+q*2,true):W[r.o+9+q]);set(row,col,s)}
  if(r.t===0x0A&&Object.keys(cells).length)break; // EOF del primo foglio dopo i dati
 }
 return Object.keys(cells).map(Number).sort((a,b)=>a-b).map(k=>{const c=cells[k];const m=Math.max(...Object.keys(c).map(Number));return Array.from({length:m+1},(_,i)=>c[i]==null?'':String(c[i]))});
}

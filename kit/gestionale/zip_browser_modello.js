const fs=require('fs');const T=new Uint32Array(256);for(let n=0;n<256;n++){let c=n;for(let k=0;k<8;k++)c=c&1?0xEDB88320^(c>>>1):c>>>1;T[n]=c>>>0}
const crc=u=>{let c=0xFFFFFFFF;for(let i=0;i<u.length;i++)c=T[(c^u[i])&255]^(c>>>8);return (c^0xFFFFFFFF)>>>0};
const files=['../xls/a.xls','../xls/r.xls'].map((p,i)=>({n:new TextEncoder().encode('Report_attivita_ALUNNO_'+i+'.xls'),u:new Uint8Array(fs.readFileSync(p))}));
const parts=[],cent=[];let off=0;const le=(v,b)=>{const a=new Uint8Array(b);for(let i=0;i<b;i++)a[i]=(v>>>(8*i))&255;return a};
for(const f of files){const c=crc(f.u);parts.push(le(0x04034b50,4),le(20,2),le(0x0800,2),le(0,2),le(0,2),le(0x5B6A,2),le(c,4),le(f.u.length,4),le(f.u.length,4),le(f.n.length,2),le(0,2),f.n,f.u);
cent.push(le(0x02014b50,4),le(20,2),le(20,2),le(0x0800,2),le(0,2),le(0,2),le(0x5B6A,2),le(c,4),le(f.u.length,4),le(f.u.length,4),le(f.n.length,2),le(0,2),le(0,2),le(0,2),le(0,2),le(0,4),le(off,4),f.n);off+=30+f.n.length+f.u.length}
const cs=cent.reduce((s,a)=>s+a.length,0);const end=[le(0x06054b50,4),le(0,2),le(0,2),le(files.length,2),le(files.length,2),le(cs,4),le(off,4),le(0,2)];
fs.writeFileSync('t.zip',Buffer.concat([...parts,...cent,...end].map(x=>Buffer.from(x))));

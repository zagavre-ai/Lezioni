# Disposizione automatica delle mappe (ricottura simulata): niente sovrapposizioni, frecce corte che non attraversano altri riquadri
import random, math, sys, json
sys.path.insert(0,'/tmp/claude-0/w/build')
from maps import *

def inter(a,b,pad=0):
    return max(0,min(a[2]+pad,b[2])-max(a[0]-pad,b[0]))*max(0,min(a[3]+pad,b[3])-max(a[1]-pad,b[1]))
def seg_hits_box(p,q,b):
    # Liang-Barsky
    x0,y0=p;x1,y1=q;dx,dy=x1-x0,y1-y0;t0,t1=0,1
    for pp,qq in ((-dx,x0-b[0]),(dx,b[2]-x0),(-dy,y0-b[1]),(dy,b[3]-y0)):
        if pp==0:
            if qq<0:return False
        else:
            r=qq/pp
            if pp<0:
                if r>t1:return False
                t0=max(t0,r)
            else:
                if r<t0:return False
                t1=min(t1,r)
    return t0<t1
def cross(p1,p2,p3,p4):
    def o(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    return o(p1,p2,p3)*o(p1,p2,p4)<0 and o(p3,p4,p1)*o(p3,p4,p2)<0

def energy(M,state,bounds=(30,150,1890,1030),dims=None):
    nodes=M.nodes;ids=list(nodes)
    dims=dims or {i:(nodes[i].w,nodes[i].h) for i in ids}
    boxes={i:(state[i][0]-dims[i][0]/2,state[i][1]-dims[i][1]/2,state[i][0]+dims[i][0]/2,state[i][1]+dims[i][1]/2) for i in ids}
    e=0
    for k,i in enumerate(ids):
        b=boxes[i]
        e+=max(0,bounds[0]-b[0])*40+max(0,b[2]-bounds[2])*40+max(0,bounds[1]-b[1])*40+max(0,b[3]-bounds[3])*40
        for j in ids[k+1:]:
            e+=inter(b,boxes[j],14)/6
    segs=[]
    for a,b,_ in M.edges:
        pa=state[a];pb=state[b];L=math.hypot(pa[0]-pb[0],pa[1]-pb[1]);e+=L*0.12
        for i in ids:
            if i!=a and i!=b and seg_hits_box(pa,pb,boxes[i]):e+=1500
        # il figlio sotto o di lato al genitore
        if pb[1]<pa[1]-60:e+=60
        segs.append((pa,pb,a,b))
    for x in range(len(segs)):
        for y in range(x+1,len(segs)):
            s,t=segs[x],segs[y]
            if len({s[2],s[3],t[2],t[3]})==4 and cross(s[0],s[1],t[0],t[1]):e+=700
    return e

WOPT=[260,320,380,440,520,620,740,900]
def solve(M,seed=1,iters=60000,init=None,fixed=()):
    random.seed(seed);ids=list(M.nodes)
    alt={}
    for i,n in M.nodes.items():
        if n.kind=='lab':alt[i]=[(n.w,n.h)];continue
        alt[i]=[]
        imm=Image.new('RGBA',(10,10));dd=ImageDraw.Draw(imm);lw=max(dd.textlength(w,font=F('bold' if n.bold else 'med',n.size)) for w in n.text.split())
        for wc in WOPT:
            if wc-36<lw+8 and wc!=WOPT[-1]:continue
            m=Node(i,n.text,n.kind,0,0,wc,n.size,n.shape,n.bold);alt[i].append((m.w,m.h,wc))
    ch={i:min(range(len(alt[i])),key=lambda k:abs(alt[i][k][0]-M.nodes[i].w)) if M.nodes[i].kind!='lab' else 0 for i in ids}
    dims=lambda:{i:alt[i][ch[i]][:2] for i in ids}
    st={i:(init[i] if init else (random.uniform(100,1800),random.uniform(200,1000))) for i in ids}
    cur=energy(M,st,dims=dims());T=300.0;best=(cur,dict(st),dict(ch))
    for it in range(iters):
        T=300*(1-it/iters)**2+1
        i=random.choice(ids)
        if i in fixed:continue
        old=st[i];oc=ch[i];sc=300 if it<iters*0.5 else 80
        if random.random()<0.25 and M.nodes[i].kind!='lab':ch[i]=random.randrange(len(alt[i]))
        else:st[i]=(old[0]+random.gauss(0,sc),old[1]+random.gauss(0,sc))
        e=energy(M,st,dims=dims())
        if e<cur or random.random()<math.exp((cur-e)/T):
            cur=e
            if e<best[0]:best=(e,dict(st),dict(ch))
        else:st[i]=old;ch[i]=oc
    e,st,ch=best
    for i,n in M.nodes.items():
        if n.kind!='lab':
            m=Node(i,n.text,n.kind,st[i][0],st[i][1],alt[i][ch[i]][2],n.size,n.shape,n.bold);M.nodes[i]=m
        else:n.cx,n.cy=st[i]
        M.nodes[i].cx,M.nodes[i].cy=st[i]
    return e

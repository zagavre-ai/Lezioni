import re,sys
for p in sys.argv[1:]:
    B=open(p).read().split('\n\n');n=0
    for i in range(len(B)-1):
        a=B[i].split('\n');b=B[i+1].split('\n')
        if len(a)<2 or len(b)<2:continue
        m=re.search(r"\s(\w+)$",a[-1])
        if m and b[1].startswith("'"):
            a[-1]=a[-1][:m.start()];b[1]=m.group(1)+b[1];B[i]='\n'.join(a);B[i+1]='\n'.join(b);n+=1
    open(p,'w').write('\n\n'.join(B));print(p,n)

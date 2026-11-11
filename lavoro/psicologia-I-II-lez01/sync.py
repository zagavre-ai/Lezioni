import json,sys
sys.argv=['x']
import align as AL
cov=json.load(open('/home/claude/lezioni/psicologia-I-II-lez01/coverage.json')); U=AL.U
sp=[i for i,c in enumerate(cov) if c>=0.2]
# frasi brevissime tra due frasi dette: restano
S=set(sp)
for i in range(1,len(U)-1):
    if i not in S and len(U[i]['txt'])<70 and (i-1) in S and (i+1) in S: S.add(i)
idx=sorted(S)
A=AL.run(idx)
json.dump({'spoken':idx,'align':A},open('/home/claude/lezioni/psicologia-I-II-lez01/sync.json','w'))
print(len(U),'frasi;',len(idx),'dette;',len(U)-len(idx),'saltate')

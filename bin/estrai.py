import sys,json
from pptx import Presentation
p=Presentation(sys.argv[1]);S=[]
for i,s in enumerate(p.slides,1):
    tx=[]
    for sh in s.shapes:
        if sh.has_text_frame:
            for para in sh.text_frame.paragraphs:
                t=''.join(r.text for r in para.runs).strip()
                b=''.join(r.text for r in para.runs if r.font.bold).strip()
                if t:tx.append([t,b])
    imgs=[f's{i:02d}_{j}' for j,sh in enumerate(s.shapes) if sh.shape_type==13]
    S.append({'n':i,'tx':tx,'img':imgs})
json.dump(S,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)

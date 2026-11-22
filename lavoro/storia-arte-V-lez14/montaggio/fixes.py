import re
REP=[(r"\b8 ?[Dd]ix\b","Otto Dix"),(r"\bDicks\b","Dix"),(r"Georg Gross","George Grosz"),(r"\bGross\b","Grosz"),(r"Backman","Beckmann"),(r"\bGh?ernica\b","Guernica"),
 (r"\bKalo\b","Kahlo"),(r"Courbe\b","Courbet"),(r"Candinsky","Kandinsky"),(r"\bFOV\b","fauves"),(r"\bSchiller\b","Sheeler"),(r"Grand Hood|Grand Code","Grant Wood"),(r"\b[HC]ooper\b","Hopper"),
 (r"Walt Evans","Walker Evans"),(r"Dolo Ange","Dorothea Lange"),(r"Foreign Security Administration","Farm Security Administration"),(r"Albert Spur","Albert Speer"),(r"Dora Ma\b","Dora Maar"),
 (r"Nippomo","Nipomo"),(r"Cher Cropper's Family","Sharecropper's Family"),(r"itleriano","hitleriano"),(r"Street\.? Photography","Straight Photography"),(r"\b27, 28, ","1927-1928, "),
 (r"Ivan fotografa","Evans fotografa"),(r"Charles Shiller","Charles Sheeler"),(r"Shiller","Sheeler"),(r"\b(Uh|Um|uh|um)\b,?\s*",""),(r"nuova oggettività","Nuova Oggettività"),(r"Gross e 8 Dix","Grosz e Otto Dix"),
 (r"American Landscape 1930","American Landscape, 1930"),(r"Nighthawks","Nighthawks")]
DROP=re.compile(r"^\s*(See|Pill|Yeah, piano|Soffre|Del|D|Eccolo qua)\.?\s*$",re.I)
def fix(t):
    for a,b in REP:t=re.sub(a,b,t)
    return re.sub(r'\s+',' ',t).strip()

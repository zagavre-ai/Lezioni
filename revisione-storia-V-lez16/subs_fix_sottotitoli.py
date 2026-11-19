# Correzioni ai sottotitoli · Storia V lez. 16: SOLO regole automatiche (nomi, date, disturbi). Non riletti riga per riga.
import re
DROP_RE = re.compile(r"^(um|uh|yeah|ehm|mm|ah|on the|non|ora|la|dire|e poi\.\.\.|\.\.\.|e beh|sì|okay)[\.\s]*$", re.I)
DROP_IDX = set()
GLOBAL = [
 (r"\bKhrushchev\b|\bKhrushche\b|\bKhrusch\b|\bKhrush\b|\bKrusciov\b|\bKruscev\b|\bChruščev\b|\bKhrushev\b", "Chruščëv"),
 (r"\bBriesnev\b|\bBrezniev\b|\bBresnev\b|\bBreznev\b|\bBrežnev\b", "Brežnev"),
 (r"\bLindon Johnson\b|\bLind Johnson\b|\bLindle Johnson\b|\bLindson\b|\bLyndon\b", "Lyndon Johnson"), (r"Lyndon Johnson Johnson", "Lyndon Johnson"),
 (r"\bbuom\b", "boom"), (r"\bCivil Rights Heads\b|\bCivil Right Act\b", "Civil Rights Act"), (r"\bvoting right heads\b|\bVoting right heads\b|\bvoting rights\b", "Voting Rights Act"),
 (r"\bcagnolina laica\b", "cagnolina Laika"), (r"\bYuri Gagarin\b", "Jurij Gagarin"), (r"\bMalcolm Mixan\b|\bMalco Mixan\b|\bMalcom X\b", "Malcolm X"),
 (r"\bMatt Luther King\b|\bMartin Luther King\b", "Martin Luther King"), (r"\bKu Klux Clan\b|\bCurcus Klan\b", "Ku Klux Klan"),
 (r"\bmillenovecentosessantatré\b", "1963"), (r"\bsessantatré\b", "'63"),
]
OVR = {}
DUBBI = []

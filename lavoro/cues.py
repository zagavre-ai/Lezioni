# -*- coding: utf-8 -*-
CUES = {
 1: [["deficit", "disavanzo", "vietnam", "assistenza sociale", "spese"], ["bretton woods", "convertibilità", "oro", "cambi fissi", "dollaro"], ["kippur", "egitto e la siria", "egitto e siria", "1973", "israele"], ["petrolio", "opec", "quadrupl", "shock petrolifero", "stagflazione", "inflazione"]],
 2: [["camp david", "sadat", "begin", "1978", "assassinat"], ["libano", "olp", "sabra", "chatila", "1982", "guerra civile", "profughi"], ["intifada", "hamas", "gaza", "cisgiordania", "1987", "fondamentalismo"]],
 3: [["scià", "shah", "pahlavi", "rivoluzione popolare", "velo"], ["khomeini", "comeini", "teocrazia", "sharia", "sciaria", "repubblica islamica", "anti-americano"], ["ostaggi", "ambasciata", "teheran", "diplomatic"], ["saddam", "iraq", "guerra", "1980", "due milioni", "golfo persico", "kuwait"]],
 4: [["cina", "mao", "1972", "nixon apre", "relazioni diplomatiche", "isolare"], ["salt", "distensione", "helsinki", "armamenti", "diritti umani", "1975"], ["watergate", "dimissioni", "carter", "ford", "1974", "afghanistan"], ["reagan", "impero del male", "scudo spaziale", "spese militari", "linea dura", "1981"]],
 5: [["cile", "allende", "pinochet", "golpe", "1973", "nazionalizzazioni"], ["argentina", "desaparecidos", "giunta", "madri di plaza", "plaza de mayo", "1976"], ["falkland", "democrazia", "sconfitta", "ritorno", "crollo dei regimi"]],
 6: [["shock petroliferi", "industrie", "disoccupazione", "minatori", "sindacal", "inflazione"], ["thatcher", "lady di ferro", "privatizzazion", "neoliberis", "stato sociale"], ["cee", "allargamento", "irlanda", "danimarca", "grecia", "spagna", "portogallo", "parlamento europeo", "mitterrand", "1979"]],
 7: [["briesnev", "griesnev", "brežnev", "leonid", "afghanistan", "immobilismo", "stagnazione"], ["gorbach", "perestro", "glasnost", "glasso", "mikhail", "1985", "democratizz"], ["non intervento", "effetto domino", "muro di berlino", "ungheria", "cecoslovacchia", "romania", "bulgaria", "9 novembre", "riunificazione", "germania est"], ["colpo di stato", "agosto del 91", "1991", "dissol", "csi", "baltiche", "cacciato", "dimett", "eltsin", "yeltsin"]],
 8: [["deng", "xiaoping", "riforme economiche", "capitalismo", "visti", "high tech", "arricchire"], ["monopartitica", "libere elezioni", "mani salde", "apparato industriale", "dittatura", "elezioni solo"], ["tien", "carri", "studente", "giugno", "protest", "piazza", "sangue"]],
}
ORD = {n: list(range(len(CUES[n]))) for n in CUES}
ORD[8] = [1, 2, 0]
OVERRIDE = {}

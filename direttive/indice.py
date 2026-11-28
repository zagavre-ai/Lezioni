"""Genera il PDF, legge in che pagina cade ogni sezione, riscrive l'indice e rigenera.
Ripete finche' i numeri di pagina non cambiano piu'."""
import re, subprocess, sys, html
import pymupdf

DOCS = {
    "docente": ("docente.html", "pdf.js", "Direttive_operative_Docente.pdf"),
    "responsabile": ("responsabile.html", "pdf_resp.js", "Direttive_operative_Responsabile.pdf"),
}

def titoli(sorgente):
    """Titoli delle sezioni: h2 principali e h3 come sottovoci."""
    testo = open(sorgente).read()
    corpo = testo.split("<!-- INDICE_FINE -->", 1)[-1]
    out = []
    for m in re.finditer(r"<h([23])[^>]*>(.*?)</h\1>", corpo, re.S):
        liv, t = int(m.group(1)), re.sub(r"<[^>]+>", "", m.group(2))
        t = html.unescape(t).strip()
        if t.lower() == "indice":
            continue
        out.append((liv, t))
    return out

def titoli_nel_pdf(doc):
    """Ogni titolo stampato nel PDF, con la sua pagina.
    Li distingue dalle voci dell'indice in base alla dimensione del carattere."""
    out = []
    prima = 0
    for i in range(doc.page_count):
        if "in breve" in doc[i].get_text().lower():
            prima = i
            break
    for i in range(prima, doc.page_count):
        for blocco in doc[i].get_text("dict")["blocks"]:
            for riga in blocco.get("lines", []):
                pezzi = [s for s in riga["spans"] if s["size"] >= 10.2]
                if not pezzi:
                    continue
                testo = re.sub(r"\s+", " ", "".join(s["text"] for s in pezzi)).strip()
                if testo:
                    out.append((testo.lower(), i + 1))
    return out

def pagina_di(mappa, titolo, da=1):
    chiave = re.sub(r"\s+", " ", titolo).strip().lower()
    for testo, pag in mappa:
        if pag >= da and (testo == chiave or testo.startswith(chiave[:38])):
            return pag
    return None

def costruisci(sorgente, script, pdf, sottovoci=False):
    precedente = None
    for giro in range(6):
        subprocess.run(["node", script], check=True, capture_output=True)
        doc = pymupdf.open(pdf)
        mappa = titoli_nel_pdf(doc)
        ancore = {}
        for m in re.finditer(r'<h[23][^>]*id="([^"]+)"[^>]*>(.*?)</h[23]>',
                             open(sorgente).read(), re.S):
            ancore[html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()] = m.group(1)
        voci, cursore = [], 1
        for liv, t in titoli(sorgente):
            if liv == 3 and not sottovoci:
                continue
            p = pagina_di(mappa, t, cursore)
            if p:
                cursore = p
                voci.append((liv, t, p))
        doc.close()
        numeri = [v[2] for v in voci]
        righe = []
        for liv, t, p in voci:
            cls = ' class="sotto"' if liv == 3 else ""
            ancora = ancore.get(t, "")
            apri = f'<a href="#{ancora}">' if ancora else ""
            chiudi = "</a>" if ancora else ""
            righe.append(f'<li{cls}>{apri}<span class="pallino"></span>'
                         f'<span class="voce">{html.escape(t)}</span>'
                         f'<span class="punti"></span><span class="pag">{p}</span>{chiudi}</li>')
        blocco = "\n".join(righe)
        s = open(sorgente).read()
        s = re.sub(r"<!-- INDICE_INIZIO -->.*?<!-- INDICE_FINE -->",
                   "<!-- INDICE_INIZIO -->\n" + blocco + "\n<!-- INDICE_FINE -->",
                   s, flags=re.S)
        open(sorgente, "w").write(s)
        if numeri == precedente:
            subprocess.run(["node", script], check=True, capture_output=True)
            d = pymupdf.open(pdf)
            segnalibri = [[1 if liv == 2 else 2, t, p] for liv, t, p in voci]
            for i in range(d.page_count):
                if "da copiare" in d[i].get_text().lower():
                    segnalibri.append([2, "Modello del feedback (da copiare)", i + 1])
                    break
            segnalibri.sort(key=lambda v: v[2])
            d.set_toc(segnalibri)
            d.saveIncr()
            d.close()
            print(f"{pdf}: indice stabile al giro {giro}, {len(voci)} voci, segnalibri aggiunti")
            return
        precedente = numeri
    subprocess.run(["node", script], check=True, capture_output=True)
    print(f"{pdf}: fermato dopo 6 giri")

if __name__ == "__main__":
    for nome, (src, js, pdf) in DOCS.items():
        costruisci(src, js, pdf)

def innesta_copertina(pdf, copertina):
    """Sostituisce la pagina 1 con la copertina a piena pagina,
    lasciando intatta la numerazione del resto."""
    d = pymupdf.open(pdf)
    c = pymupdf.open(copertina)
    toc = d.get_toc()
    d.delete_page(0)
    d.insert_pdf(c, from_page=0, to_page=0, start_at=0)
    d.set_toc(toc)
    d.save(pdf + ".tmp")
    d.close(); c.close()
    import os; os.replace(pdf + ".tmp", pdf)
    print(f"{pdf}: copertina innestata")

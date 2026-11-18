# fa partire il Chromium già installato (senza sandbox) anche per gli strumenti che chiamano chromium.launch() senza opzioni
try:
    from playwright.sync_api import BrowserType
    _l=BrowserType.launch
    def launch(self,*a,**k):
        k.setdefault('executable_path','/opt/pw-browsers/chromium-1243/chrome-linux64/chrome')
        k['args']=list(k.get('args') or [])+['--no-sandbox']
        return _l(self,*a,**k)
    BrowserType.launch=launch
except Exception: pass

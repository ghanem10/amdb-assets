"""AMDB luxury post renderer. Usage: python3 lux.py slides.json outdir"""
import sys, json, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path("/home/claude/amdb")
F = ROOT / "fonts/node_modules/@fontsource"
def ff(fam, pkg, sub, w, style="normal"):
    return f"@font-face{{font-family:{fam};font-weight:{w};font-style:{style};src:url(file://{F}/{pkg}/files/{pkg}-{sub}-{w}-{style}.woff2)}}"
FONTS = "".join([
    ff("Corm","cormorant-garamond","latin",500), ff("Corm","cormorant-garamond","latin",600),
    ff("Corm","cormorant-garamond","latin",500,"italic"),
    ff("Naskh","noto-naskh-arabic","arabic",500), ff("Naskh","noto-naskh-arabic","arabic",600), ff("Naskh","noto-naskh-arabic","arabic",700),
    ff("Plex","ibm-plex-sans-arabic","arabic",300), ff("Plex","ibm-plex-sans-arabic","arabic",400), ff("Plex","ibm-plex-sans-arabic","arabic",500),
    ff("Man","manrope","latin",300), ff("Man","manrope","latin",400), ff("Man","manrope","latin",500), ff("Man","manrope","latin",600), ff("Man","manrope","latin",700),
])

CSS = """
:root{--ink:#06182E;--navy:#0B2A55;--cyan:#1FB6D3;--pearl:#EEF3F6;--silver:#9FB0C2;--mist:#C9D6E2}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;font-family:Man,Plex;-webkit-font-smoothing:antialiased}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;display:flex;flex-direction:column;padding:72px 88px 64px}
.dark{color:var(--pearl);background:radial-gradient(120% 80% at 85% 10%,#103565 0%,#0A2346 40%,var(--ink) 100%)}
.light{color:var(--ink);background:radial-gradient(120% 80% at 90% 0%,#FFFFFF 0%,#F2F6F9 50%,#E6EDF3 100%)}
.grain:after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.05;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.hd{display:flex;align-items:center;gap:22px;position:relative;z-index:2}
.hd img{width:92px;height:92px;border-radius:50%;box-shadow:0 0 0 1px rgba(255,255,255,.25),0 10px 30px rgba(0,0,0,.25)}
.light .hd img{box-shadow:0 0 0 1px rgba(11,42,85,.12),0 10px 26px rgba(11,42,85,.15)}
.hd .nm{font-family:Man;font-weight:600;font-size:23px;letter-spacing:.02em}
.hd .tg{font-family:Man;font-weight:400;font-size:17px;opacity:.6;margin-top:3px;letter-spacing:.01em}
.hd .pg{margin-left:auto;font-family:Man;font-weight:500;font-size:20px;opacity:.55;letter-spacing:.08em}
.arc{position:absolute;left:-120px;right:-120px;z-index:1;pointer-events:none}
.body{position:relative;z-index:2;flex:1;display:flex;flex-direction:column;justify-content:center}
.en{font-family:Corm;font-weight:500;font-size:104px;line-height:.98;letter-spacing:-.01em}
.en i{font-style:italic;color:var(--cyan)}
.light .en i{color:#0E7FA0}
.ar{font-family:Naskh;font-weight:600;font-size:60px;line-height:1.55;direction:rtl;text-align:right;margin-top:40px}
.p{font-family:Man;font-weight:400;font-size:31px;line-height:1.5;margin-top:44px;max-width:800px;opacity:.82}
.par{font-family:Plex;font-weight:400;font-size:31px;line-height:1.75;direction:rtl;text-align:right;margin-top:14px;opacity:.82}
.hair{height:1px;background:linear-gradient(90deg,transparent,rgba(31,182,211,.6),transparent);margin:44px 0 0}
.ft{position:relative;z-index:2;display:flex;justify-content:space-between;align-items:center;padding-top:26px;border-top:1px solid rgba(201,214,226,.22);font-family:Man;font-size:21px;font-weight:500;letter-spacing:.01em}
.light .ft{border-top:1px solid rgba(11,42,85,.14)}
.ft span{display:flex;align-items:center;gap:11px;opacity:.85}
.ft svg{width:24px;height:24px;flex:none;color:var(--cyan)}
.light .ft svg{color:#0E7FA0}
.big{font-family:Corm;font-weight:500;font-size:300px;line-height:.8;color:var(--cyan);opacity:.9}
.k{font-family:Man;font-weight:500;font-size:22px;letter-spacing:.06em;color:var(--cyan);margin-bottom:28px}
.light .k{color:#0E7FA0}
.svc{display:flex;justify-content:space-between;align-items:baseline;padding:26px 0;border-bottom:1px solid rgba(11,42,85,.12)}
.svc:first-child{border-top:1px solid rgba(11,42,85,.12)}
.svc .e{font-family:Corm;font-weight:500;font-size:50px}
.svc .a{font-family:Naskh;font-weight:600;font-size:36px;direction:rtl;opacity:.85}
.cta{display:inline-flex;align-items:center;gap:14px;align-self:flex-start;margin-top:48px;padding:22px 34px;border-radius:999px;background:var(--cyan);color:var(--ink);font-family:Man;font-weight:700;font-size:26px}
"""

ICON = {
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6 8.5-6"/></svg>',
 "wa":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 20l1.2-3.6A8 8 0 1 1 8 19z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.6-2-1-1 .8c-1-.4-2.3-1.7-2.7-2.7l.8-1-1-2z" fill="currentColor" stroke="none"/></svg>',
 "ig":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1" fill="currentColor"/></svg>',
}
LOGO = f"file://{ROOT}/logo_round.png"

def arc(top, h=520, op=.55, light=False):
    c = "#0E7FA0" if light else "#1FB6D3"
    return (f'<svg class="arc" style="top:{top}px" height="{h}" viewBox="0 0 1320 {h}" preserveAspectRatio="none">'
            f'<defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{c}" stop-opacity="0"/><stop offset=".5" stop-color="{c}" stop-opacity="{op}"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient></defs>'
            f'<path d="M0 {h-10} Q 660 {-h*0.55} 1320 {h-10}" fill="none" stroke="url(#g)" stroke-width="1.6"/>'
            f'<path d="M0 {h+30} Q 660 {-h*0.35} 1320 {h+30}" fill="none" stroke="url(#g)" stroke-width="1" opacity=".5"/></svg>')

def header(page=""):
    pg = f'<div class="pg">{page}</div>' if page else ""
    return (f'<div class="hd"><img src="{LOGO}"><div><div class="nm">Aloui Med Digital Bridge</div>'
            f'<div class="tg">Bridging healthcare with digital solutions</div></div>{pg}</div>')

FOOTER = (f'<div class="ft"><span>{ICON["mail"]}amdb.agency@yahoo.com</span>'
          f'<span>{ICON["wa"]}+216 94 871 811</span><span>{ICON["ig"]}@amdb_agency</span></div>')

def page(cls, inner):
    return f"<div class='s {cls} grain'>{inner}</div>"

def render(slides, outdir):
    out = pathlib.Path(outdir).resolve(); out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width":1080,"height":1350})
        for name, html in slides.items():
            doc = f"<html><head><meta charset='utf-8'><style>{FONTS}{CSS}</style></head><body>{html}</body></html>"
            f = out / f"{name}.html"; f.write_text(doc, encoding="utf-8")
            pg.goto(f"file://{f}"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            pg.screenshot(path=str(out / f"{name}.jpg"), type="jpeg", quality=94)
        b.close()

if __name__ == "__main__":
    spec = sys.argv[1]
    ns = {"arc":arc,"header":header,"FOOTER":FOOTER,"page":page}
    exec(pathlib.Path(spec).read_text(encoding="utf-8"), ns)
    render(ns["SLIDES"], sys.argv[2])

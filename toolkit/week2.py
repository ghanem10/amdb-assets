SLIDES = {}

CHECK = '<svg viewBox="0 0 24 24" width="30" height="30"><circle cx="12" cy="12" r="11" fill="#1FB6D3" opacity=".16"/><path d="M7 12.5l3.2 3.2L17 9" fill="none" stroke="#0E7FA0" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

X_CSS = """<style>
.top{position:relative;z-index:2;margin-top:70px}
.h1{font-family:Corm;font-weight:500;font-size:96px;line-height:1.0;letter-spacing:-.01em}
.h1ar{font-family:Naskh;font-weight:700;font-size:54px;line-height:1.55;direction:rtl;text-align:right;margin-top:26px}
.map{position:absolute;left:0;right:0;top:640px;height:560px;z-index:1}
.pcard{position:absolute;z-index:3;left:88px;top:700px;width:560px;border-radius:30px;background:#F6F9FB;color:#06182E;
  box-shadow:0 30px 80px rgba(0,0,0,.45),0 0 0 1px rgba(255,255,255,.4);padding:34px 36px 20px}
.pcard .t{display:flex;justify-content:space-between;align-items:baseline}
.pcard .t .e{font-family:Man;font-weight:700;font-size:27px}
.pcard .t .a{font-family:Plex;font-weight:500;font-size:25px;direction:rtl;color:#3A4E66}
.pcard .sub{font-family:Man;font-size:18px;color:#6B7F95;margin-top:6px}
.pcard .row{display:flex;align-items:center;gap:16px;padding:15px 0;border-top:1px solid rgba(11,42,85,.09)}
.pcard .row:first-of-type{margin-top:20px}
.pcard .row .e{font-family:Man;font-weight:500;font-size:22px;flex:1}
.pcard .row .a{font-family:Plex;font-weight:500;font-size:22px;direction:rtl;color:#3A4E66}
.pin{position:absolute;z-index:2;left:790px;top:770px;width:120px;height:160px}
.note{position:absolute;z-index:3;right:88px;top:990px;width:300px;text-align:right}
.note .e{font-family:Corm;font-style:italic;font-weight:500;font-size:36px;line-height:1.1;color:#EEF3F6}
.note .a{font-family:Plex;font-size:24px;direction:rtl;color:#9FB0C2;margin-top:8px}
</style>"""

# ---------- P1: Google Maps profile (dark) ----------
streets = "".join([
 '<path d="M-20 120 C 240 90, 420 180, 700 140 S 1040 60, 1100 90" />',
 '<path d="M-20 330 C 200 300, 520 360, 760 300 S 1000 260, 1100 280" />',
 '<path d="M-20 470 C 300 450, 600 500, 1100 440" />',
 '<path d="M180 -10 C 210 160, 160 360, 230 570" />',
 '<path d="M520 -10 C 500 200, 560 380, 520 570" />',
 '<path d="M860 -10 C 820 150, 900 330, 870 570" />',
])
minor = "".join(f'<path d="M{x} -10 L {x+40} 570"/>' for x in (60,330,690,980)) + "".join(f'<path d="M-20 {y} L 1100 {y-30}"/>' for y in (40,230,400,540))
MAP = (f'<svg class="map" viewBox="0 0 1080 560" preserveAspectRatio="none">'
       f'<defs><radialGradient id="glow" cx="78%" cy="38%" r="40%"><stop offset="0" stop-color="#1FB6D3" stop-opacity=".28"/><stop offset="1" stop-color="#1FB6D3" stop-opacity="0"/></radialGradient>'
       f'<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".25" stop-color="#fff" stop-opacity="1"/><stop offset=".85" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
       f'<mask id="m"><rect width="1080" height="560" fill="url(#fade)"/></mask></defs>'
       f'<g mask="url(#m)"><rect width="1080" height="560" fill="url(#glow)"/>'
       f'<g fill="none" stroke="#9FC8E2" stroke-opacity=".07" stroke-width="2">{minor}</g>'
       f'<g fill="none" stroke="#9FC8E2" stroke-opacity=".16" stroke-width="5" stroke-linecap="round">{streets}</g>'
       f'<circle cx="845" cy="215" r="120" fill="none" stroke="#1FB6D3" stroke-opacity=".22" stroke-width="1.5"/>'
       f'<circle cx="845" cy="215" r="200" fill="none" stroke="#1FB6D3" stroke-opacity=".12" stroke-width="1.2"/></g></svg>')
PIN = ('<svg class="pin" viewBox="0 0 120 160"><defs><linearGradient id="pg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5AD3EA"/><stop offset="1" stop-color="#0E7FA0"/></linearGradient></defs>'
       '<ellipse cx="60" cy="150" rx="26" ry="7" fill="#000" opacity=".35"/>'
       '<path d="M60 146 C 60 146 14 92 14 58 A 46 46 0 1 1 106 58 C 106 92 60 146 60 146 Z" fill="url(#pg)"/>'
       '<circle cx="60" cy="58" r="17" fill="#06182E"/></svg>')
rows = [("Opening hours","أوقات العمل"),("Phone and WhatsApp","الهاتف وواتساب"),("Recent photos","صور حديثة"),("Replies to reviews","الرد على التقييمات")]
CARD = ('<div class="pcard"><div class="t"><div class="e">Your clinic</div><div class="a">عيادتك</div></div>'
        '<div class="sub">Google Business Profile</div>' +
        "".join(f'<div class="row">{CHECK}<div class="e">{e}</div><div class="a">{a}</div></div>' for e,a in rows) + '</div>')
SLIDES["p1"] = page("dark", X_CSS + header() + MAP + PIN + CARD + """
<div class="top">
  <div class="h1">Patients often meet you on Google Maps first.</div>
  <div class="h1ar">غالبًا ما يتعرّف عليك المريض<br>أولًا على خرائط غوغل.</div>
</div>
<div class="note"><div class="e">Four details<br>to check today.</div><div class="a">أربع تفاصيل راجِعها اليوم</div></div>
<div style="flex:1"></div>""" + FOOTER)

# ---------- P2: carousel "3 posts that build trust" ----------
C_CSS = """<style>
.cv-h{font-family:Corm;font-weight:500;font-size:100px;line-height:.98;letter-spacing:-.01em;margin-top:60px;text-wrap:balance;position:relative;z-index:3}
.cv-a{font-family:Naskh;font-weight:700;font-size:54px;line-height:1.55;direction:rtl;text-align:right;margin-top:30px;position:relative;z-index:3}
.fan{position:absolute;left:0;right:0;top:720px;height:440px;z-index:2}
.fan .tile{position:absolute !important;width:300px;height:300px;border-radius:26px;background:linear-gradient(160deg,#123F70,#0A2346);border:1px solid rgba(159,200,226,.22);box-shadow:0 30px 70px rgba(0,0,0,.45);padding:26px;color:#EEF3F6;overflow:hidden}
.tile .bar{height:12px;border-radius:6px;background:rgba(11,42,85,.12);margin-top:12px}
.tile .tag{font-family:Man;font-weight:700;font-size:15px;letter-spacing:.04em;color:#0E7FA0}
.num{font-family:Man;font-weight:200;font-size:150px;line-height:.8;color:#0E7FA0}
.st-e{font-family:Corm;font-weight:500;font-size:84px;line-height:1.0;margin-top:34px;text-wrap:balance}
.st-a{font-family:Naskh;font-weight:700;font-size:48px;line-height:1.55;direction:rtl;text-align:right;margin-top:18px}
.row2{display:flex;gap:46px;align-items:center;margin-top:54px}
.mini{flex:none;width:380px;height:380px;border-radius:28px;background:linear-gradient(160deg,#0B2A55,#06182E);box-shadow:0 26px 60px rgba(11,42,85,.28);padding:30px;color:#EEF3F6;position:relative;overflow:hidden}
.mini .lbl{font-family:Man;font-weight:600;font-size:18px;letter-spacing:.01em;color:#1FB6D3}
.desc .e{text-wrap:pretty;font-family:Man;font-size:27px;line-height:1.5;color:#22364F}
.desc .a{text-wrap:balance;font-family:Plex;font-size:28px;line-height:1.7;direction:rtl;text-align:right;color:#22364F;margin-top:18px}
.ctap{display:inline-flex;align-items:center;gap:14px;align-self:flex-start;margin-top:56px;padding:24px 36px;border-radius:999px;background:#1FB6D3;color:#06182E;font-family:Man;font-weight:700;font-size:28px}
</style>"""

def tile_body(kind, light=False):
    if kind=="walk":
        steps=[("Arrival","الوصول"),("Consultation","الاستشارة"),("Your plan","خطة العلاج")]
        s=""
        for i,(e,a) in enumerate(steps):
            s+=(f'<div style="display:flex;align-items:center;gap:16px;margin-top:{26 if i else 30}px">'
                f'<div style="width:22px;height:22px;border-radius:50%;border:2px solid #1FB6D3;background:{"#1FB6D3" if i==0 else "transparent"};flex:none"></div>'
                f'<div style="font-family:Man;font-weight:600;font-size:22px;flex:1">{e}</div><div style="font-family:Plex;font-size:21px;direction:rtl;opacity:.75">{a}</div></div>')
        line='<div style="position:absolute;left:40px;top:118px;width:2px;height:150px;background:rgba(31,182,211,.35)"></div>'
        return '<div class="lbl">Your first visit</div>'+line+s
    if kind=="qa":
        return ('<div class="lbl">Patient question</div>'
                '<div style="font-family:Corm;font-weight:500;font-size:150px;line-height:.8;color:#1FB6D3;margin-top:22px">?</div>'
                '<div style="height:14px;border-radius:7px;background:rgba(238,243,246,.85);width:86%;margin-top:18px"></div>'
                '<div style="height:14px;border-radius:7px;background:rgba(238,243,246,.85);width:62%;margin-top:12px"></div>'
                '<div style="height:10px;border-radius:5px;background:rgba(238,243,246,.3);width:90%;margin-top:26px"></div>'
                '<div style="height:10px;border-radius:5px;background:rgba(238,243,246,.3);width:74%;margin-top:10px"></div>')
    if kind=="team":
        av="".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:12px"><div style="width:74px;height:74px;border-radius:50%;background:linear-gradient(135deg,#9FB0C2,#5C7390);box-shadow:0 0 0 3px rgba(31,182,211,{.9 if i==1 else .25})"></div><div style="height:9px;width:62px;border-radius:5px;background:rgba(238,243,246,.55)"></div><div style="height:8px;width:44px;border-radius:4px;background:rgba(238,243,246,.25)"></div></div>' for i in range(3))
        return ('<div class="lbl">Meet the team</div>'
                f'<div style="display:flex;justify-content:space-between;margin-top:56px">{av}</div>'
                '<div style="height:10px;border-radius:5px;background:rgba(238,243,246,.3);width:80%;margin:44px auto 0"></div>')

SLIDES["p2_1"] = page("dark", C_CSS + header("1 / 5") + """
<div class="cv-h">Three posts that build trust before the first visit.</div>
<div class="cv-a">ثلاثة منشورات تبني الثقة<br>قبل الزيارة الأولى.</div>
<div class="fan">
  <div class="tile mini" style="left:100px;top:70px;transform:rotate(-8deg);width:340px;height:340px;opacity:.9">""" + tile_body("team") + """</div>
  <div class="tile mini" style="left:640px;top:70px;transform:rotate(8deg);width:340px;height:340px;opacity:.9">""" + tile_body("qa") + """</div>
  <div class="tile mini" style="left:360px;top:20px;width:360px;height:360px;box-shadow:0 40px 90px rgba(0,0,0,.6),0 0 0 1px rgba(31,182,211,.5)">""" + tile_body("walk") + """</div>
</div>
<div style="flex:1"></div>
<div class="p" style="font-size:22px;opacity:.55;margin:0 0 26px;position:relative;z-index:3">Swipe &nbsp;&nbsp; <span style="font-family:Plex">اسحب</span></div>""" + FOOTER)

ideas = [
 ("2 / 5","1","walk","The first-visit walkthrough.","جولة الزيارة الأولى.",
  "Show what happens from the waiting room to the end of the consultation. A nervous patient relaxes when they know what to expect.",
  "اشرح ما يحدث من قاعة الانتظار إلى نهاية الاستشارة. المريض القلق يطمئن حين يعرف ما ينتظره."),
 ("3 / 5","2","qa","The question you answer every day.","السؤال الذي تُجيب عنه كل يوم.",
  "Pick one question patients ask at every consultation and answer it in a short post. One question per post.",
  "اختر سؤالًا يطرحه المرضى في كل استشارة، وأجب عنه في منشور قصير. سؤال واحد لكل منشور."),
 ("4 / 5","3","team","The people behind the door.","الفريق الذي يستقبل المريض.",
  "Introduce the team who welcomes patients, with their consent. A familiar face makes the first visit easier.",
  "عرّف بالفريق الذي يستقبل المرضى، بعد موافقتهم. الوجه المألوف يجعل الزيارة الأولى أسهل."),
]
for pg,n,kind,e,a,de,da in ideas:
    SLIDES[f"p2_{int(n)+1}"] = page("light", C_CSS + arc(1000, 228, .45, True) + header(pg) + f"""
<div class="body" style="justify-content:center;padding-bottom:40px">
  <div class="num">{n}</div>
  <div class="st-e">{e}</div>
  <div class="st-a">{a}</div>
  <div class="row2"><div class="mini">{tile_body(kind)}</div>
    <div class="desc"><div class="e">{de}</div><div class="a">{da}</div></div></div>
</div>""" + FOOTER)

SLIDES["p2_5"] = page("dark", C_CSS + arc(1000, 228) + header("5 / 5") + """
<div class="body">
  <div class="en" style="font-size:100px">We can write these for your practice.</div>
  <div class="ar" style="font-size:56px">يمكننا كتابة هذه المنشورات لعيادتك.</div>
  <div class="p">Planned with you, written in Arabic and English.</div>
  <div class="par">نخطّطها معك، ونكتبها بالعربية والإنجليزية.</div>
  <div class="ctap">Message us on WhatsApp<span style="font-family:Plex;font-weight:500;border-left:1px solid rgba(6,24,46,.35);padding-left:14px">راسلنا على واتساب</span></div>
</div>""" + FOOTER)

# ---------- P4: bilingual mirror (light) ----------
M_CSS = """<style>
.mir{display:flex;justify-content:space-between;align-items:flex-start;margin-top:90px;position:relative;z-index:3}
.mir .e{width:450px;font-family:Corm;font-weight:500;font-size:70px;white-space:nowrap;line-height:1.1}
.mir .a{width:440px;font-family:Naskh;font-weight:700;font-size:52px;line-height:1.5;direction:rtl;text-align:right;margin-top:-6px}
.mid{position:absolute;left:540px;top:250px;width:1px;height:330px;background:linear-gradient(180deg,rgba(11,42,85,0),rgba(11,42,85,.25),rgba(11,42,85,0));z-index:2}
.bridge{position:absolute;left:0;top:590px;width:1080px;height:420px;z-index:1}
.bub{position:absolute;z-index:3;padding:22px 30px;border-radius:28px;font-size:30px;box-shadow:0 18px 40px rgba(11,42,85,.14)}
.bub.l{left:88px;top:920px;background:#fff;color:#06182E;font-family:Man;font-weight:500;border-bottom-left-radius:8px}
.bub.r{right:88px;top:920px;background:#0B2A55;color:#EEF3F6;font-family:Plex;font-weight:500;direction:rtl;border-bottom-right-radius:8px}
.apex{position:absolute;z-index:3;left:0;right:0;top:645px;display:flex;flex-direction:column;align-items:center}
.apex .dot{width:34px;height:34px;border-radius:50%;background:#1FB6D3;box-shadow:0 0 0 12px rgba(31,182,211,.16),0 0 0 26px rgba(31,182,211,.07)}
.apex .t{margin-bottom:24px;font-family:Man;font-weight:600;font-size:22px;color:#0B2A55;display:flex;gap:12px}
.apex .t span:last-child{font-family:Plex;font-weight:500;opacity:.7}
.foot2{position:relative;z-index:3;display:flex;justify-content:space-between;gap:60px;margin-bottom:34px}
.foot2 .e{text-wrap:balance;font-family:Man;font-size:25px;line-height:1.5;color:#22364F;width:420px}
.foot2 .a{text-wrap:balance;font-family:Plex;font-size:26px;line-height:1.7;color:#22364F;direction:rtl;text-align:right;width:400px}
</style>"""
BRIDGE = ('<svg class="bridge" viewBox="0 0 1080 420"><defs><linearGradient id="bg2" x1="0" x2="1">'
          '<stop offset="0" stop-color="#0E7FA0" stop-opacity=".15"/><stop offset=".5" stop-color="#0E7FA0" stop-opacity=".9"/><stop offset="1" stop-color="#0E7FA0" stop-opacity=".15"/></linearGradient></defs>'
          '<path d="M150 300 Q 540 -40 930 300" fill="none" stroke="url(#bg2)" stroke-width="3"/>'
          '<path d="M110 340 Q 540 20 970 340" fill="none" stroke="url(#bg2)" stroke-width="1.4" opacity=".55"/>'
          + "".join(f'<line x1="{x}" y1="{300-((x-540)**2*-1+390**2)/390**2*170+0:.0f}" x2="{x}" y2="300" stroke="#0E7FA0" stroke-opacity=".18" stroke-width="1.2"/>' for x in range(230,860,62))
          + '<line x1="60" y1="300" x2="1020" y2="300" stroke="#0B2A55" stroke-opacity=".18" stroke-width="1.5"/></svg>')
SLIDES["p4"] = page("light", M_CSS + header() + """
<div class="mir"><div class="e">Speak to every<br>patient in their<br>language.</div><div class="a">تحدّثْ إلى كلِّ مريضٍ<br>باللغة التي يفكّر بها.</div></div>
<div class="mid"></div>""" + BRIDGE + """
<div class="apex"><div class="t"><span>Your clinic</span><span>عيادتك</span></div><div class="dot"></div></div>
<div class="bub l">When can I book?</div>
<div class="bub r">متى يمكنني الحجز؟</div>
<div style="flex:1"></div>
<div class="foot2"><div class="e">We write every post in Arabic and English, so every patient can follow you with ease.</div>
<div class="a">نكتب كل منشور بالعربية والإنجليزية، حتى يتابعك كل مريض بسهولة.</div></div>""" + FOOTER)

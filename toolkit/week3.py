SLIDES = {}

BASE = """<style>
.ui{font-family:Man}
.uiar{font-family:Plex;direction:rtl}
.phone{position:absolute;z-index:3;border-radius:64px;background:#0A1A30;padding:16px;
  box-shadow:0 60px 120px rgba(0,0,0,.55),0 0 0 2px rgba(159,176,194,.35),inset 0 0 0 1px rgba(255,255,255,.08)}
.phone .scr{width:100%;height:100%;border-radius:50px;overflow:hidden;position:relative}
.sb{display:flex;justify-content:space-between;align-items:center;padding:22px 34px 0;font-family:Man;font-weight:600;font-size:21px}
.notch{position:absolute;top:14px;left:50%;transform:translateX(-50%);width:130px;height:34px;border-radius:20px;background:#0A1A30}
</style>"""

# ---------- P1: WhatsApp away message (dark, night) ----------
P1 = """<style>
.p1h{position:absolute;z-index:4;left:88px;top:250px;width:520px}
.p1h .h1{font-family:Corm;font-weight:500;font-size:86px;line-height:1;letter-spacing:-.01em}
.p1h .h1 i{font-style:italic;color:#1FB6D3}
.p1h .ar{font-family:Naskh;font-weight:700;font-size:52px;line-height:1.6;direction:rtl;text-align:right;margin-top:34px;width:500px}
.p1s{position:absolute;z-index:4;left:88px;top:905px;width:450px}
.p1s .e{font-family:Man;font-size:25px;line-height:1.5;opacity:.8}
.p1s .a{font-family:Plex;font-size:25px;line-height:1.7;direction:rtl;text-align:right;opacity:.8;margin-top:14px;text-wrap:balance}
.glow{position:absolute;z-index:1;left:480px;top:220px;width:760px;height:900px;background:radial-gradient(closest-side,rgba(31,182,211,.22),rgba(31,182,211,0));}
.moon{position:absolute;z-index:1;right:96px;top:196px;width:90px;height:90px;opacity:.6}
.chat{background:#E9EEF2;color:#06182E;height:100%}
.chat .top{background:#0B2A55;color:#EEF3F6;padding:0 0 22px}
.chat .who{display:flex;align-items:center;gap:16px;padding:22px 30px 0}
.chat .av{width:58px;height:58px;border-radius:50%;background:linear-gradient(135deg,#1FB6D3,#0E7FA0);display:flex;align-items:center;justify-content:center;font-family:Man;font-weight:700;font-size:22px;color:#06182E}
.chat .nm{font-family:Man;font-weight:700;font-size:24px}
.chat .st{font-family:Man;font-size:17px;opacity:.65;margin-top:2px}
.chat .day{align-self:center;font-family:Man;font-size:16px;color:#5B6E84;background:#DCE4EB;padding:6px 16px;border-radius:12px;margin:22px auto 6px;width:max-content}
.msgs{display:flex;flex-direction:column;gap:16px;padding:6px 24px}
.b{max-width:84%;border-radius:22px;padding:16px 20px 12px;font-size:22px;line-height:1.55;box-shadow:0 2px 0 rgba(11,42,85,.06)}
.b .t{font-family:Man;font-size:14px;color:#6B7F95;text-align:left;margin-top:4px}
.in{align-self:flex-start;background:#fff;border-top-left-radius:6px}
.out{align-self:flex-end;background:#CFF0F6;border-top-right-radius:6px}
.lab{display:flex;align-items:center;gap:8px;font-family:Man;font-weight:600;font-size:15px;color:#0E7FA0;margin-bottom:6px}
.chips{display:flex;gap:10px;justify-content:flex-end;flex-wrap:wrap;padding:4px 24px 0}
.chip{font-family:Plex;font-size:18px;direction:rtl;padding:9px 18px;border-radius:999px;border:1.5px solid #0E7FA0;color:#0E7FA0;background:#F4FAFC}
</style>"""
MOON = '<svg class="moon" viewBox="0 0 90 90"><path d="M58 12a36 36 0 1 0 20 52A30 30 0 0 1 58 12z" fill="none" stroke="#9FB0C2" stroke-width="2"/></svg>'
CLOCK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0E7FA0" stroke-width="2.4"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
PHONE1 = f"""<div class="phone" style="left:640px;top:262px;width:430px;height:830px;transform:rotate(-4deg)">
<div class="scr"><div class="chat"><div class="top"><div class="sb"><span>21:40</span><span style="opacity:.8">&#9679;&#9679;&#9679;</span></div>
<div class="who"><div class="av">Dr</div><div><div class="nm">Your clinic</div><div class="st">Business account</div></div></div></div>
<div class="day">Today</div>
<div class="msgs">
 <div class="b in"><div class="uiar">مساء الخير، هل يوجد موعد<br>متاح هذا الأسبوع؟</div><div class="t">21:40</div></div>
 <div class="b out"><div class="lab">{CLOCK}Automatic away message</div>
  <div class="uiar">شكرًا على رسالتك. العيادة مغلقة الآن، وسنتواصل معك غدًا ابتداءً من التاسعة صباحًا.</div>
  <div class="ui" style="font-size:19px;color:#3A4E66;margin-top:8px;line-height:1.45">Thank you for your message. The clinic is closed now. We reply tomorrow from 9:00.</div>
  <div class="t">21:40</div></div>
</div>
<div class="chips"><span class="chip">أوقات العمل</span><span class="chip">الموقع</span><span class="chip">حجز موعد</span></div>
</div></div><div class="notch"></div></div>"""
SLIDES["p1_whatsapp"] = page("dark", BASE + P1 + header() + '<div class="glow"></div>' + PHONE1 + """
<div class="p1h"><div class="h1">Patients write<br><i>at night.</i><br>Who replies?</div>
<div class="ar">المريض يراسلك ليلًا.<br>من يردّ عليه؟</div></div>
<div class="p1s"><div class="e">A WhatsApp Business away message answers straight away and tells the patient when the clinic will reply.</div>
<div class="a">رسالة الغياب في واتساب للأعمال تردّ فورًا وتخبر المريض متى ستردّ عليه العيادة.</div></div>
<div style="flex:1"></div>""" + FOOTER)

# ---------- P4: You approve, we publish (light) ----------
P4 = """<style>
.strip{position:absolute;z-index:2;left:60px;right:60px;top:250px;height:440px;border-radius:36px;background:#FFFFFF;
  box-shadow:0 40px 90px rgba(11,42,85,.14),0 0 0 1px rgba(11,42,85,.06);display:flex;padding:38px 34px 0;gap:16px}
.day{flex:1;display:flex;flex-direction:column;align-items:center}
.day .d{font-family:Man;font-weight:600;font-size:21px;color:#0B2A55}
.day .da{font-family:Plex;font-size:17px;color:#6B7F95;margin-top:2px;direction:rtl}
.slot{margin-top:24px;width:100%;aspect-ratio:4/5;border-radius:18px;position:relative;overflow:hidden}
.empty{border:2px dashed rgba(11,42,85,.14)}
.tdark{background:radial-gradient(120% 80% at 80% 10%,#103565,#06182E)}
.tlight{background:linear-gradient(160deg,#FFFFFF,#E3EBF2);box-shadow:inset 0 0 0 1px rgba(11,42,85,.1)}
.slot .l1{position:absolute;left:14px;right:14px;height:9px;border-radius:5px}
.slot .tm{position:absolute;left:0;right:0;bottom:-46px;text-align:center;font-family:Man;font-size:17px;color:#6B7F95}
.tm2{font-family:Man;font-weight:500;font-size:18px;color:#6B7F95;margin-top:14px}
.sum{position:absolute;z-index:3;left:100px;top:612px;display:flex;align-items:center;gap:14px;font-family:Man;font-weight:500;font-size:21px;color:#0B2A55}
.sum .dot{width:10px;height:10px;border-radius:50%;background:#0E7FA0}
.sum .a{font-family:Plex;color:#6B7F95;direction:rtl}
.ok{position:absolute;right:10px;top:10px;width:30px;height:30px;border-radius:50%;background:#0E7FA0;display:flex;align-items:center;justify-content:center}
.seal{position:absolute;z-index:3;left:790px;top:560px;width:220px;height:220px;border-radius:50%;background:#06182E;color:#EEF3F6;
  display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 30px 60px rgba(6,24,46,.35);transform:rotate(-8deg)}
.seal .r{position:absolute;inset:12px;border-radius:50%;border:1.5px solid rgba(31,182,211,.6)}
.seal .e{font-family:Corm;font-style:italic;font-weight:500;font-size:40px;line-height:1}
.seal .a{font-family:Naskh;font-weight:700;font-size:28px;margin-top:6px}
.p4h{position:absolute;z-index:3;left:88px;right:88px;top:800px}
.p4h .h1{font-family:Corm;font-weight:500;font-size:112px;line-height:.95;letter-spacing:-.015em;color:#06182E}
.p4h .h1 i{font-style:italic;color:#0E7FA0}
.p4row{position:absolute;z-index:3;left:88px;right:88px;top:1055px;display:flex;justify-content:space-between;gap:60px}
.p4row .e{font-family:Man;font-size:23px;line-height:1.5;color:#3A4E66;width:440px}
.p4row .a{font-family:Plex;font-size:23px;line-height:1.7;color:#3A4E66;direction:rtl;text-align:right;width:420px;text-wrap:balance}
.p4ar{position:absolute;z-index:3;right:88px;top:812px;text-align:right;direction:rtl;font-family:Naskh;font-weight:700;font-size:60px;line-height:1.45;color:#06182E}
</style>"""
TICK = '<svg width="16" height="16" viewBox="0 0 24 24"><path d="M6 12.5l4 4L18 8" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def tile(kind, t):
    if kind == "empty":
        return f'<div class="slot empty"></div>'
    if kind == "img":
        inner = ('<div class="l1" style="top:26px;width:40%;background:rgba(238,243,246,.85)"></div>'
                 '<div class="l1" style="top:44px;width:60%;background:rgba(238,243,246,.5)"></div>'
                 '<div style="position:absolute;left:22%;top:45%;width:56%;height:40%;border-radius:12px;background:#E9EEF2;opacity:.9"></div>')
        cls = "tdark"
    elif kind == "reel":
        inner = ('<svg style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)" width="54" height="54" viewBox="0 0 54 54"><circle cx="27" cy="27" r="26" fill="rgba(255,255,255,.14)" stroke="rgba(255,255,255,.6)"/><path d="M22 17l15 10-15 10z" fill="#EEF3F6"/></svg>'
                 '<div class="l1" style="bottom:22px;width:50%;left:25%;background:rgba(31,182,211,.8)"></div>')
        cls = "tdark"
    elif kind == "car":
        inner = ('<div style="position:absolute;left:22%;top:24%;width:56%;height:56%;border-radius:10px;background:#fff;box-shadow:0 0 0 1px rgba(11,42,85,.12),8px -8px 0 -2px #D5E0E9,16px -16px 0 -4px #C4D3DF"></div>'
                 '<div style="position:absolute;bottom:14px;left:0;right:0;display:flex;justify-content:center;gap:6px">' + '<span style="width:7px;height:7px;border-radius:50%;background:#0E7FA0"></span>' + '<span style="width:7px;height:7px;border-radius:50%;background:#B9C8D6"></span>'*4 + '</div>')
        cls = "tlight"
    else:  # light image
        inner = ('<div class="l1" style="top:26px;width:44%;background:#0B2A55;opacity:.8"></div>'
                 '<div class="l1" style="top:44px;width:62%;background:#0B2A55;opacity:.3"></div>'
                 '<div style="position:absolute;left:18%;top:46%;width:64%;height:36%;border-radius:50% 50% 0 0;border:2px solid #0E7FA0;border-bottom:none;opacity:.7"></div>')
        cls = "tlight"
    return f'<div class="slot {cls}">{inner}<div class="ok">{TICK}</div></div><div class="tm2">{t}</div>'
days = [("Mon","الإثنين","img","10:00"),("Tue","الثلاثاء","empty",""),("Wed","الأربعاء","reel","18:00"),
        ("Thu","الخميس","limg","10:00"),("Fri","الجمعة","car","10:00"),("Sat","السبت","empty","")]
STRIP = '<div class="strip">' + "".join(f'<div class="day"><div class="d">{d}</div><div class="da">{a}</div>{tile(k,t)}</div>' for d,a,k,t in days) + '</div>'
SLIDES["p4_approve"] = page("light", BASE + P4 + header() + STRIP + """
<div class="sum"><span class="dot"></span>4 posts this week, in Arabic and English<span class="a">أربعة منشورات هذا الأسبوع</span></div>
<div class="seal"><div class="r"></div><div class="e">Approved</div><div class="a">تمّت الموافقة</div></div>
<div class="p4h"><div class="h1">You approve.<br><i>We publish.</i></div></div>
<div class="p4ar">أنت توافق،<br>ونحن ننشر.</div>
<div class="p4row"><div class="e">Every week we plan, write in Arabic and English, and design four posts. You review them in one message.</div>
<div class="a">كل أسبوع نخطّط ونكتب بالعربية والإنجليزية ونصمّم أربعة منشورات، وتراجعها أنت في رسالة واحدة.</div></div>
<div style="flex:1"></div>""" + FOOTER)

# ---------- P2: Story Highlights carousel ----------
CAR = """<style>
.pgn{position:absolute;z-index:4;right:88px;top:104px;font-family:Man;font-weight:500;font-size:20px;opacity:.55;letter-spacing:.08em}
.ch{position:absolute;z-index:4;left:88px;right:88px;top:250px}
.ch .h1{font-family:Corm;font-weight:500;font-size:96px;line-height:1;letter-spacing:-.01em}
.ch .h1 i{font-style:italic;color:#1FB6D3}
.ch .ar{font-family:Naskh;font-weight:700;font-size:54px;line-height:1.6;direction:rtl;text-align:right;margin-top:30px}
.rings{position:absolute;z-index:3;left:0;right:0;top:790px;display:flex;justify-content:center;gap:56px}
.rg{display:flex;flex-direction:column;align-items:center;width:250px}
.rg .o{width:236px;height:236px;border-radius:50%;padding:7px;background:conic-gradient(from 210deg,#1FB6D3,#9FE3F0,#9FB0C2,#1FB6D3)}
.rg .o .in{width:100%;height:100%;border-radius:50%;background:#06182E;border:7px solid #0A2346;display:flex;align-items:center;justify-content:center}
.rg .e{font-family:Man;font-weight:600;font-size:26px;margin-top:22px}
.rg .a{font-family:Plex;font-size:24px;opacity:.7;direction:rtl;margin-top:2px}
.swipe{position:absolute;z-index:4;left:88px;top:1150px;font-family:Man;font-size:20px;opacity:.55;display:flex;gap:12px;align-items:center}
/* interior */
.num{font-family:Corm;font-weight:500;font-size:150px;line-height:.8;color:#0E7FA0;font-variant-numeric:lining-nums}
.it{position:absolute;z-index:3;left:88px;right:88px;top:240px;display:flex;justify-content:space-between;align-items:flex-end}
.it .tt{font-family:Corm;font-weight:500;font-size:76px;line-height:1;color:#06182E;margin-top:24px}
.it .ta{font-family:Naskh;font-weight:700;font-size:50px;direction:rtl;text-align:right;color:#06182E;line-height:1.5}
.sp{position:absolute;z-index:3;left:88px;top:530px;width:400px;height:650px;border-radius:52px;background:#0A1A30;padding:12px;
  box-shadow:0 40px 80px rgba(11,42,85,.28),0 0 0 1.5px rgba(11,42,85,.25)}
.sp .scr{width:100%;height:100%;border-radius:42px;overflow:hidden;position:relative;background:radial-gradient(120% 70% at 80% 0%,#123A6E,#06182E);color:#EEF3F6}
.bars{display:flex;gap:6px;padding:26px 22px 0}
.bars span{flex:1;height:4px;border-radius:2px;background:rgba(238,243,246,.3)}
.bars span.on{background:#EEF3F6}
.sh{display:flex;align-items:center;gap:12px;padding:16px 22px}
.sh .av{width:40px;height:40px;border-radius:50%;background:conic-gradient(#1FB6D3,#9FB0C2,#1FB6D3);padding:3px}
.sh .av div{width:100%;height:100%;border-radius:50%;background:#0B2A55}
.sh .n{font-family:Man;font-weight:600;font-size:19px}
.sc{padding:26px 26px 0}
.sc .k{font-family:Man;font-weight:600;font-size:17px;color:#1FB6D3}
.sc .h{font-family:Corm;font-weight:500;font-size:44px;line-height:1.05;margin-top:8px}
.sc .ha{font-family:Naskh;font-weight:700;font-size:30px;direction:rtl;text-align:right;margin-top:6px}
.rw{display:flex;align-items:center;gap:12px;margin:0 22px;padding:15px 16px;border-radius:16px;background:rgba(238,243,246,.08);margin-top:12px}
.rw .ic{width:34px;height:34px;border-radius:50%;background:rgba(31,182,211,.18);display:flex;align-items:center;justify-content:center;flex:none}
.rw .e{font-family:Man;font-size:18px;flex:1}
.rw .a{font-family:Plex;font-size:17px;direction:rtl;opacity:.7}
.btn{margin:22px 22px 0;padding:16px;border-radius:999px;background:#1FB6D3;color:#06182E;font-family:Man;font-weight:700;font-size:19px;text-align:center}
.ds{position:absolute;z-index:3;left:540px;right:88px;top:560px}
.ds .e{font-family:Man;font-size:27px;line-height:1.55;color:#3A4E66}
.ds .a{font-family:Plex;font-size:27px;line-height:1.8;color:#3A4E66;direction:rtl;text-align:right;margin-top:26px;text-wrap:balance}
.ds .hr{height:1px;background:rgba(11,42,85,.14);margin:34px 0}
.mini{display:flex;gap:16px;margin-top:6px}
.mini .c{width:66px;height:66px;border-radius:50%;padding:4px;background:#C9D6E2}
.mini .c.on{background:conic-gradient(from 210deg,#1FB6D3,#9FE3F0,#0E7FA0,#1FB6D3)}
.mini .c div{width:100%;height:100%;border-radius:50%;background:#fff;border:3px solid #fff;display:flex;align-items:center;justify-content:center}
</style>"""
def ic(path, col="#1FB6D3", size=None):
    s = size or 30
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'
I_DOOR = '<path d="M5 21V4.5A1.5 1.5 0 0 1 6.5 3h11A1.5 1.5 0 0 1 19 4.5V21"/><path d="M3 21h18"/><circle cx="15" cy="12.5" r=".9" fill="currentColor"/>'
I_LEAF = '<path d="M12 3c3.5 3.2 5.5 6.3 5.5 9.5a5.5 5.5 0 0 1-11 0C6.5 9.3 8.5 6.2 12 3z"/><path d="M12 10v8"/>'
I_CAL = '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="M9 14.5l2 2 4-4"/>'
I_PIN = '<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>'
I_BAG = '<rect x="4" y="7.5" width="16" height="12.5" rx="2.5"/><path d="M9 7.5V6a3 3 0 0 1 6 0v1.5"/>'
I_CLK = '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>'
I_INFO = '<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5"/><circle cx="12" cy="8" r=".9" fill="currentColor"/>'
I_USER = '<circle cx="12" cy="8.5" r="3.5"/><path d="M5 20c1.2-3.6 4-5.5 7-5.5s5.8 1.9 7 5.5"/>'
I_SEQ = '<path d="M5 6h14M5 12h14M5 18h9"/>'

def ring(icon, e, a):
    return f'<div class="rg"><div class="o"><div class="in">{ic(icon,"#9FE3F0",86)}</div></div><div class="e">{e}</div><div class="a">{a}</div></div>'

SLIDES["p2_carousel_1"] = page("dark", BASE + CAR + header() + '<div class="pgn">1 / 5</div>' + arc(640, 420, .35) + """
<div class="ch"><div class="h1">Three Story Highlights<br>that work like a<br><i>mini website.</i></div>
<div class="ar">ثلاث قصص مثبّتة تعمل<br>كموقع صغير لعيادتك.</div></div>
<div class="rings">""" + ring(I_DOOR,"First visit","الزيارة الأولى") + ring(I_LEAF,"Treatments","العلاجات") + ring(I_CAL,"Book","الحجز") + """</div>
<div style="flex:1"></div>""" + FOOTER)

def story(bar, title_k, title_e, title_a, rows, button=None):
    bars = "".join(f'<span class="{"on" if i<=bar else ""}"></span>' for i in range(3))
    rws = "".join(f'<div class="rw"><div class="ic">{ic(p,"#1FB6D3",20)}</div><div class="e">{e}</div><div class="a">{a}</div></div>' for p,e,a in rows)
    btn = f'<div class="btn">{button}</div>' if button else ""
    return (f'<div class="sp"><div class="scr"><div class="bars">{bars}</div>'
            f'<div class="sh"><div class="av"><div></div></div><div class="n">Your clinic</div></div>'
            f'<div class="sc"><div class="k">{title_k}</div><div class="h">{title_e}</div><div class="ha">{title_a}</div></div>'
            f'<div style="height:14px"></div>{rws}{btn}</div></div>')

def mini(on):
    icons=[I_DOOR,I_LEAF,I_CAL]
    return '<div class="mini">' + "".join(f'<div class="c {"on" if i==on else ""}"><div>{ic(p,"#0E7FA0" if i==on else "#9FB0C2",26)}</div></div>' for i,p in enumerate(icons)) + '</div>'

INTER = [
 ("2 / 5","1","First visit","الزيارة الأولى",
  story(0,"First visit","Before you come","قبل أن تأتي",[(I_DOOR,"The entrance","المدخل"),(I_PIN,"Where to park","مكان الركن"),(I_BAG,"What to bring","ماذا تحضر")]),
  "Show the entrance, where to park, what to bring and how the first consultation goes.",
  "أظهر مدخل العيادة، وأين يركن المريض سيارته، وما يحضره معه، وكيف تجري الاستشارة الأولى."),
 ("3 / 5","2","Treatments","العلاجات",
  story(1,"Treatments","Laser session","جلسة الليزر",[(I_INFO,"What it is","ما هو"),(I_USER,"Who it suits","لمن يناسب"),(I_SEQ,"The session","الجلسة")]),
  "One story per treatment: what it is, who it suits and how a session goes. Give clear information and leave out promises of results.",
  "قصة لكل علاج: ما هو، ولمن يناسب، وكيف تجري الجلسة، بمعلومة واضحة ودون وعود بالنتائج."),
 ("4 / 5","3","Book","الحجز",
  story(2,"Book","Book your visit","احجز موعدك",[(I_CLK,"Opening hours","أوقات العمل"),(I_PIN,"Location","الموقع")],button="Message us on WhatsApp"),
  "Opening hours, location and a WhatsApp button. Update it whenever something changes.",
  "أوقات العمل والموقع وزر واتساب، مع تحديثها كلما تغيّر شيء."),
]
for i,(pg,n,te,ta,ph,de,da) in enumerate(INTER):
    SLIDES[f"p2_carousel_{i+2}"] = page("light", BASE + CAR + header() + f'<div class="pgn">{pg}</div>' + f"""
<div class="it"><div><div class="num">{n}</div><div class="tt">{te}</div></div><div class="ta">{ta}</div></div>
{ph}
<div class="ds">{mini(i)}<div class="hr"></div><div class="e">{de}</div><div class="a">{da}</div></div>
<div style="flex:1"></div>""" + FOOTER)

SLIDES["p2_carousel_5"] = page("dark", BASE + CAR + header() + '<div class="pgn">5 / 5</div>' + arc(840, 420, .35) + """
<div class="ch" style="top:270px"><div class="h1">We design and write<br>your highlights in<br><i>Arabic and English.</i></div>
<div class="ar">نصمّم قصصك المثبّتة<br>ونكتبها بالعربية والإنجليزية.</div></div>
<div class="rings" style="top:790px;justify-content:flex-start;left:88px;gap:34px">""" + "".join(f'<div class="rg" style="width:150px"><div class="o" style="width:130px;height:130px;padding:5px"><div class="in" style="border-width:5px">{ic(p,"#9FE3F0",46)}</div></div><div class="e" style="font-size:20px;margin-top:14px">{e}</div><div class="a" style="font-size:19px">{a}</div></div>' for p,e,a in [(I_DOOR,"First visit","الزيارة الأولى"),(I_LEAF,"Treatments","العلاجات"),(I_CAL,"Book","الحجز")]) + """</div>
<div style="position:absolute;z-index:4;left:88px;top:1060px;display:flex;align-items:center;gap:18px;padding:22px 34px;border-radius:999px;background:#1FB6D3;color:#06182E;font-family:Man;font-weight:700;font-size:27px">
""" + ic('<path d="M4 20l1.2-3.6A8 8 0 1 1 8 19z"/>',"#06182E",30) + """Message us on WhatsApp</div>
<div style="position:absolute;z-index:4;right:88px;top:1078px;font-family:Plex;font-size:27px;opacity:.8;direction:rtl">راسلنا على واتساب <span dir="ltr" style="font-family:Man">+216 93 871 805</span></div>
<div style="flex:1"></div>""" + FOOTER)

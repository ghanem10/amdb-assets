SLIDES = {}

# Post 1: single image, dark
SLIDES["p1"] = page("dark", arc(1000, 228) + header() + """
<div class="body">
  <div class="en">Your patients search for you before they book.</div>
  <div class="ar">مرضاك يبحثون عنك قبل أن يحجزوا.</div>
  <div class="hair" style="width:260px"></div>
  <div class="p">In a few seconds, what they find decides whether they trust you.</div>
  <div class="par">وفي ثوانٍ قليلة، ما يجدونه يقرّر هل يثقون بك.</div>
</div>""" + FOOTER)

# Post 2: carousel, 5 slides
SLIDES["p2_1"] = page("dark", arc(1000, 228) + header("1 / 5") + """
<div class="body">
  <div class="en" style="font-size:112px">Three signs your Instagram is turning patients away.</div>
  <div class="ar" style="font-size:52px">ثلاث علامات أن حسابك يُبعد عنك المرضى.</div>
  <div class="p" style="font-size:24px;opacity:.55;margin-top:36px">Swipe &nbsp;&nbsp; اسحب</div>
</div>""" + FOOTER)

signs = [
  ("2 / 5","1","Your last post was months ago.","آخر منشور لك كان منذ أشهر.",
   "A silent account makes patients wonder if the clinic is still open.",
   "الحساب المتوقف يجعل المريض يتساءل هل العيادة ما زالت تعمل."),
  ("3 / 5","2","There is no clear way to book.","لا توجد طريقة واضحة للحجز.",
   "If your number takes effort to find, the patient books somewhere else.",
   "إذا تعب المريض في البحث عن رقمك، سيحجز عند غيرك."),
  ("4 / 5","3","Your visuals don't match your care.","صورك لا تعكس مستوى خدمتك.",
   "Excellent medicine deserves an image that looks just as good.",
   "الطب المتميّز يستحق صورة في نفس المستوى."),
]
for i,(pg,n,en,ar,p,par) in enumerate(signs):
    SLIDES[f"p2_{i+2}"] = page("light", arc(1000, 228, .45, True) + header(pg) + f"""
<div class="body">
  <div class="big" style="font-family:Man;font-weight:300;font-size:200px;color:#0E7FA0">{n}</div>
  <div class="en" style="font-size:88px;margin-top:30px">{en}</div>
  <div class="ar" style="font-size:54px;margin-top:26px">{ar}</div>
  <div class="p" style="margin-top:36px">{p}</div>
  <div class="par">{par}</div>
</div>""" + FOOTER)

SLIDES["p2_5"] = page("dark", arc(1000, 228) + header("5 / 5") + """
<div class="body">
  <div class="en">Your account can bring patients to your door.</div>
  <div class="ar">حسابك قادر أن يجلب لك المرضى.</div>
  <div class="p">We build and manage it for you, in Arabic and English.</div>
  <div class="par">نحن نبنيه وندير محتواه، بالعربية والإنجليزية.</div>
  <div class="cta">Message us on WhatsApp<span style="font-family:Plex;font-weight:500;border-left:1px solid rgba(6,24,46,.35);padding-left:14px">راسلنا على واتساب</span></div>
</div>""" + FOOTER)

# Post 4: services, light
svc = [("Content creation","صناعة المحتوى"),("Social media management","إدارة حسابات التواصل"),
       ("Online reputation","السمعة الرقمية"),("Websites","المواقع الإلكترونية")]
rows = "".join(f'<div class="svc"><div class="e">{e}</div><div class="a">{a}</div></div>' for e,a in svc)
SLIDES["p4"] = page("light", header() + f"""
<div class="body">
  <div class="en" style="font-size:96px">Your expertise deserves to be seen.</div>
  <div class="ar" style="font-size:56px;margin-top:24px">خبرتك تستحق أن تُرى.</div>
  <div style="margin-top:56px">{rows}</div>
  <div style="display:flex;justify-content:space-between;margin-top:30px"><div class="p" style="font-size:26px;margin:0">For doctors, clinics and labs.</div><div class="par" style="font-size:26px;margin:0">للأطباء والعيادات والمخابر.</div></div>
</div>""" + FOOTER)

# AMDB social media playbook

Brand: Aloui Med Digital Bridge (AMDB), a digital agency for doctors, clinics and labs.
Founder & CEO: Dr. Aloui Ghanem. Contact on every post: amdb.agency@yahoo.com · WhatsApp Business +216 93 871 805 (since 16 Nov 2026; the old +216 94 871 811 is retired) · @amdb_agency.

## Accounts (Metricool brand id 7924395, timezone Africa/Tunis)
Instagram @amdb_agency, Facebook page, LinkedIn company account "Aloui Med Digital Bridge".

## Weekly rhythm
4 publications per week, each scheduled on Instagram, Facebook and LinkedIn as three separate Metricool posts with platform-specific text:
- 1 single image (1080x1350)
- 1 carousel (5 slides; on LinkedIn as one PDF document with documentTitle)
- 1 reel (1080x1920, ~30-40 s, Arabic voice-over, Instagram REEL with isAiGenerated true, Facebook REEL, LinkedIn video)
- 1 single image
Best times from Metricool data: Instagram/Facebook 10:00 on weekdays (Friday 10:00 strongest), 18:00 for reels (Tue-Thu); LinkedIn peaks at 11:00 (Thu/Fri strongest), so LinkedIn posts go at 11:00 rather than the Instagram time.

## Languages and voice
- Official languages: Arabic and English. Instagram: English then Arabic, separated by a line with a single ".", 6-8 hashtags. Facebook: Arabic first, short English summary, 2 hashtags. LinkedIn: English, longer and professional, company voice ("we"), 3 hashtags.
- No prices in posts. CTA: message us on WhatsApp.
- Never write testimonials, case studies, client results, discounts, partnerships or medical/legal claims without asking the user first.
- No AI-sounding copy: no "it's not X, it's Y", no em dashes, no emoji bullets, no engagement bait, no invented statistics or invented anecdotes.
- Audience priority: dermatologists (aesthetic/laser/hair), aesthetic doctors, plastic surgeons, small aesthetic clinics; Gulf + Arabic-speaking + Tunisia.

## Design system (lux.py)
- Palette: ink #06182E, navy #0B2A55, logo cyan #1FB6D3 (#0E7FA0 on light), pearl #EEF3F6, silver #9FB0C2.
- Type: Cormorant Garamond 500 (English headlines), Noto Naskh Arabic 600/700 (Arabic headlines), Manrope (small English), IBM Plex Sans Arabic (small Arabic). Install with: cd fonts && npm i @fontsource/cormorant-garamond @fontsource/noto-naskh-arabic @fontsource/ibm-plex-sans-arabic @fontsource/manrope (lux.py expects them at /home/claude/amdb/fonts/node_modules).
- Every post: round logo + name header, centred headline EN then AR, footer with the three contacts, thin cyan arc above the footer. Alternate dark and light slides. No all-caps labels, no single-word colour accents.
- Usage: python3 lux.py week1.py outdir (week1.py is the example spec). Check every render visually before scheduling; avoid Arabic lines that leave one orphan word.

## Reel (toolkit/reel)
- reel.html is a time-driven page (setTime(t)); render_reel.py renders stills for checking, then scene files, then concat. music.py makes a soft pad bed.
- Voice: Speko audio.synthesize, ElevenLabs voice Ywuz3KyW2N5pqKNpwcCL, model eleven_v3_conversational, language ar, Modern Standard Arabic with diacritics on ambiguous words. Synthesize the whole script in one call, then transcribe it back twice (audio.transcribe, word_timestamps) and re-generate if a word is wrong. Brand name spoken as "ألوي ميد ديجيتال بريدج". Captions word-synced from the timestamps.
- Mix: voice loudnorm -15 LUFS, music -30 LUFS, generated SFX (rayen-reel-editor make_sfx.py: pop, tick, whoosh, typing, ping) at about 0.5 gain on each reveal.
- ElevenLabs connector (creative_generate_speech, eleven_v3, same voice) works with the user's credits, but its file host (elevenlabsusercontent.com) is blocked by the cloud sandbox egress, so the audio cannot be downloaded there. Use it only where that host is reachable.
- Fallback when ElevenLabs is blocked (Speko asks for a $5 top-up before ElevenLabs; ElevenLabs free plan can be busy): Speko munsit voice ar-msa-male-2 (Hassan, MSA). It added a vowel before the first word in week 2; check the first 0.5 s on a spectrogram and trim at the stop closure.
- Safe zone: captions bottom edge above y=1440, nothing important in the right 230 px below y=500 (Instagram buttons). Run rayen-reel-editor qc.py on the render and read the safe-zone sheet.
- toolkit/reel2 is the week 2 version (review card scene, step header, typed reply, word-synced captions).

## Hosting media
Push media to github.com/ghanem10/amdb-assets under weekN/, then use https://raw.githubusercontent.com/ghanem10/amdb-assets/main/weekN/<file> as Metricool media URLs (Metricool copies them).

## Design lessons
- Week 1 was text-only on one template; every post looked the same in the grid. From week 2: one drawn object per post that carries the idea (HTML/SVG in the palette, never stock or AI people), one dominant headline, Arabic given equal weight.
- Use text-wrap:balance on Arabic paragraphs and explicit <br> on Arabic headlines to avoid orphan words; check every render at full size.
- Mock UI labels in sentence case (no all-caps), and keep mock content generic and clearly illustrative (no names, no real star ratings presented as genuine).
- Carousel cover: a fanned stack of the interior mock-ups works as the thumbnail; interior slides share one template (number, title EN/AR, mock-up left, description right).

- Week 3: change the composition per post (no shared template). Make the drawn object the hero at 700-900 px, cropped or overlapping a card edge for depth, with a headline column or band around it. Alternate top-heavy and bottom-heavy layouts in the grid.
- Wrap phone numbers inside Arabic text in <span dir="ltr" style="font-family:Man">, otherwise they render reversed in a serif fallback.
- Cormorant digits are old-style by default; use font-variant-numeric:lining-nums for big numbers.
- Keep bio and UI text in mock-ups short enough to fit one line; a wrapped last word reads as an orphan at full size.
- Metricool: check getScheduledPosts for status ERROR after each week. "You have reached your Metricool account limit" stopped the Nov 20-21 posts; scheduling still succeeds, the failure only shows at publish time.

## Week log
- Week 1 (11-14 Nov 2026): first impression post, carousel "three signs", reel "patients search before they book", services post.
- Week 2 (16-21 Nov 2026): Mon Google Maps profile checklist (image), Wed reel "bad review, don't delete it" (reputation), Fri carousel "three posts that build trust before the first visit", Sat bilingual "speak to every patient in their language". Week 1 data: carousel had the most IG views; LinkedIn video had the most impressions (38). Reel voice: munsit Hassan (ElevenLabs unavailable).
- Week 3 (26-28 Nov 2026, approved late so moved from Mon-Fri to Thu-Sat): Thu 10:00 image "Patients write at night. Who replies?" (WhatsApp Business away message), Thu 18:00 reel "Can a new patient book from your bio?" (LinkedIn 13:00 to avoid two LinkedIn posts at 11:00), Fri 10:00 carousel "Three Story Highlights that work like a mini website", Sat 10:00 image "You approve. We publish." Week 2 data: Maps image best on IG (9 views), reels 6-7 views with 50% skip rate, LinkedIn video 38 impressions in week 1. Reel voice: munsit Hassan. Metricool limit not fixed at scheduling time, so these may fail until 1 Dec.

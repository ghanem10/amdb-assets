# AMDB social media playbook

Brand: Aloui Med Digital Bridge (AMDB), a digital agency for doctors, clinics and labs.
Founder & CEO: Dr. Aloui Ghanem. Contact on every post: amdb.agency@yahoo.com · WhatsApp +216 94 871 811 · @amdb_agency.

## Accounts (Metricool brand id 7924395, timezone Africa/Tunis)
Instagram @amdb_agency, Facebook page, LinkedIn company account "Aloui Med Digital Bridge".

## Weekly rhythm
4 publications per week, each scheduled on Instagram, Facebook and LinkedIn as three separate Metricool posts with platform-specific text:
- 1 single image (1080x1350)
- 1 carousel (5 slides; on LinkedIn as one PDF document with documentTitle)
- 1 reel (1080x1920, ~30-40 s, Arabic voice-over, Instagram REEL with isAiGenerated true, Facebook REEL, LinkedIn video)
- 1 single image
Best times from Metricool data: 10:00 on weekdays; 18:00 for reels.

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
- Mix: voice loudnorm -15 LUFS, music -30 LUFS.

## Hosting media
Push media to github.com/ghanem10/amdb-assets under weekN/, then use https://raw.githubusercontent.com/ghanem10/amdb-assets/main/weekN/<file> as Metricool media URLs (Metricool copies them).

## Week log
- Week 1 (11-14 Nov 2026): first impression post, carousel "three signs", reel "patients search before they book", services post.

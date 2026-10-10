import re, json

html = open('episodes.html', encoding='utf-8').read()

# ---- JSON-LD by eid ----
m = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
ld = json.loads(m.group(1))
ld_by_eid = {}
for i, item in enumerate(ld['itemListElement']):
    it = item['item']
    eid = re.search(r'/vi/([A-Za-z0-9_-]+)/?', it['thumbnailUrl'][0]).group(1)
    desc_parts = it['description'].split('\n')
    ld_by_eid[eid] = {
        'pos': i+1, 'name': it['name'],
        'desc_en': desc_parts[0].strip(),
        'desc_hi': desc_parts[1].strip() if len(desc_parts) > 1 else '',
        'date': it['uploadDate'], 'dur': it['duration'],
    }

# ---- Cards by eid ----
blocks = re.split(r'<article class="episode-card', html)
card_by_eid = {}
card_order = []
for b in blocks[1:]:
    eid = re.search(r'img.youtube.com/vi/([A-Za-z0-9_-]+)/0', b)
    if not eid:
        continue
    eid = eid.group(1)
    title_m = re.search(r'<h2 class="episode-title">(.*?)</h2>', b, re.S)
    title = title_m.group(1).strip() if title_m else None
    dm = re.search(r'<p class="episode-desc">(.*?)</p>', b, re.S)
    en = hi = None
    if dm:
        en_spans = re.findall(r'<span lang="en" class="en">(.*?)</span>', dm.group(1), re.S)
        hi_spans = re.findall(r'<span lang="hi" class="hi">(.*?)</span>', dm.group(1), re.S)
        en = en_spans[0].strip() if en_spans else None
        hi = hi_spans[0].strip() if hi_spans else None
    en_has = re.search(r'episode-hashtags-en">(.*?)</div>', b, re.S)
    hi_has = re.search(r'episode-hashtags-hi">(.*?)</div>', b, re.S)
    card_by_eid[eid] = {
        'title': title,
        'desc_en': en, 'desc_hi': hi,
        'en_has': en_has.group(1).strip() if en_has else None,
        'hi_has': hi_has.group(1).strip() if hi_has else None,
        'malformed_en_span': (en is None and hi is None),
    }
    card_order.append(eid)

print("Compare JSON-LD vs card, matched by video ID\n")
for pos, eid in enumerate(card_order, 1):
    c = card_by_eid[eid]
    j = ld_by_eid.get(eid, {})
    print(f"--- HTML pos {pos}  eid {eid[:12]}  LD pos {j.get('pos')}")
    print(f"    CARD  title: {c['title']}")
    print(f"    LD    name:  {j.get('name')}")
    title_match = (c['title'] == j.get('name'))
    print(f"    title == name: {title_match}")
    en_match = (c['desc_en'] == j.get('desc_en'))
    hi_match = (c['desc_hi'] == j.get('desc_hi'))
    print(f"    en desc match: {en_match} | hi desc match: {hi_match}")
    if not en_match or not hi_match or not title_match or c['malformed_en_span']:
        print(f"    !! MISMATCH FOUND")
        print(f"    !! CARD EN: {c['desc_en'][:120]}")
        print(f"    !! LD   EN: {j.get('desc_en')[:120]}")
        print(f"    !! CARD HI: {c['desc_hi'][:120]}")
        print(f"    !! LD   HI: {j.get('desc_hi')[:120]}")
    print(f"    HAS_EN: {c['en_has']}")
    print(f"    HAS_HI: {c['hi_has']}")
    print()

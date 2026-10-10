#!/usr/bin/env python3
"""Fix episode HTML issues: malformed spans, wrong Hindi hashtags, wrong Unicode chars."""
import re

path = '/Users/nirmals/Data/Ashish/Projects/Jagruk Chacha/JagrukChachaWeb/episodes.html'
with open(path, encoding='utf-8') as f:
    html = f.read()

# --- 1. Fix Episode 4 (ATM, dEjQHDmsiHU): missing </span> after English text ---
# The English span is missing its closing tag before the Hindi span starts
# Pattern: <span lang="en" class="en">...<span lang="hi" class="hi">
# Should be: <span lang="en" class="en">...</span><span lang="hi" class="hi">

# Find the malformed block for dEjQHDmsiHU (episode 4 / ATM)
# It's the one where the English text ends and Hindi starts without </span>
pattern = r'(<span lang="en" class="en">.*?)(<span lang="hi" class="hi">)'
# Only fix if there's no </span> in between
def fix_missing_span(m):
    before = m.group(1)
    if '</span>' not in before:
        return before + '</span>' + m.group(2)
    return m.group(0)

html = re.sub(pattern, fix_missing_span, html, flags=re.S)
print("1. Fixed missing </span> for English desc spans")

# --- 2. Fix Hindi hashtags ---
# Map of (episode position in HTML order) -> correct Hindi hashtag string
# HTML order: E13, E12, E11, E10, E9, E8, E7, E6, E5, E4, E3, E2, E1
# (newest first)
hashtag_fixes = {
    1: "#जागरूक_चाचा #शादी_की_प्लेट #कैटरर #रुपया #भारत",  # E13 wedding - fix macrons
    3: "#जागरूक_चाचा #अखबार #मूल्य #रुपया #भारत",        # E11 newspaper - fix Gurmukhi
    4: "#जागरूक_चाचा #एटीएम #मूल्य #रुपया #भारत",        # E10 ATM - fix Armenian + change from water bottle to ATM
    5: "#जागरूक_चाचा #पानी_की_बोतल #मूल्य #रुपया #भारत", # E9 water bottle - fix Armenian
}

# Find all episode-hashtags-hi divs and replace by order
hi_tags = list(re.finditer(r'(episode-hashtags-hi">)(.*?)(</div>)', html, re.S))
for idx, m in enumerate(hi_tags):
    pos = idx + 1
    if pos in hashtag_fixes:
        old = m.group(2).strip()
        new = hashtag_fixes[pos]
        if old != new:
            html = html[:m.start(2)] + new + html[m.end(2):]
            print(f"2. Fixed Hindi hashtags for episode {pos}: '{old}' -> '{new}'")

# --- 3. Fix English hashtags for E4 (ATM) - ensure it has #ATM not #WaterBottle ---
# E4 (position 4 in HTML) English hashtags should be #ATM #Pricing
# Let's verify the English hashtags are correct
en_tags = list(re.finditer(r'(episode-hashtags-en">)(.*?)(</div>)', html, re.S))
for idx, m in enumerate(en_tags):
    pos = idx + 1
    content = m.group(2).strip()
    print(f"   English hashtags E{pos}: {content}")

# --- 4. Verify no other malformed spans ---
blocks = re.findall(r'<p class="episode-desc">.*?</p>', html, re.S)
for i, b in enumerate(blocks, 1):
    n_en = b.count('<span lang="en" class="en">')
    n_hi = b.count('<span lang="hi" class="hi">')
    n_end = b.count('</span>')
    if n_end < n_en + n_hi:
        print(f"!! Episode {i} still has unclosed spans: open={n_en+n_hi}, closed={n_end}")

# Write back
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone! episodes.html updated.")
EOF
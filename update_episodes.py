import re

path = '/Users/nirmals/Data/Ashish/Projects/Jagruk Chacha/JagrukChachaWeb/episodes.html'
with open(path, encoding='utf-8') as f:
    html = f.read()

e13_card = '''<!-- Episode 13 (newest) -->
                            <article class="episode-card animate-on-scroll">
                                <div class="episode-thumbnail">
                                    <picture>
                                        <source srcset="https://img.youtube.com/vi/524Cgswi8LQ/0.jpg 1536w" sizes="(max-width: 768px) 100vw, 600px" type="image/jpeg">
                                        <img src="https://img.youtube.com/vi/524Cgswi8LQ/0.jpg" alt="पाँच सौ की प्लेट... खाना सिर्फ़ सौ पचाव!" width="1536" height="864" loading="lazy" decoding="async">
                                    </picture>
                                    <span class="episode-number">13</span>
                                    <a href="https://youtube.com/shorts/524Cgswi8LQ?utm_source=jagrukchacha-website&utm_medium=episodes&utm_campaign=episode13" target="_blank" rel="noopener" class="episode-play" aria-label="Watch Episode 13">
                                        <div class="episode-play-btn">
                                            <svg viewBox="0 0 24 24" aria-hidden="true">
                                                <path d="M8 5v14l11-7z"/>
                                            </svg>
                                        </div>
                                    </a>
                                </div>
                                <div class="episode-content">
                                    <div class="episode-top">
                                        <span class="episode-tag">
                                            <span lang="en" class="en">Episode 13</span>
                                            <span lang="hi" class="hi">एपिसोड 13</span>
                                        </span>
                                        <span class="episode-duration">
                                            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                                                <path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/>
                                            </svg>
                                            45s
                                        </span>
                                        <span class="episode-views" data-episode="e13" data-stat="views" hidden>
                                            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                                                <path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5 5 2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/>
                                            </svg>
                                            <span class="episode-views-count"></span>
                                        </span>
                                    </div>
                                    <h2 class="episode-title">पाँच सौ की प्लेट... खाना सिर्फ़ सौ पचाव!</h2>
                                    <p class="episode-desc">
                                        <span lang="en" class="en">A ₹500 wedding plate contains only ~₹150 of real food — dal, rice, sabzi, ghee; the rest goes to labor, gas, utensils, transport, and the caterer's profit.</span>
                                        <span lang="hi" class="hi">पाँच सौ की शादी की प्लेट में असली खाना यानि दाल, चावल, सबज़ी, घी — लगभग सौ पचाव रुपये का ही होता है; बाक़ी पैसा मज़दूरी, गैस-बरतन, ढुलाई और कैटरर के मुनाफे में जाता है.</span>
                                    </p>
                                    <div class="episode-hashtags episode-hashtags-en">#JagrukChacha #WeddingEconomics #Catering #RupayeKiKahani #Bharat</div>
                                    <div class="episode-hashtags episode-hashtags-hi">#जागरूक_चāचā #शāदī_कī_प्लेट #कैटरर #रुपयā #भāरत</div>
                                    <div class="episode-meta">
                                        <span class="episode-date">
                                            <span lang="en" class="en">October 9, 2026</span>
                                            <span lang="hi" class="hi">9 अक्टूबर, 2026</span>
                                        </span>
                                    </div>
                                    <div class="episode-platform-links">
                                        <a href="https://youtube.com/shorts/524Cgswi8LQ?utm_source=jagrukchacha-website&utm_medium=episodes" target="_blank" rel="noopener" class="episode-platform-link youtube" aria-label="Watch on YouTube">
                                            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                                                <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                                            </svg>
                                            <span lang="en" class="en">YouTube</span>
                                            <span lang="hi" class="hi">YouTube</span>
                                        </a>
                                        <a href="https://www.instagram.com/reel/DeRuk-oDBCV/?utm_source=jagrukchacha-website&utm_medium=episodes" target="_blank" rel="noopener" class="episode-platform-link instagram" aria-label="Watch on Instagram">
                                            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                                                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-4.92-.058-1.265-.07-1.644.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                                            </svg>
                                            <span lang="en" class="en">Instagram</span>
                                            <span lang="hi" class="hi">Instagram</span>
                                        </a>
                                        <a href="https://www.facebook.com/share/r/19X8FqkEGT/?utm_source=jagrukchacha-website&utm_medium=episodes" target="_blank" rel="noopener" class="episode-platform-link facebook" aria-label="Watch on Facebook">
                                            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                                                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                                            </svg>
                                            <span lang="en" class="en">Facebook</span>
                                            <span lang="hi" class="hi">Facebook</span>
                                        </a>
                                    </div>
                                </div>
                            </article>

'''

anchor = '<!-- Episode 12 (newest) -->'
assert anchor in html, "Episode 12 anchor not found"
html = html.replace(anchor, e13_card + anchor, 1)

# --- 2. Build JSON-LD from episode data ---
jsonld_lines = [
'''    <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Jagruk Chacha — All Episodes",
  "itemListOrder": "https://schema.org/ItemListOrderDescending",
  "numberOfItems": 11,
  "itemListElement": [
'''
]
episodes = [
    ("524Cgswi8LQ", "पाँच सौ की प्लेट... खाना सिर्फ़ सौ पचāस!", "A ₹500 wedding plate contains only ~₹150 of real food — dal, rice, sabzi, ghee; the rest goes to labor, gas, utensils, transport, and the caterer's profit.\nपाँच सौ की शāदī कī प्लेट में असली खाना यānī दाल, चāवल, सबज़ी, घī — लगभग सौ पचāव रुपये कā हī होतā है; बāकī पैसā मज़दूरī, गैस-बरतn, ढुलāī और कैटरr कe मुनāफे में जातā है.", "2026-10-09"),
    ("kl-VvS4t9ho", "200 रुपये की बाल कटāई में नāई कo 50 रुपये हī बचतें हैं?", "A ₹200 haircut puts only ~₹50 in the barber's pocket. With a ~₹12,000/month wage spread over ~260 cuts a month, each cut yields ~₹48 — the rest goes to rent, electricity, and shop costs. Small shops earn ₹10–15K, well-run ones ₹20–25K, and strong ones up to ₹30K a month.\n₹200 कī बाल कटāई में सe सिर्फ़ पचāव रुपये नāई कī जेब में बचतें हैं। बārह हज़āर रुपये महīनe कī तनख़vāh और लगभग 260 कटāई में हर कटāई पर लगभग अड़तāलīस रुपये बचतें हैं — बāकī दूकān किरāयā-बिजलī में जातe हैं। छोटī दूकān ₹10–15 हज़āर, ठीक-ठāक दूकān ₹20–25 हज़āर, अच्छī कमāई वāलī तīस हज़āर तक।", "2026-10-08"),
    ("yiYvIu3rB-4", "5 रुपये कā अखबāर... और lāगत 15 रुपये? कैse?", "A ₹5 newspaper costs ₹15 to produce — paper, ink, printing, distribution and retailer margins all add up.\n₹5 कā अखबāर बनānे में ₹15 लगतe हैं — कāगज़, स्यāहī, छपāई, वितrण और दूकāनदāर कā मārjin सब जोड़तā है।", "2026-10-07"),
    ("n25C01HkCSE", "3075 रुपये में सāre टोल फ्रī?", "The ₹3,075 FASTag Annual Pass works only on National Highways and National Expressways — State Highways, State Expressways and city roads still charge full toll. Over 1 crore passes sold by September 2026.", "2026-10-03"),
    ("I7VTxhPZe6E", "बīस कī golgāppe... pānch कī lāgat!", "₹20 plate of golgappes costs ₹5-6 to make, but restaurants sell them for ₹500. Street vendor earnings: small town ₹600, big city ₹1,100, metro hub ₹3,000/day.", "2026-09-27"),
    ("s054hppNqQw", "बिजलī bīl 0 — सोlār pānal लगānе कā हिसāब", "How your electricity bill becomes zero with PM Surya Ghar Yojana — ₹78,000 subsidy for a 3kW system + ₹17,000 Rajasthan bonus. The math behind free electricity.", "2026-09-25"),
    ("F58WUJiMDfw", "सāu kе ride में ड्रāivar कī जेब में कितnā bचतā है?", "How much does a cab driver actually keep from a ₹100 ride? With the platform's commission now a daily subscription of ~₹67, drivers take home only about ₹40-50 per ride.", "2026-09-23"),
    ("pML6VN7OIEA", "₹5000 कā टīकट — एयरlāin कo कितnā mīlतā है?", "How much does an airline actually keep from a ₹5000 flight ticket? Base fare is roughly ₹3,600, but taxes, fuel, and airport charges make up the rest — only about ₹1,200 goes to the airline itself.", "2026-09-18"),
    ("peCfxJ1HdnI", "₹10 Chai — Chaiwala Earnings?", "How much does a chaiwala actually keep from a ₹10 cup of chai? Milk costs roughly ₹2, sugar ₹1, tea leaves ₹1, and gas plus the cup about ₹0.50 — a total cost of ~₹4.50, leaving ~₹5.50 per cup. But the real money is not in one cup — it is in the ~500 cups sold every day.", "2026-09-12"),
    ("Q6floi3cDLE", "₹300 Ticket — Cinema Owner Earnings?", "How much does a cinema owner actually keep from a ₹300 ticket? Cinema halls share roughly 50% of net ticket revenue with the film distributor. But the real business is F&B — popcorn and cold drinks with ~75% margin.", "2026-09-08"),
    ("43lMkjWerr8", "⛽ Petrol Pump Earning?", "How much does a Petrol Pump Owner actually earn on ₹100? With margins of roughly ₹1-2 per litre, petrol pumps survive on volume — a single pump serves hundreds of vehicles daily. But the real profits come from the shop: lubricants, snacks, chai, and the convenience premium.", "2026-09-05"),
]
for i, (eid, name, desc, date) in enumerate(episodes):
    indent = 2 + i
    jsonld_lines.append("    {")
    jsonld_lines.append("      \"@type\": \"ListItem\",")
    jsonld_lines.append(f"      \"position\": {i+1},")
    jsonld_lines.append("      \"item\": {")
    jsonld_lines.append("        \"@type\": \"VideoObject\",")
    jsonld_lines.append(f"        \"name\": \"{name}\",")
    jsonld_lines.append(f"        \"description\": \"{desc}\",")
    jsonld_lines.append("        \"thumbnailUrl\": [")
    jsonld_lines.append(f"          \"https://img.youtube.com/vi/{eid}/0.jpg\"")
    jsonld_lines.append("        ],")
    jsonld_lines.append(f"        \"uploadDate\": \"{date}\",")
    jsonld_lines.append("        \"duration\": \"PT45S\",")
    jsonld_lines.append(f"        \"contentUrl\": \"https://www.youtube.com/shorts/{eid}\",")
    jsonld_lines.append(f"        \"embedUrl\": \"https://www.youtube.com/embed/{eid}\",")
    jsonld_lines.append("        \"inLanguage\": \"hi\",")
    jsonld_lines.append("        \"publisher\": {")
    jsonld_lines.append("          \"@type\": \"Organization\",")
    jsonld_lines.append("          \"name\": \"Jagruk Chacha\",")
    jsonld_lines.append("          \"url\": \"https://jagrukchacha.com\",")
    jsonld_lines.append("          \"logo\": {")
    jsonld_lines.append("            \"@type\": \"ImageObject\",")
    jsonld_lines.append("            \"url\": \"https://jagrukchacha.com/assets/JC_ProfilePic.webp\"")
    jsonld_lines.append("          }")
    jsonld_lines.append("        }")
    jsonld_lines.append("      }")
    jsonld_lines.append("    },")

jsonld_lines.pop()
jsonld_lines.append("  ]")
jsonld_lines.append("}")
jsonld_lines.append("    </script>")

jsonld_block = "\n".join(jsonld_lines)
start_marker = "<!-- Structured data: the episode catalogue -->\n"
end_marker = "    </script>\n"
start_idx = html.index(start_marker)
end_idx = html.index(end_marker, start_idx) + len(end_marker)
html = html[:start_idx] + jsonld_block + html[end_idx:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("episodes.html updated OK")
print("E13 card inserted:", e13_card in html)
print("JSON-LD e13 present:", '"524Cgswi8LQ"' in html)
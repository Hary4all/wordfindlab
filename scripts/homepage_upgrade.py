#!/usr/bin/env python3
"""One-shot homepage upgrade: SVG icons, stats, FAQ + schema.
Idempotent. Run AFTER premium_inject.py. Verifies each anchor."""
import io, sys

PATH = "index.html"

NEW_SYMBOLS = '''  <symbol id="icon-gift" viewBox="0 0 24 24">
    <rect x="3" y="8" width="18" height="4" rx="1"/>
    <path d="M12 8v13M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-7"/>
    <path d="M7.5 8a2.5 2.5 0 0 1 0-5C11 3 12 8 12 8s1-5 4.5-5a2.5 2.5 0 0 1 0 5"/>
  </symbol>
  <symbol id="icon-users" viewBox="0 0 24 24">
    <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>
    <circle cx="9" cy="7" r="4"/>
    <path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
  </symbol>
  <symbol id="icon-zap" viewBox="0 0 24 24">
    <path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>
  </symbol>
  <symbol id="icon-calendar" viewBox="0 0 24 24">
    <rect x="3" y="4" width="18" height="18" rx="2"/>
    <path d="M16 2v4M8 2v4M3 10h18"/>
  </symbol>
  <symbol id="icon-printer" viewBox="0 0 24 24">
    <path d="M6 9V3h12v6"/>
    <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/>
    <rect x="6" y="14" width="12" height="8" rx="1"/>
  </symbol>
  <symbol id="icon-cap" viewBox="0 0 24 24">
    <path d="m22 10-10-5L2 10l10 5 10-5z"/>
    <path d="M6 12v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/>
    <path d="M22 10v6"/>
  </symbol>
  <symbol id="icon-paw" viewBox="0 0 24 24">
    <circle cx="7" cy="8" r="2"/>
    <circle cx="12" cy="5.5" r="2"/>
    <circle cx="17" cy="8" r="2"/>
    <path d="M8 15.5c0-2 1.8-4 4-4s4 2 4 4c0 2.2-1.2 4.5-4 4.5s-4-2.3-4-4.5z"/>
  </symbol>
  <symbol id="icon-help" viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="9"/>
    <path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3"/>
    <path d="M12 17h.01"/>
  </symbol>
</svg>'''

STATS = '''    <!-- Site statistics -->
    <section class="pr-stats" aria-label="WordFindLab by the numbers">
      <div class="pr-stat"><span class="num" data-counter="370,000+">370,000+</span><span class="lbl">Dictionary Words</span></div>
      <div class="pr-stat"><span class="num" data-counter="3,800+">3,800+</span><span class="lbl">Word Lists &amp; Guides</span></div>
      <div class="pr-stat"><span class="num" data-counter="15+">15+</span><span class="lbl">Free Word Tools</span></div>
      <div class="pr-stat"><span class="num" data-counter="2.3M+">2.3M+</span><span class="lbl">Words Generated</span></div>
    </section>

    <!-- Trust Section -->'''

FAQ_HTML = '''    <!-- FAQ -->
    <section class="card" style="margin-top:16px" aria-labelledby="home-faq-title">
      <h2 id="home-faq-title">Frequently Asked Questions</h2>
      <div class="faq-item">
        <div class="faq-q">How does the word unscrambler work?</div>
        <p class="faq-a">Enter up to 15 letters and the tool checks every possible combination against a dictionary of 370,000+ English words. Results are grouped by length and sorted by Scrabble score, so the strongest plays appear first. Everything runs in your browser, which is why results appear in milliseconds.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Can I use blank tiles or wildcards?</div>
        <p class="faq-a">Yes. Type <b>?</b> for each blank tile (up to 3). The solver automatically tries all 26 letters in that position and includes every valid word in the results.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Which word games does this work for?</div>
        <p class="faq-a">The same engine covers Scrabble, Words With Friends, Wordscapes, Boggle, Jumble, crosswords, and daily puzzles. For game-specific help, try the dedicated <a href="/scrabble-word-finder/">Scrabble Word Finder</a>, <a href="/wordle-solver/">Wordle Solver</a>, or <a href="/words-with-friends-cheat/">WWF Cheat</a>.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Is WordFindLab really free?</div>
        <p class="faq-a">Yes &mdash; every tool, word list, and game on the site is free with no signup, no trial, and no feature paywall. The site is supported by unobtrusive advertising.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Is using a word finder cheating?</div>
        <p class="faq-a">That depends on how you use it. In casual play most people treat solvers as a learning aid &mdash; a way to discover new words and improve pattern recognition. For rated or competitive games, check your group's rules first. Our <a href="/scrabble-strategy/">strategy guides</a> can help you improve without any assistance.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Why do some results show words I've never seen?</div>
        <p class="faq-a">The full dictionary includes rare and archaic words that are valid in word games. Turn on <b>Meaningful words only</b> to keep everyday vocabulary at the top, or switch the dictionary filter to <b>Common words</b> for a cleaner list.</p>
      </div>
    </section>

'''

SCHEMAS = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "WordFindLab",
  "url": "https://wordfindlab.com/",
  "logo": "https://wordfindlab.com/assets/og/wordfindlab-logo-512.png",
  "sameAs": ["https://www.facebook.com/profile.php?id=61589971622325"]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How does the word unscrambler work?", "acceptedAnswer": {"@type": "Answer", "text": "Enter up to 15 letters and the tool checks every possible combination against a dictionary of 370,000+ English words. Results are grouped by length and sorted by Scrabble score, so the strongest plays appear first. Everything runs in your browser, which is why results appear in milliseconds."}},
    {"@type": "Question", "name": "Can I use blank tiles or wildcards?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Type ? for each blank tile (up to 3). The solver automatically tries all 26 letters in that position and includes every valid word in the results."}},
    {"@type": "Question", "name": "Which word games does this work for?", "acceptedAnswer": {"@type": "Answer", "text": "The same engine covers Scrabble, Words With Friends, Wordscapes, Boggle, Jumble, crosswords, and daily puzzles. Dedicated solvers are available for Scrabble, Wordle, and Words With Friends."}},
    {"@type": "Question", "name": "Is WordFindLab really free?", "acceptedAnswer": {"@type": "Answer", "text": "Yes - every tool, word list, and game on the site is free with no signup, no trial, and no feature paywall. The site is supported by unobtrusive advertising."}},
    {"@type": "Question", "name": "Is using a word finder cheating?", "acceptedAnswer": {"@type": "Answer", "text": "That depends on how you use it. In casual play most people treat solvers as a learning aid - a way to discover new words and improve pattern recognition. For rated or competitive games, check your group's rules first."}},
    {"@type": "Question", "name": "Why do some results show words I've never seen?", "acceptedAnswer": {"@type": "Answer", "text": "The full dictionary includes rare and archaic words that are valid in word games. Turn on Meaningful words only to keep everyday vocabulary at the top, or switch the dictionary filter to Common words for a cleaner list."}}
  ]
}
</script>
<script src="/assets/noindex-query.js?v=20260518"></script>'''

ICON = ('<div class="%s" aria-hidden="true">'
        '<svg viewBox="0 0 24 24"><use href="#%s"></use></svg></div>')

REPLACEMENTS = [
    # (old, new, required)
    ('  </symbol>\n</svg>', '  </symbol>\n' + NEW_SYMBOLS, True),
    ('<div class="game-cta-icon">\U0001f9e9</div>', ICON % ('game-cta-icon', 'icon-puzzle'), True),
    ('<div class="game-cta-icon">\U0001f981</div>', ICON % ('game-cta-icon', 'icon-paw'), True),
    ('<div class="game-cta-icon">\U0001f4c4</div>', ICON % ('game-cta-icon', 'icon-printer'), True),
    ('<div class="game-cta-icon">\U0001f393</div>', ICON % ('game-cta-icon', 'icon-cap'), True),
    ('<div class="trust-card-icon">\U0001f381</div>', ICON % ('trust-card-icon', 'icon-gift'), True),
    ('<div class="trust-card-icon">\U0001f468‍\U0001f469‍\U0001f467‍\U0001f466</div>', ICON % ('trust-card-icon', 'icon-users'), True),
    ('<div class="trust-card-icon">⚡</div>', ICON % ('trust-card-icon', 'icon-zap'), True),
    ('<div class="trust-card-icon">\U0001f4c5</div>', ICON % ('trust-card-icon', 'icon-calendar'), True),
    ('    <!-- Trust Section -->', STATS, True),
    ('    <section class="card" style="margin-top:16px">\n      <h2>Word Game Learning Blog</h2>',
     FAQ_HTML + '    <section class="card" style="margin-top:16px">\n      <h2>Word Game Learning Blog</h2>', True),
    ('<script src="/assets/noindex-query.js?v=20260518"></script>', SCHEMAS, True),
]


def main():
    html = io.open(PATH, encoding="utf-8", errors="surrogateescape",
                   newline="").read()
    if 'id="home-faq-title"' in html:
        print("already upgraded; nothing to do")
        return
    missing = [old[:60] for old, new, req in REPLACEMENTS
               if req and old not in html]
    if missing:
        print("ABORT - anchors not found:")
        for m in missing:
            print("  %r" % m)
        sys.exit(1)
    for old, new, req in REPLACEMENTS:
        assert html.count(old) == 1, "anchor not unique: %r" % old[:60]
        html = html.replace(old, new, 1)
    with io.open(PATH, "w", encoding="utf-8", errors="surrogateescape",
                 newline="") as fh:
        fh.write(html)
    # verify write completeness
    back = io.open(PATH, encoding="utf-8", errors="surrogateescape",
                   newline="").read()
    ok = back == html and back.rstrip().endswith("</html>")
    print("written=%d verified=%s" % (len(back), ok))
    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()

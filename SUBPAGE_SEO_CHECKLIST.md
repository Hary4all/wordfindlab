# WordFindLab Subpage SEO Checklist

Apply this checklist to **every subpage** on your site (500+ pages). Use a find-and-replace script or template update to apply at scale.

---

## The "Golden 7" — Must Have on Every Page

### 1. Title Tag
**Format:** `[Page Topic] | [Category] | WordFindLab`  
**Max length:** 60 characters (including spaces)

**Examples:**
- `5 Letter Words | Complete List for Wordle & Scrabble | WordFindLab`
- `Anagram Solver | Unscramble Letters Instantly | WordFindLab`
- `Scrabble Word Finder | High-Scoring Words by Letter | WordFindLab`
- `Words Starting with A | Full Dictionary List | WordFindLab`
- `How to Use Blank Tiles in Scrabble | Strategy Guide | WordFindLab`

**Rules:**
- Include the primary keyword near the beginning
- Add a secondary keyword when possible
- Always end with `| WordFindLab` for brand reinforcement
- Never use the same title on two different pages

---

### 2. Meta Description
**Format:** Compelling sentence + call to action  
**Max length:** 155 characters (including spaces)

**Examples:**
- `Find every 5-letter word for Wordle and Scrabble. Browse our complete list, filter by letter, and boost your word game score today.`
- `Unscramble any letters into real words with our free anagram solver. Supports blank tiles and shows Scrabble scores instantly.`
- `Discover words starting with A — from 2 to 15 letters. Perfect for crossword clues, Scrabble racks, and vocabulary building.`

**Rules:**
- Include primary keyword in first 120 characters
- Add a clear benefit or value proposition
- End with a soft CTA ("today", "now", "free")
- Make it unique for every page

---

### 3. Canonical URL
**Format:** `<link rel="canonical" href="https://wordfindlab.com/[page-path]/">`

**Rules:**
- Always use the full URL with trailing slash
- Never canonicalize to a different page (unless intentional consolidation)
- For paginated pages, use `?page=2` as the canonical, not page 1

---

### 4. Robots Meta
**Format:** `<meta name="robots" content="index,follow">`

**Rules:**
- Use `index,follow` for all content pages
- Use `noindex,follow` for thin pages (e.g., very short word lists with <5 words)
- Use `noindex,nofollow` for utility pages (search results, error pages)

---

### 5. Open Graph Tags (Facebook, LinkedIn, WhatsApp, Discord)
```html
<meta property="og:type" content="website">
<meta property="og:site_name" content="WordFindLab">
<meta property="og:title" content="[Same as page title]">
<meta property="og:description" content="[Same as meta description]">
<meta property="og:url" content="https://wordfindlab.com/[page-path]/">
<meta property="og:image" content="https://wordfindlab.com/assets/og/wordfindlab-og-1200x630.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="[Descriptive alt text]">
<meta property="og:locale" content="en_US">
```

**Rules:**
- `og:title` should match the page title (or be slightly shorter)
- `og:description` should match the meta description
- `og:image` should be the same for consistency, or page-specific if you have dynamic images
- `og:image:alt` is mandatory for accessibility

---

### 6. Twitter Card Tags
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@WordFindLab">
<meta name="twitter:title" content="[Same as page title]">
<meta name="twitter:description" content="[Same as meta description]">
<meta name="twitter:image" content="https://wordfindlab.com/assets/og/wordfindlab-og-1200x630.png">
<meta name="twitter:image:alt" content="[Descriptive alt text]">
```

**Rules:**
- `twitter:card` should be `summary_large_image` for best visual impact
- If you ever have a Twitter handle, add `twitter:site` and `twitter:creator`
- Image should be at least 1200x630 for optimal display

---

### 7. H1 Tag
**Format:** One `<h1>` per page, containing the primary keyword

**Examples:**
- `<h1>5 Letter Words — Complete List for Wordle & Scrabble</h1>`
- `<h1>Anagram Solver — Unscramble Any Letters</h1>`
- `<h1>Words Starting with A</h1>`

**Rules:**
- Only ONE h1 per page
- Make it descriptive and keyword-rich
- Don't stuff keywords — keep it natural and readable
- The h1 should be different from the title tag (but related)

---

## Recommended Structured Data by Page Type

### Tool Pages (Scrabble Finder, Wordle Solver, Anagram Solver, etc.)
```json
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "[Tool Name]",
  "description": "[Tool description]",
  "url": "https://wordfindlab.com/[path]/",
  "applicationCategory": "GameApplication",
  "operatingSystem": "Any",
  "isAccessibleForFree": true,
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
  "publisher": { "@type": "Organization", "name": "WordFindLab", "url": "https://wordfindlab.com/" }
}
```

### Blog Posts
```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "[Post Title]",
  "description": "[Meta description]",
  "url": "https://wordfindlab.com/blog/[slug]/",
  "datePublished": "2026-05-20",
  "dateModified": "2026-05-20",
  "author": { "@type": "Organization", "name": "WordFindLab" },
  "publisher": { "@type": "Organization", "name": "WordFindLab", "logo": { "@type": "ImageObject", "url": "https://wordfindlab.com/assets/og/wordfindlab-logo-512.png" } }
}
```

### Category Pages (5-letter words, words starting with A)
```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "[Word 1]", "url": "https://wordfindlab.com/dictionary/[word]" },
    { "@type": "ListItem", "position": 2, "name": "[Word 2]", "url": "https://wordfindlab.com/dictionary/[word]" }
  ]
}
```

### BreadcrumbList (All pages)
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://wordfindlab.com/" },
    { "@type": "ListItem", "position": 2, "name": "[Category]", "item": "https://wordfindlab.com/[category]/" },
    { "@type": "ListItem", "position": 3, "name": "[Page Name]", "item": "https://wordfindlab.com/[page-path]/" }
  ]
}
```

---

## Performance & Accessibility Checklist

### Image Optimization
- [ ] Every image has `width` and `height` attributes (prevents CLS)
- [ ] Every image has a descriptive `alt` attribute
- [ ] Images below the fold have `loading="lazy"`
- [ ] Images above the fold have `loading="eager"` or omit the attribute
- [ ] Hero/important images have `fetchpriority="high"`
- [ ] Images are served in WebP format (or AVIF for newer browsers)
- [ ] Image file sizes are under 200KB each (use Squoosh or TinyPNG)
- [ ] SVG icons are inline or in a sprite sheet (not individual files)

### Link Optimization
- [ ] Every internal link has a descriptive `title` attribute
- [ ] Anchor text is descriptive (not "click here" or "read more")
- [ ] All links use relative paths for internal links (`/page/` not `https://wordfindlab.com/page/`)
- [ ] External links have `rel="noopener noreferrer"` for security
- [ ] External links have `target="_blank"` only when necessary (avoid for accessibility)

### Mobile Optimization
- [ ] Meta viewport is present: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- [ ] Touch targets are at least 44x44px
- [ ] Font size is at least 16px on mobile (prevents iOS zoom on input focus)
- [ ] No horizontal scroll on mobile
- [ ] Images are responsive with `max-width: 100%`

---

## Content SEO Checklist

### Internal Linking
- [ ] Every page links to at least 3-5 related pages
- [ ] Footer contains links to all major tools and categories
- [ ] Related tools section at bottom of every tool page
- [ ] Breadcrumb navigation is visible on every page (not just schema)

### FAQ Sections (Add to top 50 pages)
- [ ] Each FAQ question uses `<h3>` or `<h4>` with `itemprop="name"`
- [ ] Each FAQ answer is wrapped in a `<div>` with `itemprop="acceptedAnswer"`
- [ ] The FAQ section has `itemscope itemtype="https://schema.org/FAQPage"`
- [ ] Questions are based on real search queries (use Google "People Also Ask" for ideas)

### Content Freshness
- [ ] Blog posts have `datePublished` and `dateModified` visible
- [ ] Update top 20 pages monthly with new examples or data
- [ ] Update sitemap `lastmod` dates when content changes
- [ ] Add "Last updated" text to evergreen guides

---

## URL Structure Best Practices

| Good ✅ | Bad ❌ |
|--------|--------|
| `/5-letter-words/` | `/5letterwords/` or `/words/5/` |
| `/words-starting-with/a/` | `/words-starting-with-a/` or `/a-words/` |
| `/scrabble-word-finder/` | `/scrabble/` or `/tool/123/` |
| `/blog/best-wordle-starting-words/` | `/blog/post-456/` or `/blog/?id=456` |
| `/dictionary/example/` | `/dict.php?word=example` |

**Rules:**
- Use hyphens, not underscores
- Keep URLs under 60 characters
- Use lowercase only
- Always end with trailing slash
- No query parameters unless necessary (for search/filters)

---

## Quick Wins for 500+ Pages (Batch Apply)

Use a find-and-replace script or template engine to apply these globally:

1. **Add to `<head>` of every template:**
   - Preconnect hints (fonts, GTM, analytics, ads)
   - Theme color meta
   - Hreflang
   - Open Graph base tags
   - Twitter Card base tags

2. **Add to `<body>` of every template:**
   - Breadcrumb navigation (HTML + Schema)
   - Footer with all tool links
   - "Related Tools" section at bottom
   - "Last updated" timestamp for content pages

3. **Add to every image:**
   - `loading="lazy"` (below fold)
   - `width` and `height` attributes
   - Descriptive `alt` text

4. **Add to every link:**
   - Descriptive `title` attribute
   - `rel="noopener noreferrer"` for external links

---

## Pages That Need the Most Attention (Priority Order)

1. `/` (Homepage) — Already improved ✅
2. `/scrabble-word-finder/` — High traffic, high competition
3. `/wordle-solver/` — Trending keyword
4. `/anagram-solver/` — Core tool
5. `/5-letter-words/` — Wordle traffic driver
6. `/words-starting-with/` — Category hub
7. `/words-ending-with/` — Category hub
8. `/blog/` — Content hub
9. `/guides/` — Authority builder
10. `/2-letter-words/` — Scrabble essential

---

## Testing Your Changes

After applying changes, test with:
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
- [Schema.org Validator](https://validator.schema.org/)

---

*Checklist version: 1.0 | For WordFindLab (wordfindlab.com)*

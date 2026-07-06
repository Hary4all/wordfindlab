# Image Optimization Guide for WordFindLab

## Overview

High-quality, optimized images are critical for SEO, social sharing, and user experience. This guide covers all image types you need and how to create them.

---

## Required Image Assets

### 1. Open Graph (OG) Image — 1200 x 630 px
**Purpose:** Preview when shared on Facebook, LinkedIn, WhatsApp, Discord  
**Format:** PNG (for quality) or WebP (for speed)  
**File size:** Under 200KB  
**Design:** Bold title, brand colors, clear CTA, logo  
**Path:** `/assets/og/wordfindlab-og-1200x630.png`

**Design Specs:**
- Background: Gradient from #1e3a5f to #2563eb (dark blue to brand blue)
- Text: "WordFindLab — Free Word Finder & Anagram Solver" in white, bold
- Subtext: "Scrabble | Wordle | Anagrams | Crosswords" in lighter blue
- Logo: WordFindLab mark in top-right corner
- Decorative: Subtle word tile icons or letter pattern
- Safe zone: Keep text within 60px of all edges (Facebook crops dynamically)

### 2. Twitter Card Image — 1200 x 600 px (or reuse OG image)
**Purpose:** Preview on Twitter/X  
**Format:** PNG or WebP  
**File size:** Under 200KB  
**Path:** `/assets/og/wordfindlab-og-1200x630.png` (reuse OG image)

### 3. Favicon — 32 x 32 px and 16 x 16 px
**Purpose:** Browser tab icon, bookmark icon  
**Format:** PNG (also create .ico for older browsers)  
**Path:**
- `/assets/icons/favicon-32x32.png`
- `/assets/icons/favicon-16x16.png`
- `/favicon.ico` (root level)

**Design Specs:**
- Simple "W" lettermark or a stylized word tile
- Use brand blue (#2563eb) with white letter
- Must be readable at 16x16

### 4. Apple Touch Icon — 192 x 192 px
**Purpose:** iOS home screen icon when user "adds to home screen"  
**Format:** PNG  
**Path:** `/assets/icons/icon-192x192.png`

**Design Specs:**
- Square with rounded corners (iOS adds its own rounding, so use full square)
- Brand blue background with white "W" or logo
- Leave some padding (15% on each side) so the icon doesn't touch the edges

### 5. Android/Chrome Icons (PWA) — Multiple sizes
**Purpose:** Android home screen, Chrome app icon, PWA install prompt  
**Format:** PNG  
**Paths:**
- `/assets/icons/icon-72x72.png`
- `/assets/icons/icon-96x96.png`
- `/assets/icons/icon-128x128.png`
- `/assets/icons/icon-144x144.png`
- `/assets/icons/icon-152x152.png`
- `/assets/icons/icon-192x192.png`
- `/assets/icons/icon-384x384.png`
- `/assets/icons/icon-512x512.png`

**Design Specs:**
- Same design as Apple Touch Icon
- Use `purpose: "maskable any"` in manifest.json (leave safe zone for adaptive icons)
- For maskable: keep important content within 72% of center (Android crops to any shape)

### 6. Logo — 512 x 512 px
**Purpose:** Schema.org Organization logo, rich results  
**Format:** PNG with transparent background  
**Path:** `/assets/og/wordfindlab-logo-512.png`

### 7. Desktop Screenshot — 1280 x 720 px
**Purpose:** PWA install prompt, app store listing  
**Format:** PNG or WebP  
**Path:** `/assets/og/screenshot-desktop.png`

**Design Specs:**
- Screenshot of the actual tool in use (with sample search results)
- Clean, no clutter, good lighting on the interface
- Include the hero section with search bar and results

### 8. Mobile Screenshot — 750 x 1334 px (or 1170 x 2532 for iPhone)
**Purpose:** PWA install prompt, mobile app store listing  
**Format:** PNG or WebP  
**Path:** `/assets/og/screenshot-mobile.png`

---

## Image Optimization Rules

### File Size Targets
| Image Type | Target Size | Max Size |
|-----------|-------------|----------|
| OG Image | 80-150 KB | 200 KB |
| Favicon | 1-5 KB | 10 KB |
| Touch Icon (192x192) | 5-15 KB | 30 KB |
| PWA Icons (512x512) | 15-30 KB | 50 KB |
| Screenshot | 100-200 KB | 300 KB |

### Format Selection
| Use Case | Format | Why |
|----------|--------|-----|
| Logos, icons, graphics | PNG | Sharp edges, transparency |
| Photos, screenshots | WebP | 25-35% smaller than PNG/JPEG |
| Fallback for old browsers | JPEG | Universal compatibility |
| Icons in CSS | SVG | Scalable, tiny file size |

### Responsive Images
```html
<picture>
  <source srcset="/assets/og/wordfindlab-og-1200x630.webp" type="image/webp">
  <img src="/assets/og/wordfindlab-og-1200x630.png" 
       width="1200" height="630" 
       alt="WordFindLab word finder preview"
       loading="lazy"
       decoding="async">
</picture>
```

### Critical Image Attributes
```html
<!-- Hero image (above fold) -->
<img src="hero.png" width="1200" height="630" 
     alt="Descriptive text" 
     fetchpriority="high"
     decoding="sync">

<!-- Content image (below fold) -->
<img src="content.png" width="800" height="400" 
     alt="Descriptive text" 
     loading="lazy"
     decoding="async">
```

---

## How to Generate Images (Tools)

### Option 1: Python Script (Pillow)
Use the provided Python script to generate all icons from a single source image.

### Option 2: Figma (Recommended for Design)
1. Create a 1200x630 frame for OG image
2. Use brand colors, typography, and icons
3. Export at 2x for retina displays
4. Use "Export to PNG" with compression

### Option 3: Canva (Quick & Easy)
1. Search "Facebook Open Graph" template (1200x630)
2. Customize with brand colors and text
3. Export as PNG

### Option 4: Online Tools
- **Squoosh** (squoosh.app) — Compress images, convert to WebP
- **TinyPNG** (tinypng.com) — Batch compress PNG/JPEG
- **Favicon Generator** (favicon.io) — Generate all icon sizes from one image
- **RealFaviconGenerator** (realfavicongenerator.net) — Complete favicon package

---

## Image File Structure

```
/assets/
  /og/
    wordfindlab-og-1200x630.png     (Open Graph / Twitter Card)
    wordfindlab-logo-512.png       (Organization logo for schema)
    screenshot-desktop.png         (PWA desktop screenshot)
    screenshot-mobile.png          (PWA mobile screenshot)
  /icons/
    favicon-16x16.png              (Browser tab icon)
    favicon-32x32.png              (Browser tab icon)
    icon-72x72.png                 (PWA icon)
    icon-96x96.png                 (PWA icon)
    icon-128x128.png               (PWA icon)
    icon-144x144.png               (PWA icon)
    icon-152x152.png               (PWA icon / iOS touch)
    icon-192x192.png               (PWA icon / iOS touch)
    icon-384x384.png               (PWA icon)
    icon-512x512.png               (PWA icon / splash screen)
/favicon.ico                       (Legacy browser fallback)
```

---

## Image SEO Checklist

- [ ] Every image has a descriptive `alt` attribute
- [ ] Every image has `width` and `height` attributes (prevents layout shift)
- [ ] Below-fold images use `loading="lazy"`
- [ ] Above-fold images use `fetchpriority="high"` or `loading="eager"`
- [ ] All images are compressed (under the max size targets)
- [ ] OG image exists and is accessible (test with Facebook Debugger)
- [ ] Twitter Card image exists and is accessible (test with Twitter Validator)
- [ ] Favicon is visible in browser tab
- [ ] PWA icons all render correctly (test with Chrome DevTools > Application > Manifest)
- [ ] No broken image links (use Screaming Frog or similar to crawl)
- [ ] Images are served with proper caching headers (Cache-Control: public, max-age=31536000)

---

## Common Mistakes to Avoid

❌ **Using stock photos without context** — Use relevant, branded visuals  
❌ **Forgetting `alt` text** — Screen readers and image search need this  
❌ **Oversized images** — A 4MB hero image kills your PageSpeed score  
❌ **Missing dimensions** — Causes CLS (Cumulative Layout Shift) penalties  
❌ **Using JPEG for logos/icons** — PNG or SVG preserves sharp edges  
❌ **No OG image** — Social shares will look broken or unprofessional  
❌ **Text in images without equivalent** — Always include text in HTML too  

---

*Guide version: 1.0 | For WordFindLab (wordfindlab.com)*

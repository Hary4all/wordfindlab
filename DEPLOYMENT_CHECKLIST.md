# WordFindLab SEO Deployment Checklist

## Critical Issue: "Previews Unavailable"

This error means Facebook/Twitter/LinkedIn can't fetch your OG image. Here's how to fix it.

---

## Step 1: Upload ALL New Files to Your Live Server

These files MUST be on your live server at the exact paths shown:

### Required Files (Upload These)

| Local File | Must Be At This URL | Status |
|-----------|---------------------|--------|
| `assets/og/wordfindlab-og-1200x630.png` | `https://wordfindlab.com/assets/og/wordfindlab-og-1200x630.png` | ⬜ |
| `assets/og/wordfindlab-logo-512.png` | `https://wordfindlab.com/assets/og/wordfindlab-logo-512.png` | ⬜ |
| `assets/icons/icon-192x192.png` | `https://wordfindlab.com/assets/icons/icon-192x192.png` | ⬜ |
| `assets/icons/favicon-32x32.png` | `https://wordfindlab.com/assets/icons/favicon-32x32.png` | ⬜ |
| `assets/icons/favicon-16x16.png` | `https://wordfindlab.com/assets/icons/favicon-16x16.png` | ⬜ |
| `assets/enhancements.css` | `https://wordfindlab.com/assets/enhancements.css` | ⬜ |
| `manifest.json` | `https://wordfindlab.com/manifest.json` | ⬜ |
| `favicon.ico` | `https://wordfindlab.com/favicon.ico` | ⬜ |

### How to Verify Upload

Open these URLs in your browser. If you see a 404 error, the file isn't uploaded yet:

```
https://wordfindlab.com/assets/og/wordfindlab-og-1200x630.png
https://wordfindlab.com/assets/enhancements.css
https://wordfindlab.com/manifest.json
```

**If any URL returns 404, the social preview WILL NOT WORK.**

---

## Step 2: Deploy the Improved Homepage (Optional but Recommended)

Your original `index.html` is unchanged. The improved version is `index-improved.html`.

To deploy:
```bash
# Rename to replace the original
mv index-improved.html index.html
mv 404-improved.html 404.html
```

**What's better in the new homepage:**
- All new SEO tags in the correct order
- Better title tag with more keywords
- Better meta description
- FAQ Schema + Breadcrumb Schema + Organization Schema
- All scripts at bottom of page (faster loading)
- Enhancement CSS loaded for animations

---

## Step 3: Clear Social Media Cache (CRITICAL)

Even after uploading, Facebook and Twitter cache the old version. You MUST clear their cache.

### Facebook
1. Go to: https://developers.facebook.com/tools/debug/
2. Enter your URL: `https://wordfindlab.com/`
3. Click **"Debug"**
4. Scroll down to **"Link Preview"**
5. If it says "Previews unavailable" or shows old image, click **"Scrape Again"**
6. Repeat for these important pages:
   - `https://wordfindlab.com/`
   - `https://wordfindlab.com/scrabble-word-finder/`
   - `https://wordfindlab.com/wordle-solver/`
   - `https://wordfindlab.com/anagram-solver/`
   - `https://wordfindlab.com/5-letter-words/`

### Twitter/X
1. Go to: https://cards-dev.twitter.com/validator
2. Enter your URL: `https://wordfindlab.com/`
3. Click **"Preview Card"**
4. Check if the large image card shows correctly

### LinkedIn
1. Go to: https://www.linkedin.com/post-inspector/
2. Enter your URL
3. Check the preview

---

## Step 4: Test Your Pages

Use these free tools to verify everything is working:

| Tool | URL | What to Check |
|------|-----|---------------|
| Facebook Debugger | https://developers.facebook.com/tools/debug/ | OG image shows, no errors |
| Twitter Card Validator | https://cards-dev.twitter.com/validator | Large image card shows |
| LinkedIn Inspector | https://www.linkedin.com/post-inspector/ | Preview image shows |
| Google Rich Results | https://search.google.com/test/rich-results | FAQ + Breadcrumb schema detected |
| Schema Validator | https://validator.schema.org/ | No schema errors |

---

## Common Issues & Fixes

### "The image URL could not be fetched"
**Cause:** The image file isn't on your server at the correct path.
**Fix:** Upload `assets/og/wordfindlab-og-1200x630.png` to your server.

### "The image is too small"
**Cause:** The image is smaller than 200x200 pixels.
**Fix:** Our image is 1200x630, so this shouldn't happen. If it does, check the uploaded image wasn't corrupted.

### "The image URL is not accessible"
**Cause:** The server blocks the social media crawler, or the URL redirects.
**Fix:** Check your `.htaccess` or firewall rules. Make sure the image is publicly accessible without authentication.

### "Previews unavailable" (even after uploading)
**Cause:** Facebook cached the old version before you uploaded the image.
**Fix:** Click "Scrape Again" in the Facebook Debugger. Do this 2-3 times if needed.

### "The image is not in a supported format"
**Cause:** The image is not PNG, JPEG, or GIF.
**Fix:** Our image is PNG, which is supported. Make sure it wasn't converted to another format during upload.

### Image shows but looks wrong
**Cause:** Facebook crops the image differently.
**Fix:** Our image is 1200x630 which is the recommended size. Facebook may crop to 1.91:1 (1200x628) for link previews. The image is designed to look good even when cropped.

---

## Quick Verification Commands

If you have access to your server, run these to verify:

```bash
# Check if the image is accessible
curl -I https://wordfindlab.com/assets/og/wordfindlab-og-1200x630.png
# Should return HTTP 200 OK

# Check the image size
curl -s https://wordfindlab.com/assets/og/wordfindlab-og-1200x630.png | wc -c
# Should be around 57,000 bytes

# Check if the OG tags are present
curl -s https://wordfindlab.com/ | grep -i "og:image"
# Should show the image URL
```

---

## Post-Deployment Checklist

After deploying, verify all these items:

- [ ] `https://wordfindlab.com/assets/og/wordfindlab-og-1200x630.png` loads in browser (no 404)
- [ ] `https://wordfindlab.com/assets/enhancements.css` loads in browser (no 404)
- [ ] `https://wordfindlab.com/manifest.json` loads in browser (no 404)
- [ ] Facebook Debugger shows the image for `https://wordfindlab.com/`
- [ ] Twitter Card Validator shows large image card for `https://wordfindlab.com/`
- [ ] Google Rich Results Test detects FAQPage schema on homepage
- [ ] Google Rich Results Test detects BreadcrumbList schema on subpages
- [ ] Mobile browser shows blue theme color in address bar
- [ ] Favicon shows in browser tab

---

## Expected Results After Deployment

| Metric | Before | After |
|--------|--------|-------|
| Facebook share preview | Broken / missing | Rich image card with logo + text |
| Twitter share preview | Plain text | Large image card |
| LinkedIn share preview | Missing | Image + title + description |
| WhatsApp share preview | Missing | Image + title |
| Discord share preview | Missing | Rich embed |
| Google rich results | None | FAQ + Breadcrumb snippets |

---

## Files Summary

All new files are in your workspace: `D:\unscrambler\unscrambler Site\`

| File | Type | Must Upload? |
|------|------|-------------|
| `assets/og/wordfindlab-og-1200x630.png` | OG Image | ✅ YES - Critical |
| `assets/og/wordfindlab-logo-512.png` | Logo | ✅ YES - For schema |
| `assets/og/screenshot-desktop.png` | PWA Screenshot | ⬜ Optional |
| `assets/og/screenshot-mobile.png` | PWA Screenshot | ⬜ Optional |
| `assets/icons/*` | App Icons | ✅ YES - For PWA |
| `assets/enhancements.css` | Stylesheet | ✅ YES - For animations |
| `manifest.json` | PWA Manifest | ✅ YES - For PWA |
| `favicon.ico` | Favicon | ✅ YES - For browser tab |
| `index-improved.html` | Homepage | ✅ YES - Recommended |
| `404-improved.html` | 404 Page | ✅ YES - Recommended |

---

*Last updated: 2026-06-19*

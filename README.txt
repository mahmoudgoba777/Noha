# NNC Bilingual Contact Page

A responsive, bilingual Arabic-English professional contact page for Noha El Barkouky.

## Files
- `index.html` — profile page
- `styles.css` — styling
- `assets/nnc-logo.png` — supplied company logo
- `contact.vcf` — downloadable contact card

## Publish free with GitHub Pages
1. Sign in or create an account at https://github.com/.
2. Create a new **public** repository, for example `nnc-noha-contact`.
3. Upload all files and folders from this package. Keep `index.html` at the repository root.
4. Open **Settings → Pages**.
5. Under **Build and deployment**, choose **Deploy from a branch**.
6. Select branch `main` and folder `/(root)`, then click **Save**.
7. Wait for GitHub Pages to publish the page. Your URL will look like:
   `https://YOUR-USERNAME.github.io/nnc-noha-contact/`
8. Open the published URL on your phone and test every phone, email, website, and Save Contact button.

## Create a stable QR code
After the site is live, replace `YOUR-USERNAME` in `make_qr.py` with your actual GitHub username and run:
`python make_qr.py`
It creates `NNC_Noha_Website_QR.png`.

**Important:** The QR included in this package is a setup QR and does not yet point to a live site, because the final GitHub Pages URL is not known until you publish. Once the page is published, generate the final QR using the exact live URL. Keep the repository name and GitHub username unchanged to keep the URL stable. GitHub Pages hosting is free for public repositories, but the service is not an eternal guarantee.

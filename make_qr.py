import qrcode

# Replace YOUR-USERNAME with your GitHub username after publishing.
site_url = "https://YOUR-USERNAME.github.io/nnc-noha-contact/"
img = qrcode.make(site_url)
img.save("NNC_Noha_Website_QR.png")
print("Created NNC_Noha_Website_QR.png for:", site_url)

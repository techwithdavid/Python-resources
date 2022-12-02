# Installing required libraries
import png
import pyqrcode
# pip install pyqrcode
# pip install pypng

# Importing the libraries

# Link Which represents the QR Code.
link = "https://neighbordevcr.com/"

# Generating QR Code.
url = pyqrcode.create(link)

# Creating and Saving the file as SVG.
url.svg("web.svg", scale=10)

# Creating and Saving the file as PNG.
url.png("web.png", scale=12)

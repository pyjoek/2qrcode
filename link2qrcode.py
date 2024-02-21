import qrcode

# Create a QRCode instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Data to encode
data = "https://google.com"

# Add data to the QRCode instance
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QRCode instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")

# Optionally, display the image
img.show()

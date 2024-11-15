import qrcode

# Define the URL to encode
url = "https://www.youtube.com/@TheZerxsis"

# Create a QR code from the URL
img = qrcode.make(url)

# Save the QR code image
img.save("Youtube_Channel.jpg")

print("QR code generated and saved as 'Youtube_Channel.jpg'")
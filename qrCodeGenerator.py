import qrcode

# Generate a QR code
server_url = "http://127.0.0.1:5000/scan"  # Replace with your actual server URL
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add server URL
qr.add_data(server_url)
qr.make(fit=True)

# Save QR code as an image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
print("QR Code generated and saved as 'qr_code.png'.")


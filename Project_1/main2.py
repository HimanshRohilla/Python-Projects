import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 4)

data = qr.add_data("https://www.youtube.com/@TheZerxsis")

qr.make(fit = True)
img=qr.make_image(fill_color = "red",back_color = "blue" )
img.save("Youtube_Channel.png")

print("QR code generated and saved as 'Youtube_Channel.jpg'")
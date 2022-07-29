import qrcode

data = input('What text or URL do you want to make a QR code from?: ')
fileName = input('What name do you want to give your QR code?: ')
#img = qrcode.make(data)

qr = qrcode.QRCode(version=1, box_size=50, border=10)
qr.add_data(data)
qr.
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

#Give path where to save QR code and add name of QRcode at the end
img.save(f'C:/Users/chris/PycharmProjects/Optimizers/QRCodeGenerator/{fileName}.png')

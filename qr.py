'''import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=btIQvYcLNoI")
img.save("qr.png")'''


import qrcode  #buat qr
from PIL import Image #import image dari pillow untuk manipulasi gambar

qr = qrcode.QRCode(version = 1,
                    error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size = 10, border = 4,)     #version = 1 : nentuin ukuran qr, version 1 paling kecil
                                                    #error_conrrection = nentuin tingkat koreksi kesalahan
                                                    #box_size = ukuran tiap kotak kecil qr
                                                    #border 4 = lebar border di sekitar code qr dalam jumlah kotak
qr.add_data("https://youtu.be/uoLIQSUxlMU?si=GEDKiploumjbFwZD") #isi qr
qr.make(fit=True) #ngehasilin matriks sesuai sama yang ditambahin
img = qr.make_image(fill_color="pink", back_color="blue") #atur warna, fill = depan back = belakang
img.save("baru.png") #save gambar
#Build a QRCode Scanner using Python -->Linkedin URl
#pyqrcode,png
#pip install pyqrcode
#pip install pypng
import pyqrcode
import png
#create a QRcode by giving a link
link = "https://www.linkedin.com/in/jahnavi-devi-078999289/"
qr = pyqrcode.create(link)
print(qr)
qr.png("myqr.png",scale=10)

# song qr generation

import segno

song = input("Enter song name: ")
url = input("Enter Spotify song URL: ")

qr = segno.make(url)

filename = song + "_spotify_qr.png"

qr.save(filename, scale=10)

print("Song:", song)
print("QR code saved as:", filename)

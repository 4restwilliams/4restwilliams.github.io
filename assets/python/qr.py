import qrcode
# example data
data = 'https://forrestfwilliams.github.io/2020-11-22-GSNZ'
# output file name
filename = 'gsnz_2020.png'
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)
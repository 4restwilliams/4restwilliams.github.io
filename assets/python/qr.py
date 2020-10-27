import qrcode
# example data
data = 'https://forrestfwilliams.github.io/2020-10-26-thomson-award'
# output file name
filename = 'thomson_award_2020.png'
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)
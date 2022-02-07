from PIL import Image
o=Image.open('google.png')
convert=o.convert('L')
convert.show()

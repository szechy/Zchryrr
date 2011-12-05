import Image
import ImageFont, ImageDraw, ImageOps
font = ImageFont.truetype('/home/zachorr/Impact.ttf', 25, encoding="armn")
im = Image.open("image.jpg")
draw = ImageDraw.Draw(im)
draw.text((5, 50), "WRITE ON ALL THE CATS!", font=font)
im.show()
im.save('my_image.png')
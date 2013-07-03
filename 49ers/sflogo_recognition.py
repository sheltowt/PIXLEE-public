from SimpleCV import Image

template = Image('transformed_logo.jpg')

img = Image('transformed_wallpaper.jpg')

match = img.findKeypointMatch(template)

match.draw(width=3)

print(3)

img.show() 

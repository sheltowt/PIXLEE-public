#convert to grayscale and PCA analysis
from PIL import Image
from pylab import *

# read image to array
im = Image.open('49ers.jpg').convert('L')


# create a new figure
figure()


gray()

# show contours with origin upper left corner
contour(im, origin='image')

axis('equal')
axis('off')

show()


im.save('transformed_wallpaper.jpg')

from PIL import Image
from matplotlib.pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io, color, filters

img  = Image.open('02_h.jpg')
gray = img.convert('L')
R,G,B = img.split()
fig = figure();
fig.add_subplot(2,2,1);
imshow(img);

fig.add_subplot(2,2,2);
imshow(R);
#show()
fig.add_subplot(2,2,3);
imshow(G);
#show()
fig.add_subplot(2,2,4);
imshow(B)
#show()
## Cropping
box = (800,800,2000,2000)
region = img.crop(box)
imshow(region)
show()

#rgb = io.imread('02_h.jpg', as_gray=True)
#rgb = misc.imread('02_h.jpg',mode = "L")
#gray =  rgb2gray(rgb)
#gray = cv2.cvtColor(rgb, cv2.COLORBGR2GRAY)
#rgb = imread('02_h.jpg')

#imshow(rgb)

#im_array = array(Image.open('02_h.jpg').convert('LA'))
#figure()
#gray()
#contour(im_array, origin='image')
#axis('equal')
#axis('off')
#print(im_array)
#imshow(im_array)
#imshow(gray);


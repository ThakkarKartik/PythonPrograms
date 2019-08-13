from skimage import color, io, filters
import skimage
img = io.imread('02_h.jpg')
io.imshow(img)
io.show()

gray = rgb2gray(img)
io.imshow(gray)
io.show()

sobel = filters.sobel(gray)
io.imshow(sobel)
#io.show()

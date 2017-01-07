import Image
import numpy as np

class Drawer():
	"""
	Used for executing any draw functionality
	"""

	def recurse(
			x, 
			y, 
			radius,
			r, 
			g, 
			b):

			"""
			Used to draw the circle around the current position (emulates brush strokes)
			Draws the circle through the use of recursion

			:param x: x coordinate of the current position
			:param y: y coordinate of the current position
			:param radius: radius of the circle to be drawn
			:param r: matrix of r values
			:param g: matrix of g values
			:param b: matrix of b values
			"""

		
		if (radius == 0):

			return
		
		else:

			r[x][y] = 0
			g[x][y] = 0
			b[x][y] = 0

			recurse(x+1, y, radius-1 , r , g, b)
			recurse(x-1, y, radius-1 , r , g, b)
			recurse(x, y+1, radius-1 , r , g, b)
			recurse(x, y-1, radius-1 , r , g, b)

	
	def draw(self, x, y, imageArray):
		"""
		Draws the circle around the current position
		
		Will be deprecated
		"""
		

		im = Image.open('snapshot.jpg')

		# In this case, it's a 3-band (red, green, blue) image
		# so we'll unpack the bands into 3 separate 2D arrays.
		r, g, b = np.array(im).T

		# Let's make an alpha (transparency) band based on where blue is < 100

		# Random math... This isn't meant to look good...
		# Keep in mind that these are unsigned 8-bit integers, and will overflow.
		# You may want to convert to floats for some calculations.
		recurse(x,y, 10, r, g, b)
		# Put things back together and save the result...
		im = Image.fromarray(np.dstack([item.T for item in (r,g,b,a)]))

		im.save('output.png')


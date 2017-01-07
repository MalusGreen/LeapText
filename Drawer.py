import Image
import numpy as np

class Drawer():
	"""
	Used for executing any draw functionality
	"""

	def draw(
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

		if (radius == 0) || (1000 < x < 0) || (1000 < y < 0):

			return
		
		else:

			r[x][y] = 0
			g[x][y] = 0
			b[x][y] = 0

			draw(x+1, y, radius-1 , r , g, b)
			draw(x-1, y, radius-1 , r , g, b)
			draw(x, y+1, radius-1 , r , g, b)
			draw(x, y-1, radius-1 , r , g, b)

	
	def __init__(
			self, 
			image):
		"""
		Creates a drawer object 

		:Param image: path of the image to be edited 
		"""
		self._image = Image.open(image)
		self._r = []
		self._g = []
		self._b = []

	

	def start(
			self
			):
		"""
		Seperates the stored image into its r,g,b components
		"""	

		# In this case, it's a 3-band (red, green, blue) image
		# so we'll unpack the bands into 3 separate 2D arrays.
		self._r, self._g, self._b = np.array(im).T



	def end(
			self
			):
		"""
		Compiles the seperated r,g,b into an output image

		:return the path to the output image from the updated r,g,b arrays
		"""

		# Put things back together and save the result...
		self.im = Image.fromarray(np.dstack([item.T for item in (self._r,self._g,self._b,)]))

		im.save('output.png')	

		return "output.png"










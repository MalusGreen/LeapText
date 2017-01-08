from PIL import Image, ImageDraw
import numpy as np

class DrawObj():
	"""
	Used for executing any draw functionality
	"""

	def draw(
			self,
			x, 
			y, 
			radius,):

		"""
		Used to draw the circle around the current position (emulates brush strokes)
		Draws the circle through the use of recursion

		:param x: x coordinate of the current position
		:param y: y coordinate of the current position
		:param radius: radius of the circle to be drawn
		"""

		if (radius == 0) or 1000 <= x or x < 0 or 1000 <= y or y < 0:


			return
		
		else:
			
			if(self._lastX == None):
				self._lastX = x;
				self._lastY = y;
				self._undo_stack.append(self._current)
				self._current = []
				
			self._draw.line((self._lastX,self._lastY,x,y),fill=0,width=radius,)
			self._lastX = x;
			self._lastY = y;
			self._current.append([x,y])
	
	def erase(
			self,
			x, 
			y, 
			radius,):

		"""
		Used to draw the circle around the current position (emulates brush strokes)
		Draws the circle through the use of recursion

		:param x: x coordinate of the current position
		:param y: y coordinate of the current position
		:param radius: radius of the circle to be drawn
		"""

		if (radius == 0) or 1000 <= x or x < 0 or 1000 <= y or y < 0:


			return
		
		else:
			if(self._lastX == None):
				self._lastX = x
				self._lastY = y
			self._draw.line((self._lastX,self._lastY,x,y),fill=(255, 255, 255),width=radius)
			self._lastX = x
			self._lastY = y
			



	def undo(self):

		for num in range(0, len(self._current)-2):
			self._draw.line((self._current[num][0],self._current[num][1],self._current[num+1][0],self._current[num+1][1]),fill=(255, 255, 255),width=20)
		
		self._current = self._undo_stack.pop();	

	
	def __init__(
			self,
			image):
		"""
		Creates a drawer object 

		:Param image: path of the image to be edited
		"""
		self._path = image
		self._image = None
		self._lastX =  None
		self._lastY = None
		self._draw = None
		self._r = []
		self._g = []
		self._b = []
		self._current = []
		self._undo_stack = Stack() 
		self.isDrawing = False
	

	def start(
			self
			):
		"""
		Seperates the stored image into its r,g,b components
		"""
		self._image = Image.open(self._path)
		self._draw = ImageDraw.Draw(self._image)
		# In this case, it's a 3-band (red, green, blue) image
		# so we'll unpack the bands into 3 separate 2D arrays.
		self._r, self._g, self._b = np.array(self._image).T
		self.isDrawing = True

	def clear(
			self
			):
		self._image = Image.open(self._path)
		self._draw = ImageDraw.Draw(self._image)

	def end(
			self
			):
		"""
		Compiles the seperated r,g,b into an output image

		:return the path to the output image from the updated r,g,b arrays
		"""

		# Put things back together and save the result...
		#self._image = Image.fromarray(np.dstack([item.T for item in (self._r,self._g,self._b,)]))
		self.isDrawing = False

		self._image.save('output.png')

		return "output.png"



class Stack():
	
	def __init__(self):
		self._container = []
		self._limit = 10
		
	def push(self, elem):
		if (len(self._container) == self._limit):
			self._container = []
			
		self._container.append(elem)
		
	def pop(self):
		if (not self._is_empty()):
			return self._container.pop()
		
	def is_empty(self):
		return len(self._container) == 0




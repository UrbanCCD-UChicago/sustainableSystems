import uuid 

class Geography(object):
	"""A geography represents either a point or a polygon
	has a name value and geog value that are 
	passed as constructors
	"""
	def __init__(self,name,geog,id = uuid.uuid4()):
		self.name = name
		self.geog = geog
		self.id = id
	def __str__(self):
		return "%s,%s" % (self.name, self.geog)



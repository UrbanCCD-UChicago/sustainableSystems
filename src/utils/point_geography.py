from geographies import Geography
from db_connection import get_connection, close_connection 

class PointGeography(Geography):
	"""A class for point geographies"""
	def __init__(self, name,address,city,zip,point):
		Geography.__init__(self,name,point)
		self.address = address
		self.city = city
		self.zip = zip

	def gen_sql():
		return """INSERT INTO point_geographies (name,id,address,city,zip,point) 
		VALUES (%s,%s,%s,%s,%s,%s);""" % \
		(self.name,self.id,self.address,self.city,self.zip,self.geog) 

	def insert():
		conn = db_connection.get_connection()
		cur = conn.cursor()
		cur.execute(self.gen_sql())
		conn.commit()
		close_connection(conn,cur)


	def __str__():
		return "%s is a point at %s with an address of %s,%s,%s" \
		(self.name,self.geog,self.address,self.city,self.zip)


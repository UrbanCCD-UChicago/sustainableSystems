from geographies import Geography
from db_connection import get_connection, close_connection 

class PolygonGeography(Geography):
	"""A class for polygon geographies"""
	def __init__(self, name,polygon):
		Geography.__init__(self,name,polygon)

	def gen_sql():
		return """INSERT INTO polygon_geographies (name,id,address,city,zip,polygon) 
		VALUES (%s,%s,%s);""" % \
		(self.name,self.id,self.geog) 

	def insert():
		conn = db_connection.get_connection()
		cur = conn.cursor()
		cur.execute(self.gen_sql())
		conn.commit()
		close_connection(conn,cur)

	def __str__():
		return "%s is a polygon at bounded by %" \
		(self.name,self.geog)


import psycopg2
import os

def get_connection():
	"""
		Returns a connection to the database, figures if it is production
		or dev based on virtualenv
	"""
	env = os.environ.get('ECODISTRICTS_MODE')
	if env ==  "production":
		print "we don't have production set up yet"
		exit()
	elif env == "vagrant":
		conn = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="localhost")
		return conn
	elif env == None:
		conn = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="22.22.22.22")
		return conn

def close_connection(conn,cur):
	""" 
		Passed the psycopg2 connection to the db and the cursor, 
		will commit the changes and then close the connection.
	"""
	try:
		conn.commit()
	except Exception, e:
		print e
		print "You're changes to the db were not made, please try again"
		pass
	cur.close()
	conn.close()
	return True

if __name__ == '__main__':
	conn = get_connection()
	cur = conn.cursor()
	close_connection(conn,cur)
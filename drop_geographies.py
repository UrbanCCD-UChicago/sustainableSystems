import psycopg2 
from utils.db_connection import get_connection,close_connection

def main():
	"""Creates the main polygon and 
	point geographies tables
	"""
	conn = get_connection()
	cur = conn.cursor()
	statements = [
		"""DROP TABLE IF EXISTS polygon_geographies;""",
		"""DROP TABLE IF EXISTS point_geographies;"""]
	for statement in statements:
		cur.execute(statement)
		conn.commit()
	close_connection(conn,cur)
	
if __name__ == '__main__':
	main()
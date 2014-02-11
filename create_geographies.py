import psycopg2 
from utils.db_connection import get_connection,close_connection

def main():
	"""Creates the main polygon and 
	point geographies tables
	"""
	conn = get_connection()
	cur = conn.cursor()
	statements = [
		"""CREATE TABLE IF NOT EXISTS polygon_geographies(
			name text NOT NULL,
			id uuid PRIMARY KEY NOT NULL,
			polygon geography(POLYGON,4326)
			);""",
		"""CREATE TABLE IF NOT EXISTS point_geographies(
			id uuid PRIMARY KEY NOT NULL,
			address text NOT NULL, 
			city text NOT NULL,
			zip integer NOT NULL,
			point geography(POINT,4326)
			);"""]
	for statement in statements:
		cur.execute(statement)
		conn.commit()
	close_connection(conn,cur)
	
if __name__ == '__main__':
	main()
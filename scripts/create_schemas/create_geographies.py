import psycopg2 
from utils import get_connection

def main():
	conn = get_connection()
	cur = conn.cursor()
	statements = [
		"""CREATE TABLE geographies(gid serial PRIMARY KEY NOT NULL,
			geog geography(POLYGON,4326)
			);""",
		"""CREATE TABLE address_to_point(
			gid serial PRIMARY KEY NOT NULL,
			address text(255) NOT NULL, 
			city text(255) NOT NULL,
			zip integer NOT NULL
			point geography(POINT,4326)
			);"""]
	for statement in statements:
		cur.execute(statement)
		conn.commit()
	close_connection()
	
if __name__ == '__main__':
	main()
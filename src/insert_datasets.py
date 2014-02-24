import boto
from utils.point_geography import PointGeography
from utils.polygon_geography import PolygonGeography 
import pandas as pd 

DATASET_CSV_LIST=["s3://ecodistricts/data_upload/CI.1.c.PublicArtWorks.csv"]

def main():
	for dataset in DATASET_CSV_LIST:
		df = pd.read_csv(dataset)
		print df.head()


if __name__ == '__main__':
	main()
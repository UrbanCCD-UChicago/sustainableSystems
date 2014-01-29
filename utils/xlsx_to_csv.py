 import xlrd
 import csv
 import argparse

 def csv_from_excel(excel,csv):
    wb = xlrd.open_workbook(excel)
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open(csv, 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))
    your_csv_file.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--excel', type=str, required=True,
        help="""
            location of excel file""")
    parser.add_argument('--csv', type=str, required=True,
        help="""
            location output csv file
        """)
    args = parser.parse_args()
    csv_from_excel(args.excel,args.csv)
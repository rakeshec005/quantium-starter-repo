import csv
import glob
import os

def merge_sales_files(data_dir='data', output_path='output.csv'):
    files = sorted(glob.glob(os.path.join(data_dir, 'daily_sales_data_*.csv')))
    with open(output_path, 'w', newline='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(['Sales', 'Date', 'Region'])
        for fp in files:
            with open(fp, newline='') as infile:
                reader = csv.reader(infile)
                for row in reader:
                    if len(row) < 5:
                        continue
                    product_name = row[0].strip()
                    price_str = row[1].strip()
                    quantity = row[2].strip()
                    date = row[3].strip()
                    region = row[4].strip()
                    if product_name == 'pink morsel':
                        try:
                            price = float(price_str.replace('$', '').replace(',', ''))
                            qty = int(quantity)
                        except Exception:
                            continue
                        sales_amount = price * qty
                        writer.writerow([f"{sales_amount:.2f}", date, region])

if __name__ == '__main__':
    merge_sales_files()
    print('Wrote output.csv')
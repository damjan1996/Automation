import mariadb
import pandas as pd
import math
import sys
from datetime import datetime


TAX = 1.19  # Define the tax rate
FILE_PATH = 'item_price_data.xlsx'  # File path to the Excel data file
TABLE_NAME = 'YOUR_TABLE_NAME'  # The name of your table in the database


# Function to log info messages
def log_info(text):
    now = datetime.now()
    line = "\n[" + now.strftime("%d/%m/%Y %H:%M:%S") + "] " + text + "\n"
    print(line)
    with open('log_contao.txt', 'a') as f:
        f.writelines(line)


# Function to read the Excel data file
def read_data():
    data = pd.read_excel(FILE_PATH)
    column_names = ['Art. Nr. \n', 'VK mit MwSt.']
    df = pd.DataFrame(data, columns=column_names)
    values = df[column_names].values.tolist()
    processed_data = []
    for element in values:
        if math.isnan(element[0]) or math.isnan(element[1]):
            continue
        processed_data.append((str(int(element[0])), element[1]))
    return processed_data


data_exel = read_data()
print(data_exel)

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="YOUR_DATABASE_USER",
        password="YOUR_DATABASE_PASSWORD",
        host="YOUR_DATABASE_HOST",
        port=3306,
        database="YOUR_DATABASE_NAME"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


# Function to get data from MariaDB, the table name is specified by TABLE_NAME variable
def get_data_from_mariadb():
    cur = conn.cursor()
    cur.execute(f"SELECT item_number, gross_price, net_price FROM {TABLE_NAME}")
    data = []
    for (item_number, gross_price, net_price) in cur:
        data.append([item_number, gross_price.replace(',', '.'), net_price.replace(',', '.')])
    return data


# Function to update product price in MariaDB, the table name is specified by TABLE_NAME variable
def update_product_price_mariadb(item_number, new_gross):
    new_net = new_gross / TAX
    cur = conn.cursor()
    try:
        cur.execute(f"UPDATE {TABLE_NAME} SET gross_price=?, net_price=? WHERE item_number=?",
                    (new_gross, new_net, item_number))
        conn.commit()
        return True
    except mariadb.Error as e:
        print(f"Error: {e}")
        return False


data_mariadb = get_data_from_mariadb()
print(data_mariadb)

# Process data from Excel and MariaDB
for de in data_exel:
    for dm in data_mariadb:
        if de[0] == dm[0]:
            if de[1] != float(dm[1]):
                log_info('Product with productNumber: ' + de[0] + ' must be updated')
                info2 = 'updated product with productNumber:' + str(de[0]) + ' OLD price:' + str(dm[1]) + ' NEW price:' + str(de[1])
                flag = update_product_price_mariadb(de[0], de[1])
                if flag:
                    log_info("Successfully " + info2)
                else:
                    log_info("Error " + info2)
            else:
                log_info('Price is same for product with productNumber: ' + de[0])

# Close connection
conn.close()

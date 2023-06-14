Title: Python MariaDB Product Price Updater

Description:
This repository contains a Python script developed to automate the process of updating product prices in a MariaDB database.
The script extracts the data from an Excel file and subsequently updates the prices in the database if they differ from those specified in the Excel file.

The script has been designed as follows:

1. read_data:
This function reads data from an Excel file, specifically the product number and corresponding prices.
It cleans and processes the data, returning a list of tuples.

2. get_data_from_mariadb:
This function retrieves the current prices from the MariaDB database.
It connects to the database and executes an SQL query to fetch the required data.

3. update_product_price_mariadb:
This function updates the price of a product in the database.
It executes an SQL update query using the product number and the new gross price.

Main Block:
In the main section of the script, it reads the Excel file, fetches the data from the MariaDB database, and updates the prices if required.

If the new price from the Excel file differs from the current price in the database, it calls update_product_price_mariadb to update the price in the database.
The script logs the progress and errors in a text file for easy tracking of the updating process.

Before running this script, you need to replace placeholders (e.g., YOUR_DATABASE_USER, YOUR_DATABASE_PASSWORD, YOUR_DATABASE_HOST, YOUR_DATABASE_NAME, TABLE_NAME) with your actual MariaDB database details.

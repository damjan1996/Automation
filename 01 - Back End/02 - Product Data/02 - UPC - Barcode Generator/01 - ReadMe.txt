Title: Python EAN13 Barcode Generator

Description:
This repository hosts a Python script that generates an EAN13 barcode image from a given EAN number.
The script utilizes the python-barcode library, which provides comprehensive support for creating barcodes using different barcode symbologies.

Here's a breakdown of the script:

1. create_barcode:
This function takes an EAN number and a filename as arguments.
It generates an EAN13 barcode using the EAN13 class from the barcode module.
The ImageWriter class is used to generate an image file of the barcode.
The barcode image is saved using the provided filename.

2. main:
This function calls the create_barcode function with a predefined EAN number and filename.

To run the script, you need to replace the placeholder EAN number with your actual EAN number and define your desired output filename.
After running the script, the barcode image will be saved in the current directory with the provided filename.

Please ensure you have the python-barcode Python library installed before running this script.

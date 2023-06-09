from barcode import EAN13
from barcode.writer import ImageWriter

def create_barcode(ean: str, filename: str):
    """
    Create a EAN13 barcode image from the provided EAN number
    """
    barcode_final = EAN13(ean, writer=ImageWriter())
    barcode_final.save(filename)

def main():
    """
    Main function to call the create_barcode function
    """
    ean = '5636106845976'  # Replace 'your_EAN_number' with your actual EAN number
    filename = "03 - example_barcode"  # Output file name
    create_barcode(ean, filename)

if __name__ == "__main__":
    main()

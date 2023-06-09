import os
import io
from PIL import Image, ImageOps
from rembg import remove

def process_image(input_image_path, output_image_path):
    """
    Process an individual image: remove background, crop, resize and center
    """

    # Import the image and remove the background
    with open(input_image_path, "rb") as input_image:
        input_image_data = input_image.read()

    # Remove the background from the image
    image_with_transparent_background_data = remove(input_image_data)
    image_with_transparent_background = Image.open(io.BytesIO(image_with_transparent_background_data))

    # Crop the image to remove any extra border around the main object
    image_without_extra_border = image_with_transparent_background.crop(image_with_transparent_background.getbbox())

    # Compute the aspect ratio and new dimensions of the object while maintaining aspect ratio
    aspect_ratio = float(image_without_extra_border.width) / float(image_without_extra_border.height)
    new_height = 800  # 1000 - 100 - 100 (space at the top and bottom)
    new_width = int(new_height * aspect_ratio)

    # Resize the object maintaining the original aspect ratio
    resized_image = image_without_extra_border.resize((new_width, new_height), Image.LANCZOS)

    # Create a new 1000x1000 image with a transparent background
    output_image = Image.new("RGBA", (1000, 1000), (0, 0, 0, 0))

    # Position the object in the center of the new image
    position = (
        (output_image.width - resized_image.width) // 2,
        (output_image.height - resized_image.height) // 2,
    )
    output_image.paste(resized_image, position, resized_image)

    # Save the image with a resolution of 300 DPI
    output_image.save(output_image_path, dpi=(300, 300))

def process_all_images(input_directory, output_directory):
    """
    Process all images in the provided directory
    """

    # Create the output directory if it doesn't exist yet
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # List all files in the input directory
    all_files = os.listdir(input_directory)

    # Filter only image files
    image_extensions = {'.jpg', '.jpeg', '.png'}
    image_files = [file for file in all_files if os.path.splitext(file)[1].lower() in image_extensions]

    # Process each image file
    for image_file in image_files:
        input_image_path = os.path.join(input_directory, image_file)
        output_image_path = os.path.join(output_directory, os.path.splitext(image_file)[0] + '.png')
        process_image(input_image_path, output_image_path)
        print(f"Processed {input_image_path} -> {output_image_path}")


# Example usage
input_directory = "03 - Test Image Directories/test_image_directory"
output_directory = "03 - Test Image Directories/test_image_edited"
process_all_images(input_directory, output_directory)

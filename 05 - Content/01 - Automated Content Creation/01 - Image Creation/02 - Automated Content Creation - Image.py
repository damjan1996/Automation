from PIL import Image, ImageDraw, ImageFont
import datetime
import textwrap

def create_text_image():
    """
    Creates a text image with a timestamp and saves it in the same directory as "example_image"
    """
    # Define the image size
    image_size = (5000, 5000)

    # Define the image resolution
    image_resolution = 300

    # Define the background colors
    background_color = (255, 255, 255)  # white
    chat_box_color = (173, 216, 230)  # light blue

    # Define the text
    text = "Lorem ipsum dolor sit amet. Consectetur adipiscing elit. Sed do eiusmod tempor incididunt."

    # Define the fonts and sizes
    # Replace "your_font.ttf" with the path to your actual font file
    text_font = ImageFont.truetype("Montserrat-Regular.ttf", 100)
    timestamp_font = ImageFont.truetype("Montserrat-Regular.ttf", 75)

    # Define the padding
    padding = 80

    # Create the image and the draw object
    image = Image.new("RGB", image_size, background_color)
    image_info = image.info
    image_info["dpi"] = (image_resolution, image_resolution)
    draw = ImageDraw.Draw(image)

    # Calculate the maximum text area
    max_text_width = image_size[0] - 2 * padding

    # Wrap and split the text according to the maximum text area
    wrapped_text = textwrap.fill(text, width=30, break_long_words=True, break_on_hyphens=False)

    # Calculate the text size
    line_height = 1.5  # Set line height
    line_spacing = int(text_font.size * (line_height - 1))  # Calculate the space between lines
    bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=text_font, spacing=line_spacing)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Define the size of the chat box
    chat_box_width = text_width + 2 * padding
    chat_box_height = text_height + 2 * padding + int(line_spacing * (wrapped_text.count('\n') - 1))

    # Define the position of the chat box
    chat_box_left = (image_size[0] - chat_box_width) / 2
    chat_box_top = ((image_size[1] - chat_box_height) / 2) - 500  # decrease the value by 500
    chat_box_right = chat_box_left + chat_box_width
    chat_box_bottom = chat_box_top + chat_box_height

    # Fill the chat box with color and create rounded corners
    radius = 40
    draw.rounded_rectangle([chat_box_left, chat_box_top, chat_box_right, chat_box_bottom], fill=chat_box_color, radius=radius)

    # Calculate the height of the additional padding at the top and bottom of the text
    extra_padding = (chat_box_height - text_height - int(line_spacing * (wrapped_text.count('\n') - 1))) / 2

    # Define the vertical position of the text with the additional padding
    text_x = chat_box_left + padding
    # Check how many lines of text we have
    num_lines = wrapped_text.count('\n') + 1
    if num_lines == 1:
        text_y = chat_box_top + extra_padding - 40
    else:
        text_y = chat_box_top + extra_padding + 10

    # Write the text
    draw.multiline_text((text_x, text_y), wrapped_text, font=text_font, fill=(0, 0, 0), spacing=line_spacing)

    # Define the current timestamp
    timestamp = datetime.datetime.now().strftime("%H:%M")

    # Calculate the size of the timestamp text
    timestamp_width, timestamp_height = draw.textsize(timestamp, font=timestamp_font)

    # Define the distance between text and timestamp
    timestamp_padding = 50

    # Define the vertical position of the timestamp
    timestamp_y = chat_box_bottom + 15  # decrease the value by 500

    # Define the horizontal position of the timestamp (right-aligned, without additional padding)
    timestamp_x = chat_box_right - timestamp_width

    # Draw the timestamp
    draw.text((timestamp_x, timestamp_y), timestamp, font=timestamp_font, fill=(0, 0, 0), align="center")

    # Save the image
    image.save("03 - example_image.png")

if __name__ == "__main__":
    create_text_image()

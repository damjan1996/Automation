Title: Python Text Image Generator

Description:
The Python Text Image Generator repository contains a single Python script that generates an image with stylized text and a timestamp, using the Python Imaging Library (PIL).
It's a useful tool for creating stylized chat-like images with text and time data for use in applications like social media posts, blog articles, and more.

Key Components of the Script:

1. create_text_image:
This is the primary function that creates the text image.
It starts by defining various properties of the image such as its size, resolution, background color, text content, fonts, and sizes.
It then calculates the maximum width of the text area, wraps and splits the text to fit within this area, and calculates the text size.
Afterward, it creates a "chat box" on the image, which is a rounded rectangle filled with color that contains the text.
The function also calculates the appropriate padding for the text within the chat box.
The function then draws the text within the chat box and creates a timestamp that it also adds to the image.
The timestamp is right-aligned with the chat box and placed below the text.
Finally, the function saves the image to the same directory with the filename "03 - example_image.png".

Please ensure that the font file "Montserrat-Regular.ttf" is present in the same directory as the script, or adjust the script to point to the font's location on your machine.

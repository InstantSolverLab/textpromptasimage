
from PIL import Image, ImageDraw, ImageFont

def text_to_image(input_file_path, output_file_path, font_path=None, font_size=20, image_width=800, padding=20):
    """
    Converts text from a .txt file into an image.

    Args:
        input_file_path (str): The path to the input .txt file.
        output_file_path (str): The path to save the output image file.
        font_path (str, optional): The path to a .ttf or .otf font file. Defaults to the default PIL font.
        font_size (int, optional): The font size. Defaults to 20.
        image_width (int, optional): The width of the output image. Defaults to 800.
        padding (int, optional): The padding around the text. Defaults to 20.
    """
    try:
        with open(input_file_path, 'r', encoding='cp1252') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Set up the font
    try:
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.load_default()
    except IOError:
        print(f"Error: The font file '{font_path}' was not found. Using the default font.")
        font = ImageFont.load_default()

    # Create a dummy image to calculate the required image height
    dummy_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_img)

    # Function to wrap text
    def wrap_text(text, font, max_width):
        lines = []
        words = text.split()
        if not words:
            return lines

        current_line = words[0]
        for word in words[1:]:
            if draw.textbbox((0, 0), current_line + ' ' + word, font=font)[2] <= max_width:
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        return lines

    wrapped_text = wrap_text(text, font, image_width - 2 * padding)

    # Calculate text height
    line_height = font.getbbox('A')[3] - font.getbbox('A')[1]
    text_height = len(wrapped_text) * (line_height + 5) # Adding a small gap between lines

    image_height = text_height + 2 * padding

    # Create the final image with a white background
    img = Image.new('RGB', (image_width, image_height), color = (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Draw the text on the image
    y_text = padding
    for line in wrapped_text:
        d.text((padding, y_text), line, font=font, fill=(0, 0, 0))
        y_text += line_height + 5

    # Save the image
    try:
        img.save(output_file_path)
        print(f"Image successfully created at: {output_file_path}")
    except Exception as e:
        print(f"An error occurred while saving the image: {e}")

if __name__ == '__main__':
    # Create a dummy text file for demonstration
  
    # --- Parameters ---
    input_file = "sample_text.txt"
    output_image = "output_image.png"
    # To use a specific font, provide the path to the .ttf file.
    # For example: font_file = "arial.ttf"
    # If font_file is None, a default font will be used.
    font_file = None
    font_size_param = 24
    image_width_param = 1000
    padding_param = 25

    text_to_image(input_file, output_image, font_path=font_file, font_size=font_size_param, image_width=image_width_param, padding=padding_param)
Here is a complete README file formatted in Markdown, based on the Python script you provided.

-----

# Text File to Image Converter 🎨

A simple Python script to convert the contents of a plain `.txt` file into an image file (e.g., `.png`, `.jpg`), with support for custom fonts, text wrapping, and padding.

This is useful for quickly turning notes, quotes, or code snippets into shareable images.

## ✨ Features

  * **Text Wrapping:** Automatically wraps long lines of text to fit the specified image width.
  * **Custom Fonts:** Use any `.ttf` or `.otf` font file you provide.
  * **Custom Sizing:** Control the final image width, font size, and padding.
  * **Error Handling:** Provides basic error messages for missing files or fonts.
  * **Dependency-Light:** Relies only on the popular **Pillow** (PIL) library.

-----

## 📦 Requirements

  * Python 3.6+
  * Pillow (the Python Imaging Library fork)

-----

## ⚙️ Installation

1.  **Clone the repository:**
    *(Replace `your-username/your-repository-name` with your actual repo path)*

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Install the required library:**

    ```bash
    pip install Pillow
    ```

-----

## 🚀 Usage

There are two main ways to use this script.

### 1\. Run as a Standalone Script

This is the simplest method for quick conversions.

1.  **Create your text file:** Create a file named `sample_text.txt` (or any other name) in the same directory.

2.  **Edit parameters (optional):** Open the Python script (`text_to_image.py`) and modify the parameters in the `if __name__ == '__main__':` block at the bottom of the file.

    ```python
    if __name__ == '__main__':
        # --- Parameters ---
        input_file = "sample_text.txt"
        output_image = "output_image.png"

        # To use a specific font, provide the path to the .ttf file.
        # e.g., font_file = "fonts/Arial.ttf"
        font_file = None
        
        font_size_param = 24
        image_width_param = 1000
        padding_param = 25

        text_to_image(input_file, output_image, font_path=font_file, font_size=font_size_param, image_width=image_width_param, padding=padding_param)
    ```

3.  **Run the script:**

    ```bash
    python text_to_image.py
    ```

This will read `sample_text.txt` and generate an `output_image.png` file in the same directory.

### 2\. Import as a Module

You can also import the `text_to_image` function into your own Python projects.

```python
from text_to_image import text_to_image

# Example of converting a file
text_to_image(
    input_file_path="my_notes.txt",
    output_file_path="notes_image.jpg",
    font_path="fonts/Merriweather-Regular.ttf",
    font_size=30,
    image_width=1200,
    padding=50
)

print("Image created successfully!")
```

-----

## Example Output

After creating a `sample_text.txt` and running the script with the default parameters, you will get an `output_image.png` file.

-----

## 📄 Function Parameters

The `text_to_image()` function accepts the following arguments:

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `input_file_path` | `str` | **Required** | The path to the input `.txt` file. |
| `output_file_path` | `str` | **Required** | The path to save the output image (e.g., `output.png`). |
| `font_path` | `str` | `None` | Path to a `.ttf` or `.otf` font file. If `None`, the default PIL font is used. |
| `font_size` | `int` | `20` | The font size in points. |
| `image_width` | `int` | `800` | The total width of the output image in pixels. |
| `padding` | `int` | `20` | The white space (padding) around the text in pixels. |

-----

## 📜 License

This project is licensed under the MIT License.

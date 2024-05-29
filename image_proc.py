import logging
from PIL import Image
from tkinter import filedialog
import tkinter as tk


def setup_logger(name, log_file, level=logging.DEBUG):
    """Function to set up logging configuration."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler and set level to INFO
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create file handler and set level to DEBUG
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(logging.DEBUG)

    # Create formatters and set format
    console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatters to handlers
    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def get_file_path():
    """Prompt user to select a file and return its path."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(title="Select Image File",
                                           filetypes=(("Image files", "*.jpg;*.png;*.bmp"), ("All files", "*.*")))

    return file_path


if __name__ == '__main__':
    logger = setup_logger('imageproc', 'assign5.log')

    logger.info("Starting image processing...")

    try:
        file_path = get_file_path()
        if not file_path:
            logger.error("No file selected. Exiting.")
            exit()

        im = Image.open(file_path, 'r')
        width, height = im.size

        new_image = Image.new(im.mode, im.size)
        new_pixel_map = new_image.load()

        for x in range(width):
            for y in range(height):
                coordinate = (x, y)
                pixel = im.getpixel(coordinate)
                new_pixel = sum(pixel) // len(pixel)
                new_pixel = tuple([new_pixel] * len(pixel))
                new_pixel_map[x, y] = new_pixel

        im.show()  # Display original input image
        new_image.show()  # Display black and white result
        # new_image.save("new_grayscale.jpg")

        # Example of PIL capabilities
        # rotated_image = new_image.rotate(45, expand=True)
        # rotated_image.show()

        logger.info("Image processing completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

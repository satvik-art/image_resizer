# Image Resizer

This Python script allows you to easily resize a batch of images while maintaining their aspect ratio. Whether you need to prepare images for a presentation, website, or any other purpose, this tool can save you time and effort.

## Requirements
- Python 3.x
- Pillow (PIL) library

## Installation
1. Install Python 3.x: [Python Download](https://www.python.org/downloads/)
2. Install Pillow (PIL): `pip install Pillow`

## Usage
1. Organize your images in a folder (input_folder).
2. Run the script and specify the input folder, output folder, and the target dimensions (width and height) you want for the resized images.

```python
python image_resizer.py
Enter the new width: [your_width]
Enter the new height: [your_height]
```

3. The script will process each image in the input folder, maintaining its aspect ratio, and save the resized images in the output folder.

## Important Notes
- The script supports common image file formats: JPEG, PNG, GIF, and BMP.
- Resized images are saved with the same file name in the output folder.

## Customization
You can further customize the script by adjusting the target dimensions or using different resampling filters (currently set to `Image.LANCZOS`). For more options, refer to the [Pillow documentation](https://pillow.readthedocs.io/en/stable/releasenotes/7.0.0.html#resampling-filters).

## Author
Satvik Jalali

Enjoy effortless image resizing with this simple and effective tool. If you encounter any issues or have suggestions for improvements, feel free to contribute. Happy resizing!

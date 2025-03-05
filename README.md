# WebP to PNG Converter

A simple Python script to convert WebP images to PNG format.

## Requirements

- Python 3.6 or higher
- Required packages:
  - Pillow
  - colorama

To install required packages:
```bash
pip install Pillow colorama
```

## How to Use

1. Place your WebP files in the `input` folder
   - The folder will be created automatically when you run the script
   - If it doesn't exist yet, just run the script once

2. Run the script:
```bash
python webp_converter.py
```

3. Find your converted PNG files in the `output` folder

## Features

- Automatically creates input/output folders
- Converts all WebP files to PNG format
- Shows conversion progress with colored output
- Displays summary of successful/failed conversions
- Maintains original filename (just changes extension to .png)

## Notes

- The script will skip any non-WebP files in the input folder
- If a file fails to convert, an error message will be displayed
- Original WebP files are not modified or deleted

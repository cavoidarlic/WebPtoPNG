import os
from PIL import Image
import sys
from colorama import init, Fore, Style
import time

def convert_webp_to_png():
    """
    Converts all WebP images in the input folder to PNG format
    """
    init()
    

    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(script_dir, 'input')
    output_folder = os.path.join(script_dir, 'output')
    

    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)
    print(f"{Fore.CYAN}[INFO] Using input directory: {input_folder}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[INFO] Using output directory: {output_folder}{Style.RESET_ALL}")
    
    # Get all webp files in the directory
    webp_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.webp')]
    total_files = len(webp_files)
    
    if total_files == 0:
        print(f"{Fore.YELLOW}[WARNING] No WebP files found in input folder. Please place WebP files in the 'input' folder.{Style.RESET_ALL}")
        return
    
    print(f"{Fore.CYAN}[INFO] Found {total_files} WebP files to convert{Style.RESET_ALL}")
    

    success_count = 0
    error_count = 0
    start_time = time.time()
    
    for i, filename in enumerate(webp_files):
        try:

            input_path = os.path.join(input_folder, filename)
            img = Image.open(input_path)
            

            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(output_folder, output_filename)
            

            img.save(output_path, 'PNG')
            success_count += 1
            

            progress = (i + 1) / total_files * 100
            print(f"{Fore.GREEN}[{progress:.1f}%] Converted: {filename} → {output_filename}{Style.RESET_ALL}")
            
        except Exception as e:
            error_count += 1
            print(f"{Fore.RED}[ERROR] Failed to convert {filename}: {str(e)}{Style.RESET_ALL}")
    

    elapsed_time = time.time() - start_time
    print(f"\n{Fore.CYAN}[SUMMARY] Conversion complete in {elapsed_time:.2f} seconds{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[SUCCESS] {success_count} files converted successfully{Style.RESET_ALL}")
    
    if error_count > 0:
        print(f"{Fore.RED}[ERRORS] {error_count} files failed to convert{Style.RESET_ALL}")

if __name__ == "__main__":
    print(f"{Fore.CYAN}===== WebP to PNG Converter ====={Style.RESET_ALL}")
    print(f"{Fore.CYAN}[INFO] Place WebP files in the 'input' folder{Style.RESET_ALL}")
    convert_webp_to_png()
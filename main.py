import os
import shutil
import win32com.client

def install_font(font_path):
    # Use COM objects to install a font by adding its path to the Windows registry
    shell = win32com.client.Dispatch("WScript.Shell")
    # Write font entry to the registry to install the font
    shell.RegWrite("HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts\\" + os.path.basename(font_path), os.path.basename(font_path), "REG_SZ")

def copy_and_install_ttf_to_fonts(src_path, dest_fonts_path):
    # Traverse through source directory and its subdirectories
    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.lower().endswith('.ttf'):
                ttf_file_path = os.path.join(root, file)
                dest_path = os.path.join(dest_fonts_path, file)
                # Copy the TTF file to Windows/fonts directory
                shutil.copy(ttf_file_path, dest_path)
                # Install the copied font
                install_font(dest_path)
                print(f"Installed font {file} from {ttf_file_path}")

def main():
    # Specify source and destination paths
    source_directory = "C:/Users/DELL/OneDrive/Documents/GitHub/target_ttf/typewolf_google_fonts"
    windows_fonts_directory = "C:/Windows/Fonts"

    # Copy and install TTF fonts
    copy_and_install_ttf_to_fonts(source_directory, windows_fonts_directory)

if __name__ == "__main__":
    main()

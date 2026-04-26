import glob
import os
import shutil

user_profile = os.environ["USERPROFILE"]
current_working_directory = os.getcwd()  # مسیر جایی که فایل پایتون باز میشه

source_dir = os.path.join(user_profile, "Pictures")  # مبدا
destination_dir = os.path.join(current_working_directory, "backup")  # مقصد

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
    print(f"Created destination directory: {destination_dir}")


picture_files = glob.glob(os.path.join(source_dir, "**", "*.png"), recursive=True)
picture_files.extend(glob.glob(os.path.join(source_dir, "**", "*.jpg"), recursive=True))

print(f"Found picture files: {picture_files}")

for picture_file_path in picture_files:
    print("Copying file:", picture_file_path)
    try:
        # انتقال اطلاعات از مسیر مبدا به مقصد
        shutil.copy2(picture_file_path, destination_dir)
        print(f"Successfully copied {picture_file_path} to {destination_dir}")
    except FileNotFoundError:
        print(f"Error: File not found at {picture_file_path}")
    except Exception as e:
        print(f"An error occurred while copying {picture_file_path}: {e}")

    print("All specified picture files have been copied (or attempted to copy).")

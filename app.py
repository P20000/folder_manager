import os
import shutil

def sort_files_by_extension(folder_path):
    if not os.path.exists(folder_path):
        print("❌ The given folder does not exist.")
        return

    # List all items in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, ext = os.path.splitext(filename)
        ext = ext[1:].lower() if ext else 'no_extension'

        # Create the target folder
        target_folder = os.path.join(folder_path, ext.upper())
        os.makedirs(target_folder, exist_ok=True)

        # Target path
        target_path = os.path.join(target_folder, filename)

        # Handle duplicate file names
        if os.path.exists(target_path):
            base, extension = os.path.splitext(filename)
            counter = 1
            while os.path.exists(target_path):
                new_filename = f"{base}_{counter}{extension}"
                target_path = os.path.join(target_folder, new_filename)
                counter += 1

        # Move file
        shutil.move(file_path, target_path)
        print(f"✅ Moved: {filename} → {target_folder}")

    print("\n🎯 Sorting complete!")

# Example usage:
if __name__ == "__main__":
    folder = input("Enter the path of the folder to sort: ").strip()
    sort_files_by_extension(folder)

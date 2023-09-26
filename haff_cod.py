import os
import zipfile

zip_name = 'archive.zip'
dir_path = '.'
output_zip_path = 'out/plugins-output.zip'

if not os.path.exists(dir_path):
    print(f"Error: {dir_path} does not exist.")
    exit(1)

os.makedirs(os.path.dirname(output_zip_path), exist_ok=True)

with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, dir_path)
            zipf.write(file_path, arcname=rel_path)

print(f"ZIP archive created at {output_zip_path}")

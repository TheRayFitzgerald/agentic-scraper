import os

OUTPUT_DIR = "output"

def download_openai_file(content, file_name):
    # Ensure the output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Read the file content
    file_data_bytes = content.read()
    
    # Write the file to the output directory
    with open(f"{OUTPUT_DIR}/{file_name}", "wb") as f:
        f.write(file_data_bytes)
        print(f"Downloaded file: {file_name}")




def download_openai_file(content):
    file_data_bytes = content.read()
    # write the content to a file
    with open("file.csv", "w") as f:
        f.write(file_data_bytes.decode("utf-8"))
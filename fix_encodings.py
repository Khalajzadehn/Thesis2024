import os
import chardet

data_files = os.listdir("files")


def detect_encoding(file_path):
    """Try to detect the encoding of the file."""
    with open(f"files/{file_path}", 'rb') as file:
        raw_data = file.read(32)  # read first 32 bytes for guessing
        result = chardet.detect(raw_data)
        return result['encoding']


def convert_to_utf16(file_path, encoding):
    """Read the file with the given encoding and write it back in UTF-16."""
    with open(f"files/{file_path}", 'r', encoding=encoding) as file:
        contents = file.read()
        contents = contents.replace("DFauto (English)", "DFauto__English")
        contents = contents.replace("DFauto (Dutch)", "DFauto__Dutch")

    with open(f"files_converted/{file_path}", 'w', encoding='utf-8') as file:
        file.write(contents)


for file in data_files:
    if file.endswith(".merged.txt"):
        encoding = detect_encoding(file)
        try:
            if encoding:
                convert_to_utf16(file, encoding)
            else:
                print(f"Could not detect encoding for {file}")
        except Exception as e:
            print(file, encoding, str(e))
            convert_to_utf16(file, "utf-8")

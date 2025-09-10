import gzip

file_path = 'supermarket project /victory.gz'  # Replace with your .gz file path

try:
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        content = f.read()
        print(content[:10])
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
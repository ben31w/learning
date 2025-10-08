import hashlib
import webbrowser
import zlib

from html_string import html_string

def hash_html(content: str) -> str:
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def compress_html(content: str) -> bytes:
    return zlib.compress(content.encode('utf-8'))

def decompress_html(blob: bytes) -> str:
    return zlib.decompress(blob).decode('utf-8')


if __name__ == '__main__':
    compressed = compress_html(html_string)
    hashed = hash_html(html_string)
    # print(compressed)
    print()
    print(f"Hash:                     {hashed}")
    print(f"Original string length:   {len(html_string):6}")
    print(f"Compressed string length: {len(compressed):6}")

    print()
    original = decompress_html(compressed)
    # print(original)

    filepath = f'html/decompressed_ben31w_{hashed}.html'
    with open(filepath, 'w') as f:
        f.write(original)

    webbrowser.open(filepath)
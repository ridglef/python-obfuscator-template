import zlib

def transform(src: str):
    compressed_data = zlib.compress(src.encode("utf8"), level=9)
    return f"exec(__import__('zlib').decompress({compressed_data!r}))"

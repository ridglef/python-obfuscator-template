# Python Obfuscator Template
A simple template for making an obfuscator for python \n
It provides very little protection because this is just a template/base
# Features
- Gui
- Integer Xor encryption
- Base64 + Zlib compression
# Sample
Before:
```py
hello = "Amogus"
r = 789786

if __name__ == '__main__':
    print(hello)
    print(r)
```
After:
```py
exec(__import__('base64').b64decode("ZXhlYyhfX2ltcG9ydF9fKCd6bGliJykuZGVjb21wcmVzcyhiJ3hceGRhXHhjYkhceGNkXHhjOVx4YzlXXHhiMFVQd1x4Y2NceGNkTy8tVlx4ZTcqXHgwMnJMXHJNLUxcci0sXHgxNFx4ZTJceDE0TFx4OGRceDhjXHhjZE0sXHhjZE1ceGI4Mlx4ZDNceDE0XHhlMlx4ZTNceGYzXHgxMnNTXHhlM1x4ZTNceDE1bFx4ODFceGVhXHhlM1x4ZTNzXHgxMzNceGYzXHhlMlx4ZTNceGQ1XHhhZFx4YjhceDE0XHg4MFx4YTBceGEwKDNceGFmRCNceDAzZFx4OWEmXHg5MkBceDkxJlx4MDAhZlx4MWJEJykp"))
```

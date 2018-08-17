import hashlib

md5 = hashlib.md5("JJF 1357-1990".encode("utf-8")).hexdigest()

print(md5)
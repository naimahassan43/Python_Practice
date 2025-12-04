# opening and reading files in Python
f = open('config', 'rt')
content = f.read(15)
print(content)
print(f.closed)
f.close()
print(f.closed)


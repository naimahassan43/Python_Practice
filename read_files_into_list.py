# Reading files into a list

# 1. f.read().splitlines()
with open('config') as f:
    content = f.read().splitlines()
    print(content)
print('#' * 50)

# 2. f.readlines()
with open('config') as f:
    content = f.readlines()
    print(content)
print('#' * 50)

# 3. List comprehension with f.readline()
with open('config') as f:
    content = f.readline()
    print(content, end='')
    content = f.readline()
    print(content, end='')
print('#' * 50)

# 4. list(f)
with open('config') as f:
    content = list(f)
    print(content)
print('#' * 50)
# 5. iterating over the file object
with open('config') as f:
    for line in f:
        print(line, end='')
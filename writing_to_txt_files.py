with open('devices.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('This is a sample text file.\n')
    f.write('Writing to text files in Python is easy!\n')

with open('my_file.txt', 'a') as f:
    f.write('Some additional text appended to the file.\n')
    f.write('Some other additional text appended to the file.\n')

with open('my_file.txt', 'r+') as f:
    f.seek(15)
    f.write('100')
    f.write('Line added at the beginning of the file.\n')
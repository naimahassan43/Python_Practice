with open('config') as f:
    content = f.read()
    print(content)
    print(f.closed)
    f.read()




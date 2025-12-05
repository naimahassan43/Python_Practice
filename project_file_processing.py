with open('devices.txt') as f:
    content = f.read().splitlines()
    #print(content)
    devices = list()
    for line in content[1:]:
        #print(line)
        devices.append(line.split(':'))
    print(devices)

    for device in devices:
        print(f'ping {device[1]}')
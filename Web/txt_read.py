import linecache

def read(line):
    file_path = 'ip.txt'
    ip_value = linecache.getline(file_path, line)
    return ip_value.strip('\n')

if __name__ == '__main__':
    print(read(5))
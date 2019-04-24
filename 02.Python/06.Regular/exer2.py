import re 
import sys 

def get_address(port):
    f = open("./1.txt")

    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break 
        if not data:
            return "Not found the port"
        try:
            PORT =  re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue

        if PORT == port:
            pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknown)'
            addr = re.search(pattern,data).group(1)
            return addr

if __name__ == "__main__":
    port = sys.argv[1]
    print(get_address(port))
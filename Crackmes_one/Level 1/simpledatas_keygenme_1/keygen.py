# Crackmes.one
# Crackme:
# Level 1
# https://github.com/JavierYuste/---
import argparse

parser=argparse.ArgumentParser(description="It uses dnstwister or urlcrazy (currently only dnstwister) to find possible phising sites trying to clone the url specified. Then it checks their html similarity to your site's index with SimHash algorithm, created by Moses Charikar. All suggests are welcome!", epilog="Example:python BadDNS.py www.example.com -email MY_EMAIL -passwd MY_PASSWD -dest DESTINATION -p 80.0 -E /root/Desktop/exclusionsfile.txt")
parser.add_argument("name",metavar="name",help="The name you wanna type",type=str)
parser.add_argument("-v","--verbose",help="Verbose",action='store_true')

if __name__ == '__main__':
    args=parser.parse_args()

    # Loop
    var13C = 0
    var29C = 0
    i = 0
    while var29C < len(args.name):
        var13C = var13C + ord(args.name[i:i+1])
        var29C = var29C + 1
        i = i + 1

    print('Valid serials for ' + args.name)
    # First serial = NAME.length + 0x6E + NAME.substr(0,1) + var13C
    print('[+] First solution: ' + str(len(args.name)) + str(int(0x6E)) + str(ord(args.name[:1])) + str(var13C))

    # Second serial = NAME.substr + 0x5F + var13C + NAME.
    print('[+] Second solution: ' + str(ord(args.name[:1])) + str(int(0x5F)) + str(var13C) + str(len(args.name)))

    # Third serial = var13C + 0x55 + NAME.length + NAME.substr
    print('[+] Third solution: ' + str(var13C) + str(int(0x55)) + str(len(args.name)) + str(ord(args.name[:1])))
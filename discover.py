from iptools import IpRange
from iptools.ipv4 import validate_ip
from aastra.check import Aastra_Check

__author__ = 'amucci'


def main():

    admin_username = raw_input("Enter Administrator Username [admin]:")
    admin_password = raw_input("Enter Administrator Password [22222]:")

    while True:
        ip_start = raw_input("Enter IP start:")
        if not ip_start:
            print '\033[1;31mIP Start Required\033[1;m'
        else:
            if validate_ip(ip_start):
                break
            else:
                print '\033[1;31mThis is not a valid IPv4 address\033[1;m'
    while True:
        ip_stop = raw_input("Enter IP stop:")
        if not ip_stop:
            print '\033[1;31mIP Stop Required\033[1;m'
        else:
            if validate_ip(ip_stop):
                break
            else:
                print '\033[1;31mThis is not a valid IPv4 address\033[1;m'


    if not admin_username:
        admin_username = "admin"
    if not admin_password:
        admin_password = "22222"

    #get the ip_start and stop and get a ip range
    r = IpRange(ip_start,ip_stop)
    for ip in r:
        check = Aastra_Check(ip,admin_username,admin_password)
        if check.check():
            check.get_local_file()
        else:
            print "%s Is not an Aastra SIP Device"%ip

if __name__ == "__main__":
    main()
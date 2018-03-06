#!/usr/bin/env python3

import sys
import socket

def usage():
    print('Usage: {} <ip address> <start port> <end port(optional)>')
    sys.exit(0)
def socket_setup(addrng,prtrng):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    for addr in addrng:
        for prt in prtrng:
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                s.connect((addr,prt))
                print('Port open at: ', addr + ' port:', prt)
            except ConnectionRefusedError:
                pass
            
            try:
                s.close()
            except:
                pass


def port_range(st,end='NONE'):
    rng = []
    if end != 'NONE' and (st > end or end > 65535 or st < 0):
        print('Invalid port range')
        usage()
        sys.exit(0)

    if end == 'NONE':
        rng.append(st)
    else:
        for i in range((end + 1) - st):
            rng.append(st + i)

    return rng

if __name__ == '__main__':

    addr_rng = [sys.argv[1]]
    try:
        port = port_range(int(sys.argv[2]), int(sys.argv[3]))

    except:
        print('Invalid port range')
        usage()

    socket_setup(addr_rng, port)


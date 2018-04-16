import pyshark
import argparse
import time

def parse_cap( filename):
    print "Looking for Kerb  data from " + filename




def parse_interface(Interface):
    print "Starting Capture from interface " + Interface
    capture = pyshark.LiveCapture(interface=Interface)
    capture.sniff(timeout=10)
    

    for packet in capture.sniff_continuously():
        print packet






if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f" , dest="filename")

    args = parser.parse_args() 
    
    if args.filename:
        parse_cap(args.filename)

    else:
        parse_interface( "enp2s0")

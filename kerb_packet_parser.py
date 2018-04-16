import pyshark
import argparse
import time

def  parse_packet(packet):
     print packet 

def parse_cap( filename):
    print "File name is "+ filename



def parse_interface(Interface):
    print "Starting Capture from interface " + Interface
    capture = pyshark.LiveCapture(interface=Interface, bpf_filter="Kerberos")
    
    capture.apply_on_packets(parse_packet)




if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f" , dest="filename")

    args = parser.parse_args() 
    
    if args.filename:
        parse_cap(args.filename)

    else:
        parse_interface( "enp2s0")

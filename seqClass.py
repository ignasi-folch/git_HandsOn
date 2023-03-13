#!/usr/bin/env python

#IMporting packages
import sys, re
from argparse import ArgumentParser

#Query inputs from user
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()             #Fix lower-case input
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and re.search('U', args.seq): #if T and U cannot be DNA nor RNA
	print ('The sequence is not DNA nor RNA')
    elif re.search('T', args.seq):        #if T then DNA
        print ('The sequence is DNA')
    elif re.search('U', args.seq):      #if U then RNA
        print ('The sequence is RNA')
    else:				#if input is not made of the DNA and RNA nitrogen bases it is not DNA/RNA
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

if args.motif:                          #motif recognition functionality
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("The motif was located in the sequence.")
    else:
        print("The motif was not located in the sequence.")

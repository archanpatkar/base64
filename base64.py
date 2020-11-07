import sys
import math
from os import read

def readFile(filename):
    return open(filename,"rb").read()

def writeFile(filename,data):
    return open(filename,"wb").write(data)

def itoB(n,bits):
    bn = ""
    for i in range(0,bits):
        bn = "{}".format(n % 2) + bn
        n = math.floor(n/2)
    return bn

def totalBin(data):
    return "".join([itoB(b,8) for b in data])

def chunked(data,n,pad='0'):
    l = len(data)
    chunks = []
    curr = 0
    while curr < l:
        if curr+n > l:
            if pad: chunks.append(data[curr+1:] + pad*(n-(l-curr)))
            break 
        chunks.append(data[curr:curr+n])
        curr += n
    return chunks

def basechars(n):
    if n <= 25: return chr(65 + n)
    elif n <= 51: return chr(97 + (n - 26))
    elif n <= 61: return chr(48 + (n - 52))
    elif n == 62: return 43
    elif n == 63: return 47

def reversebase(n):
    if n == 43: return 62
    elif n == 47: return 63
    elif n >= 48 and n <= 57: return n-48 + 52
    elif n >= 65 and n <= 90: return n-65
    elif n >= 97 and n <= 122: return n-97 + 26

def encode(data):
    if isinstance(data,str): data = data.encode(encoding="ascii")
    return "".join([basechars(int(n,2)) for n in ['00'+b for b in chunked(totalBin(data),6)]])

def decode(data):
    if isinstance(data,str): data = data.encode(encoding="ascii")
    t1 = "".join([b[2:] for b in [itoB(reversebase(n),8) for n in data]])
    return [int(c,2) for c in chunked(t1,8,False)]

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "encode":
        d = sys.argv[2]
        if d == "-s": print(encode(sys.argv[3]))
        else: print(encode(readFile(d)))
    elif mode == "decode":
        d = sys.argv[2]
        if d == "-s": print("".join([chr(n) for n in decode(sys.argv[3])]))
        else: print(decode(readFile(d)))
    else: print("No such operation")
    sys.exit(1)
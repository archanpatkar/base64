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

    # print("ch------------------")
    # print(data)
    # print(len(data))
    # print(curr)
    # print(chunks)
    # print(len(chunks))
    # print("ch------------------")
def chunked(data,n,pad='0'):
    l = len(data)
    chunks = []
    curr = 0
    while curr < l:
        if curr+n > l:
            if pad:
                print("here")
                chunks.append(data[curr+1:] + pad*(n-(l-curr)))
            break 
        temp = data[curr:curr+n]
        chunks.append(temp)
        curr += n
    return chunks

def basechars(n):
    if n <= 25:
        return chr(65 + n)
    elif n <= 51:
        return chr(97 + (n - 26))
    elif n <= 61:
        return chr(48 + (n - 52))
    elif n == 62: return 43
    elif n == 63: return 47

def reversebase(n):
    if n == 43: return 62
    elif n == 47: return 63
    elif n >= 48 and n <= 57: return n-48
    elif n >= 65 and n <= 90: return n-65
    elif n >= 97 and n <= 122: return n-97

def encode(data):
    if isinstance(data,str): data = data.encode(encoding="ascii")
    return "".join([basechars(int(n,2)) for n in ['00' + b for b in chunked(totalBin(data),6)]])

def decode(data):
    if isinstance(data,str): data = data.encode(encoding="ascii")
    # print(data)
    t1 = "".join([b[2:] for b in [itoB(reversebase(n),8) for n in data]])
    print(t1)
    # if len(t1) % 8: t1 = t1[:len(t1)-len(t1) % 8]
    # print(len(t1))
    return [int(c,2) for c in chunked(t1,8,False)]

encoded = encode("ABC")
print(encoded)

decoded = decode(encoded)
print(bytearray(decoded))

encoded = encode(readFile("test.txt"))
print(encoded)

decoded = decode(encoded)
writeFile("decodedtest.txt", bytearray(decoded))
print(decoded)
print("".join([chr(c) for c in decoded]))
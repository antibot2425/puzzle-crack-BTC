import math
from bitcoin import *
from bit import *
from bit.format import bytes_to_wif
import blockcypher
from moneywagon import AddressBalance
import requests
from urllib.request import urlopen
from urllib.request import Request
import satoshi
import re

c2 = int(input("enter the number of BTC addresses to generate ==> "))
print("")
c3 = input("for generation, press  'e' ==> ")
print()
z=int(input('start range -> '))
print()
zx=int(input('stop range -> '))
print("")

#f=922337203685477579

p  = 18446744073709551616
g  = 9223372036854775808
g1 = 10145709240540253389
g2 = 11068046444225730970
g3 = 11990383647911208551
g4 = 12912720851596686132
g5 = 13835058055282163713
g6 = 14757395258967641294
g7 = 15679732462653118875
g8 = 16602069666338596456
g9 = 17524406870024074037

      
r = 0
cores=2

print("Loading Address List Please Wait and Good Luck...")
with open("puzzle.txt","r") as m: #Your Address List mix of addresses
    add = m.read().split()
add= set(add)

for x in range (c2):
    if (c3)=="e":
        x = random.randrange(z,zx,1)
    x1 = (g+x) %p
    x2 = (g1+x) %p
    x3 = (g2+x) %p
    x4 = (g3+x) %p
    x5 = (g4+x) %p
    x6 = (g5+x) %p
    x7 = (g6+x) %p
    x8 = (g7+x) %p
    x9 = (g8+x) %p
    x10 = (g9+x) %p

    key1 = Key.from_int(x1)
    key2 = Key.from_int(x2)
    key3 = Key.from_int(x3)
    key4 = Key.from_int(x4)
    key5 = Key.from_int(x5)
    key6 = Key.from_int(x6)
    key7 = Key.from_int(x7)
    key8 = Key.from_int(x8)
    key9 = Key.from_int(x9)
    key10 = Key.from_int(x10)
    wif1 = bytes_to_wif(key1.to_bytes(), compressed=True) #compressed WIF
    wif2 = bytes_to_wif(key2.to_bytes(), compressed=True) #compressed WIF
    wif3 = bytes_to_wif(key3.to_bytes(), compressed=True) #compressed WIF
    wif4 = bytes_to_wif(key4.to_bytes(), compressed=True) #compressed WIF
    wif5 = bytes_to_wif(key5.to_bytes(), compressed=True) #compressed WIF
    wif6 = bytes_to_wif(key6.to_bytes(), compressed=True) #compressed WIF
    wif7 = bytes_to_wif(key7.to_bytes(), compressed=True) #compressed WIF
    wif8 = bytes_to_wif(key8.to_bytes(), compressed=True) #compressed WIF
    wif9 = bytes_to_wif(key9.to_bytes(), compressed=True) #compressed WIF
    wif10 = bytes_to_wif(key10.to_bytes(), compressed=True) #compressed WIF
    myhex1 = "%064x" %x1
    myhex2 = "%064x" %x2
    myhex3 = "%064x" %x3
    myhex4 = "%064x" %x4
    myhex5 = "%064x" %x5
    myhex6 = "%064x" %x6
    myhex7 = "%064x" %x7
    myhex8 = "%064x" %x8
    myhex9 = "%064x" %x9
    myhex10 = "%064x" %x10
    myhex1 = myhex1[:64]
    myhex2 = myhex2[:64]
    myhex3 = myhex3[:64]
    myhex4 = myhex4[:64]
    myhex5 = myhex5[:64]
    myhex6 = myhex6[:64]
    myhex7 = myhex7[:64]
    myhex8 = myhex8[:64]
    myhex9 = myhex9[:64]
    myhex10 = myhex10[:64]
    priv1 = myhex1
    priv2 = myhex2
    priv3 = myhex3
    priv4 = myhex4
    priv5 = myhex5
    priv6 = myhex6
    priv7 = myhex7
    priv8 = myhex8
    priv9 = myhex9
    priv10 = myhex10
    pub1 = privtopub(priv1)
    pub2 = privtopub(priv2)
    pub3 = privtopub(priv3)
    pub4 = privtopub(priv4)
    pub5 = privtopub(priv5)
    pub6 = privtopub(priv6)
    pub7 = privtopub(priv7)
    pub8 = privtopub(priv8)
    pub9 = privtopub(priv9)
    pub10 = privtopub(priv10)
    addr1 = privtoaddr(myhex1)
    addr2 = privtoaddr(myhex2)
    addr3 = privtoaddr(myhex3)
    addr4 = privtoaddr(myhex4)
    addr5 = privtoaddr(myhex5)
    addr6 = privtoaddr(myhex6)
    addr7 = privtoaddr(myhex7)
    addr8 = privtoaddr(myhex8)
    addr9 = privtoaddr(myhex9)
    addr10 = privtoaddr(myhex10)
    caddr1 = key1.address #Legacy compressed address
    caddr2 = key2.address #Legacy compressed address
    caddr3 = key3.address #Legacy compressed address
    caddr4 = key4.address #Legacy compressed address
    caddr5 = key5.address #Legacy compressed address
    caddr6 = key6.address #Legacy compressed address
    caddr7 = key7.address #Legacy compressed address
    caddr8 = key8.address #Legacy compressed address
    caddr9 = key9.address #Legacy compressed address
    caddr10 = key10.address #Legacy compressed address
    
    print(priv1+"\n"+pub1+"\n"+addr1+"\n"+caddr1+"\n")
    print(priv2+"\n"+pub2+"\n"+addr2+"\n"+caddr2+"\n")
    print(priv3+"\n"+pub3+"\n"+addr3+"\n"+caddr3+"\n")
    print(priv4+"\n"+pub4+"\n"+addr4+"\n"+caddr4+"\n")
    print(priv5+"\n"+pub5+"\n"+addr5+"\n"+caddr5+"\n")
    print(priv6+"\n"+pub6+"\n"+addr6+"\n"+caddr6+"\n")
    print(priv7+"\n"+pub7+"\n"+addr7+"\n"+caddr7+"\n")
    print(priv8+"\n"+pub8+"\n"+addr8+"\n"+caddr8+"\n")
    print(priv9+"\n"+pub9+"\n"+addr9+"\n"+caddr9+"\n")
    print(priv10+"\n"+pub10+"\n"+addr10+"\n"+caddr10+"\n")
    

    if addr1 in add:
        print ("Nice One Found!!!",priv1, pub1, addr1) #Legacy uncompressed address
        s1 = priv1
        s2 = pub1
        s3 = addr1
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue
    
    if addr2 in add:
        print ("Nice One Found!!!",priv2, pub2, addr2) #Legacy uncompressed address
        s1 = priv2
        s2 = pub2
        s3 = addr2
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue

    if addr3 in add:
        print ("Nice One Found!!!",priv3, pub3, addr3) #Legacy uncompressed address
        s1 = priv3
        s2 = pub3
        s3 = addr3
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue
    
    if addr4 in add:
        print ("Nice One Found!!!",priv4, pub4, addr4) #Legacy uncompressed address
        s1 = priv4
        s2 = pub4
        s3 = addr4
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue

    if addr5 in add:
        print ("Nice One Found!!!",priv5, pub5, addr5) #Legacy uncompressed address
        s1 = priv5
        s2 = pub5
        s3 = addr5
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue

    if addr6 in add:
        print ("Nice One Found!!!",priv6, pub6, addr6) #Legacy uncompressed address
        s1 = priv6
        s2 = pub6
        s3 = addr6
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue
     
    if addr7 in add:
        print ("Nice One Found!!!",priv7, pub7, addr7) #Legacy uncompressed address
        s1 = priv7
        s2 = pub7
        s3 = addr7
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue
    
    if addr8 in add:
        print ("Nice One Found!!!",priv8, pub8, addr8) #Legacy uncompressed address
        s1 = priv8
        s2 = pub8
        s3 = addr8
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue

    if addr9 in add:
        print ("Nice One Found!!!",priv9, pub9, addr9) #Legacy uncompressed address
        s1 = priv9
        s2 = pub9
        s3 = addr9
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue
    
    if addr10 in add:
        print ("Nice One Found!!!",priv10, pub10, addr10) #Legacy uncompressed address
        s1 = priv10
        s2 = pub10
        s3 = addr10
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue

    if caddr1 in add:
        print ("Nice One Found!!!",priv1, pub1, caddr1) #Legacy uncompressed address
        s1 = priv1
        s2 = pub1
        s3 = caddr1
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue
    
    if caddr2 in add:
        print ("Nice One Found!!!",priv2, pub2, caddr2) #Legacy uncompressed address
        s1 = priv2
        s2 = pub2
        s3 = caddr2
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue

    if caddr3 in add:
        print ("Nice One Found!!!",priv3, pub3, caddr3) #Legacy uncompressed address
        s1 = priv3
        s2 = pub3
        s3 = caddr3
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue
    
    if caddr4 in add:
        print ("Nice One Found!!!",priv4, pub4, caddr4) #Legacy uncompressed address
        s1 = priv4
        s2 = pub4
        s3 = caddr4
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue

    if caddr5 in add:
        print ("Nice One Found!!!",priv5, pub5, caddr5) #Legacy uncompressed address
        s1 = priv5
        s2 = pub5
        s3 = caddr5
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue

    if caddr6 in add:
        print ("Nice One Found!!!",priv6, pub6, caddr6) #Legacy uncompressed address
        s1 = priv6
        s2 = pub6
        s3 = caddr6
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue

    if caddr7 in add:
        print ("Nice One Found!!!",priv7, pub7, caddr7) #Legacy uncompressed address
        s1 = priv7
        s2 = pub7
        s3 = caddr7
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue
    
    if caddr8 in add:
        print ("Nice One Found!!!",priv8, pub8, caddr8) #Legacy uncompressed address
        s1 = priv8
        s2 = pub8
        s3 = caddr8
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue

    if caddr9 in add:
        print ("Nice One Found!!!",priv9, pub9, caddr9) #Legacy uncompressed address
        s1 = priv9
        s2 = pub9
        s3 = caddr9
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue
    
    if caddr10 in add:
        print ("Nice One Found!!!",priv10, pub10, caddr10) #Legacy uncompressed address
        s1 = priv10
        s2 = pub10
        s3 = addr10
        f=open("foundaddress.txt","a")
        f.write(s1+"\n"+s2+"\n"+s3+"\n")
        f.write("\n")
        f.close()
        break #break or continue
    

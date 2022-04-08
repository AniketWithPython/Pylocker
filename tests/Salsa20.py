from Crypto.Hash import SHAKE256
from Crypto.Cipher import Salsa20

filedict={'placeholder':b'placeholder'}
print()
print(filedict)
print()

key=b'\xb5\xafC\xadB\xe6\x95\xf9<I\x1a\xca\xf0\xa8i\xb7\x0cXc_\xfc\xf8\xd6\xe2\xf8No\x14\xc0\xc5z\xfc'

list=filedict.items()
filedict={}
for i,j in list:
    cipher1=Salsa20.new(key)
    cipher2=Salsa20.new(key)
    filename=cipher1.nonce+cipher1.encrypt(i.encode())
    data=cipher2.nonce+cipher2.encrypt(j)
    filedict.update({filename:data})

print(filedict)
print()

keynew=b'\xb5\xafC\xadB\xe6\x95\xf9<I\x1a\xca\xf0\xa8i\xb7\x0cXc_\xfc\xf8\xd6\xe2\xf8No\x14\xc0\xc5z\xfc'

list=filedict.items()
print(list)
print()
filedict={}
for (i,j) in list:
    fnonce=i[:8]
    dnonce=j[:8]
    efilename=i[8:]
    edata=j[8:]
    fdecipher=Salsa20.new(keynew,fnonce)
    ddecipher=Salsa20.new(keynew,dnonce)
    dfilename=fdecipher.decrypt(efilename)
    ddata=ddecipher.decrypt(edata)
    filedict.update({dfilename.decode():ddata})

print(filedict)
print()
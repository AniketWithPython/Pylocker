from Crypto.Hash import SHAKE256
from Crypto.Cipher import Salsa20

keystored=b'\xb5\xafC\xadB\xe6\x95\xf9<I\x1a\xca\xf0\xa8i\xb7\x0cXc_\xfc\xf8\xd6\xe2\xf8No\x14\xc0\xc5z\xfc'

filedict={b'\xf1\xee\xc9\xeed\x18\\\xd5\xc2^\xb6\x89\xbbb\x9b\x8e\x80m\x02': b'\xfe\x01\xa5!\xd2I\x99\t\xeb\xe8u\x9c\xbe\xba\x9f8x!', b'G\x98?~K\x05\xca\xb9"O\xd8{C`\x9d\xce\xeb\xae:\x91^_8': b'\xc1\xfc\xcc\x0eR\xc1\x10\x96\n\x15\x94\x0c5u\xf2\xe4\x1b>\x8e'}

'''def pswdauth(a):
    shake=SHAKE256.new()
    shake.update(a.encode())
    key=shake.read(16)
    return key
    #if key==keystored:
       # return True'''
    
'''def pswdauth(a):
    shake=SHAKE256.new()
    shake.update(a.encode())
    key=shake.read(32)
    shakenew=SHAKE256.new()
    shakenew.update(key)
    key=shakenew.read(32)
    #return key
    #key=str(key)
    #key=key.replace('{','')
    #key=key.replace('}','')
    #keystored1=str(keystored)
    #keystored1=keystored1.replace('{','')
    #keystored1=keystored1.replace('}','')
    if key==keystored:
        return True'''
    
def pswdauth(a):
    shake=SHAKE256.new()
    shake.update(a.encode())
    key=shake.read(32)
    shakenew=SHAKE256.new()
    shakenew.update(key)
    key=shakenew.read(32)
    nlist=filedict.keys()
    for i in nlist:
        nonce=i[:8]
        name=i[8:]
        authcipher=Salsa20.new(key,nonce)
        test=authcipher.decrypt(name)
        try:
            test.decode()
        except UnicodeDecodeError:
            return False
            
        



x='password'

print(pswdauth(x))
#print(pswdauth(x))
'''while True:
    pswdin=input("Enter Password:\t")
    if pswdauth(pswdin)==True:
        break
    else:
        print("INCORRECT PASSWORD\n")'''


try:
    from Crypto.Hash import SHAKE256
    from Crypto.Cipher import Salsa20
except ModuleNotFoundError:               #If module not found
    print("ERROR: pycryptodome isn't installed in your computer.\n\n")
    print("To install pycryptodome in your computer:")
    print("- open command prompt as administrator")
    print("- type _cd C:","Users","User","AppData","Local","Programs","Python","Python39","Scripts_",sep='\\')
    print("- then type _pip install pycryptodome_")
    while True:
        pass

import os
import subprocess as s
import py_compile as pc

def pswdauth(a):
    nlist=filedict.keys()
    for i in nlist:
        nonce=i[:8]
        name=i[8:]
        authcipher=Salsa20.new(a,nonce)
        test=authcipher.decrypt(name)
        try:
            test.decode()
        except UnicodeDecodeError:
            return False

filedict={b'm\xf8\xcb\x0b\xf9\xb1\x10<.\xa6\x89\xd3\x90\xe4\xf0\x06\x08G\xe7': b"\xc3=\x95\x8fJ\xbe\xb8\x80K\xa5\x83\x8e\xba\xf2\x94\xe1'/z"}         #change for generator

while True:
    key=input("Enter Password:\t")
    shake=SHAKE256.new()
    shake.update(key.encode())
    key=shake.read(32)
    shakenew=SHAKE256.new()
    shakenew.update(key)
    key=shakenew.read(32)
    if pswdauth(key)==False:
        print("INCORRECT PASSWORD\n")
    else:
        break
        


dirc=os.getcwd()
pylocker='{}\\pylocker'.format(os.getcwd())     #pylocker folder

if os.path.exists(pylocker):                    #check if exists then remove
    try:
        os.rmdir(pylocker)                      
    except OSError:                             #if folder not empty
        for i in os.listdir(pylocker):
            os.remove('{}\\{}'.format(pylocker,i))
        os.rmdir(pylocker)

os.mkdir(pylocker)                              #make pylocker

for i,j in filedict.items():                            #decrypt and write all files
    fnonce=i[:8]
    dnonce=j[:8]
    efilename=i[8:]
    edata=j[8:]
    fdecipher=Salsa20.new(key,fnonce)
    ddecipher=Salsa20.new(key,dnonce)
    dfilename=fdecipher.decrypt(efilename)
    ddata=ddecipher.decrypt(edata)
    if dfilename.decode()=='placeholder':
        continue
    f=open('{}\\{}'.format(pylocker,dfilename.decode()),'wb')
    f.write(ddata)
    f.close()

s.Popen('Explorer "{}"'.format(pylocker))       #open it
x=input("Press Enter to continue when done")    #wait for user

list=os.listdir(pylocker)                       #encode files
filedict={}
for i in list:
    f=open("{0}\\{1}".format(pylocker,i),'rb')
    a=f.read()
    cipher1=Salsa20.new(key)
    cipher2=Salsa20.new(key)
    filename=cipher1.nonce+cipher1.encrypt(i.encode())
    data=cipher2.nonce+cipher2.encrypt(a)
    filedict.update({filename:data})
    f.close()
    os.remove("{0}\\{1}".format(pylocker,i))

cipher1=Salsa20.new(key)
cipher2=Salsa20.new(key)
filedict.update({cipher1.nonce+cipher1.encrypt(b'placeholder'):cipher2.nonce+cipher2.encrypt(b'placeholder')})

pycode="""try:
    from Crypto.Hash import SHAKE256
    from Crypto.Cipher import Salsa20
except ModuleNotFoundError:               #If module not found
    print("ERROR: pycryptodome isn't installed in your computer.\\n\\n")
    print("To install pycryptodome in your computer:")
    print("- open command prompt as administrator")
    print("- type _cd C:","Users","User","AppData","Local","Programs","Python","Python39","Scripts_",sep='\\\\')
    print("- then type _pip install pycryptodome_")
    while True:
        pass

import os
import subprocess as s
import py_compile as pc

def pswdauth(a):
    nlist=filedict.keys()
    for i in nlist:
        nonce=i[:8]
        name=i[8:]
        authcipher=Salsa20.new(a,nonce)
        test=authcipher.decrypt(name)
        try:
            test.decode()
        except UnicodeDecodeError:
            return False

filedict={0}         #change for generator

while True:
    key=input("Enter Password:\\t")
    shake=SHAKE256.new()
    shake.update(key.encode())
    key=shake.read(32)
    shakenew=SHAKE256.new()
    shakenew.update(key)
    key=shakenew.read(32)
    if pswdauth(key)==False:
        print("INCORRECT PASSWORD\\n")
    else:
        break
        


dirc=os.getcwd()
pylocker='{{}}\\\\pylocker'.format(os.getcwd())     #pylocker folder

if os.path.exists(pylocker):                    #check if exists then remove
    try:
        os.rmdir(pylocker)                      
    except OSError:                             #if folder not empty
        for i in os.listdir(pylocker):
            os.remove('{{}}\\\\{{}}'.format(pylocker,i))
        os.rmdir(pylocker)

os.mkdir(pylocker)                              #make pylocker

for i,j in filedict.items():                            #decrypt and write all files
    fnonce=i[:8]
    dnonce=j[:8]
    efilename=i[8:]
    edata=j[8:]
    fdecipher=Salsa20.new(key,fnonce)
    ddecipher=Salsa20.new(key,dnonce)
    dfilename=fdecipher.decrypt(efilename)
    ddata=ddecipher.decrypt(edata)
    if dfilename.decode()=='placeholder':
        continue
    f=open('{{}}\\\\{{}}'.format(pylocker,dfilename.decode()),'wb')
    f.write(ddata)
    f.close()

s.Popen('Explorer "{{}}"'.format(pylocker))       #open it
x=input("Press Enter to continue when done")    #wait for user

list=os.listdir(pylocker)                       #encode files
filedict={{}}
for i in list:
    f=open("{{}}\\\\{{}}".format(pylocker,i),'rb')
    a=f.read()
    cipher1=Salsa20.new(key)
    cipher2=Salsa20.new(key)
    filename=cipher1.nonce+cipher1.encrypt(i.encode())
    data=cipher2.nonce+cipher2.encrypt(a)
    filedict.update({{filename:data}})
    f.close()
    os.remove("{{}}\\\\{{}}".format(pylocker,i))

cipher1=Salsa20.new(key)
cipher2=Salsa20.new(key)
filedict.update({{cipher1.nonce+cipher1.encrypt(b'placeholder'):cipher2.nonce+cipher2.encrypt(b'placeholder')}})

pycode={1}

f=open('pylocker.txt','w')
f.write(pycode.format(filedict,repr(pycode)))
f.close()
f='pylocker.txt'
base=os.path.splitext(f)[0]
os.rename(f,base+'.py')
pc.compile("pylocker.py")
os.remove('pylocker.py')
os.replace("{{}}\__pycache__\pylocker.cpython-39.pyc".format(dirc),"{{}}\pylocker.pyc".format(dirc))
os.rmdir(pylocker)
os.rmdir('{{}}\__pycache__'.format(dirc))"""

f=open('pylocker.txt','w')
f.write(pycode.format(filedict,repr(pycode)))
f.close()
f='pylocker.txt'
base=os.path.splitext(f)[0]
os.rename(f,base+'.py')
pc.compile("pylocker.py")
os.remove('pylocker.py')
os.replace("{}\__pycache__\pylocker.cpython-39.pyc".format(dirc),"{}\pylocker.pyc".format(dirc))
os.rmdir(pylocker)
os.rmdir('{}\__pycache__'.format(dirc))
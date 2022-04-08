try:
    from Crypto.Hash import SHAKE256
    from Crypto.Cipher import Salsa20
    from stdiomask import getpass
except ModuleNotFoundError:               #If no module
    print(r"""ERROR: requirements aren't installed in your computer.
    
To install pycryptodome:
1. open cmd
2. type 'pip install -r requirements.txt'""")
    while True:
        pass

import os
import subprocess as s
import py_compile as pc

print(r'''Pylocker for Microsoft(R) Windows™ (Python™ 3.9)
(c)Aniket Maity
All Rights Reserved

UPDATES:
- added gzip for better memory and storage management.
- added password mask

Welcome To Pylocker, a software made to keeps your files safe, protected by a password.

Features:
- Uses SHA-256 Hash and Salsa20 encryption.
- only you have the key (your password). It means no one else can decrypt your files.
- if the pylocker is decompiled.....they still don't have the key.

This generator will generate your pylocker. You can make multiple pylockers for your use.

Notes:
- DO NOT put any folders within the pylocker folder.
- It is recommended to not put too many large files (>300MB) otherwise your system may freeze due to limited memory. Multiple small files are ok.

Please enter The following details:

''')

dirc=os.getcwd()

lockername=input("Enter your pylocker name (will be saved as .pylocker in {}):\t".format(dirc))
print()
lockername=' '+lockername

yn='n'
while yn not in ['y','Y']:
    while True:
        password=getpass("Enter your Password:\t")
        print()
        retype=getpass("Retype your Password again:\t")
        print()
        if retype!=password:
            print("ERROR:Passwords do not match\n")
        else:
            break
    yn=input("Do you want to Keep This Password?(y/n):\t")
    print()

placeholder={'placeholder':b'placeholder'}

shake=SHAKE256.new()
shake.update(password.encode())
key=shake.read(32)
shakenew=SHAKE256.new()
shakenew.update(key)
key=shakenew.read(32)

list=placeholder.items()
placeholder={}
for i,j in list:
    cipher1=Salsa20.new(key)
    cipher2=Salsa20.new(key)
    filename=cipher1.nonce+cipher1.encrypt(i.encode())
    data=cipher2.nonce+cipher2.encrypt(j)
    placeholder.update({filename:data})


pylocker="{}\\\\{}.pylocker".format(dirc,lockername)

code='''try:
    from Crypto.Hash import SHAKE256
    from Crypto.Cipher import Salsa20
    from stdiomask import getpass
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
import gzip
import gc

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

filedict={0}

while True:
    key=getpass("Enter Password:\\t")
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
pylocker='{{}}\\\\{1}.pylocker'.format(os.getcwd())     #pylocker folder

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
    name=dfilename.decode()
    name=name.replace('.gz','')
    zipped=gzip.open('{{}}\\\\{{}}'.format(pylocker,dfilename.decode()))
    f=open('{{}}\\\\{{}}'.format(pylocker,name),'wb')
    f.write(zipped.read())
    f.close()
    zipped.close()
    os.remove('{{}}\\\\{{}}'.format(pylocker,dfilename.decode()))

s.Popen('Explorer "{{}}"'.format(pylocker))       #open it
x=input("Press Enter to continue when done")    #wait for user
print("Please wait, The application will close automatically when encryption is completed...")

list=os.listdir(pylocker)                       #encode and encrypt files
filedict={{}}
for i in list:
    file=open("{{}}\\\\{{}}".format(pylocker,i),'rb')
    data=file.read()
    zip=gzip.open("{{}}\\\\{{}}.gz".format(pylocker,i),"wb")
    zip.write(data)
    zip.close()
    file.close()
    os.remove("{{}}\\\\{{}}".format(pylocker,i))
    name=i+'.gz'
    f=open("{{}}\\\\{{}}".format(pylocker,name),'rb')
    a=f.read()
    cipher1=Salsa20.new(key)
    cipher2=Salsa20.new(key)
    filename=cipher1.nonce+cipher1.encrypt(name.encode())
    data=cipher2.nonce+cipher2.encrypt(a)
    filedict.update({{filename:data}})
    f.close()
    os.remove("{{}}\\\\{{}}".format(pylocker,name))


cipher1=Salsa20.new(key)
cipher2=Salsa20.new(key)
filedict.update({{cipher1.nonce+cipher1.encrypt(b'placeholder'):cipher2.nonce+cipher2.encrypt(b'placeholder')}})

pycode="""try:
    from Crypto.Hash import SHAKE256
    from Crypto.Cipher import Salsa20
    from stdiomask import getpass
except ModuleNotFoundError:               #If module not found
    print("ERROR: pycryptodome isn't installed in your computer.\\\\n\\\\n")
    print("To install pycryptodome in your computer:")
    print("- open command prompt as administrator")
    print("- type _cd C:","Users","User","AppData","Local","Programs","Python","Python39","Scripts_",sep='\\\\\\\\')
    print("- then type _pip install pycryptodome_")
    while True:
        pass

import os
import subprocess as s
import py_compile as pc
import gzip
import gc

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

filedict={{0}}         #change for generator

while True:
    key=getpass("Enter Password:\\\\t")
    shake=SHAKE256.new()
    shake.update(key.encode())
    key=shake.read(32)
    shakenew=SHAKE256.new()
    shakenew.update(key)
    key=shakenew.read(32)
    if pswdauth(key)==False:
        print("INCORRECT PASSWORD\\\\n")
    else:
        break
        
dirc=os.getcwd()
pylocker='{{{{}}}}\\\\\\\\{1}.pylocker'.format(os.getcwd())     #pylocker folder

if os.path.exists(pylocker):                    #check if exists then remove
    try:
        os.rmdir(pylocker)                      
    except OSError:                             #if folder not empty
        for i in os.listdir(pylocker):
            os.remove('{{{{}}}}\\\\\\\\{{{{}}}}'.format(pylocker,i))
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
    f=open('{{{{}}}}\\\\\\\\{{{{}}}}'.format(pylocker,dfilename.decode()),'wb')
    f.write(ddata)
    f.close()
    name=dfilename.decode()
    name=name.replace('.gz','')
    zipped=gzip.open('{{{{}}}}\\\\\\\\{{{{}}}}'.format(pylocker,dfilename.decode()))
    f=open('{{{{}}}}\\\\\\\\{{{{}}}}'.format(pylocker,name),'wb')
    f.write(zipped.read())
    f.close()
    zipped.close()
    os.remove('{{{{}}}}\\\\\\\\{{{{}}}}'.format(pylocker,dfilename.decode()))

s.Popen('Explorer "{{{{}}}}"'.format(pylocker))       #open it
x=input("Press Enter to continue when done")    #wait for user
print("Please wait, The application will close automatically when encryption is completed...")

list=os.listdir(pylocker)                       #encode and encrypt files
filedict={{{{}}}}
for i in list:
    file=open("{{{{}}}}\\\\\\\\{{{{}}}}".format(pylocker,i),'rb')
    data=file.read()
    zip=gzip.open("{{{{}}}}\\\\\\\\{{{{}}}}.gz".format(pylocker,i),"wb")
    zip.write(data)
    zip.close()
    file.close()
    os.remove("{{{{}}}}\\\\\\\\{{{{}}}}".format(pylocker,i))
    name=i+'.gz'
    f=open("{{{{}}}}\\\\\\\\{{{{}}}}".format(pylocker,name),'rb')
    a=f.read()
    cipher1=Salsa20.new(key)
    cipher2=Salsa20.new(key)
    filename=cipher1.nonce+cipher1.encrypt(name.encode())
    data=cipher2.nonce+cipher2.encrypt(a)
    filedict.update({{{{filename:data}}}})
    f.close()
    os.remove("{{{{}}}}\\\\\\\\{{{{}}}}".format(pylocker,name))
    

cipher1=Salsa20.new(key)
cipher2=Salsa20.new(key)
filedict.update({{{{cipher1.nonce+cipher1.encrypt(b'placeholder'):cipher2.nonce+cipher2.encrypt(b'placeholder')}}}})

pycode={{1}}

f=open('{1}.pylocker.txt','w',8192)
print(gc.collect())
f.write(pycode.format(filedict,repr(pycode)))
f.close()
f='{1}.pylocker.txt'
base=os.path.splitext(f)[0]
os.rename(f,base+'.py')
pc.compile("{1}.pylocker.py")
os.remove('{1}.pylocker.py')
os.replace("{{{{}}}}\__pycache__\{1}.pylocker.cpython-39.pyc".format(dirc),"{{{{}}}}\{1}.pylocker.pyc".format(dirc))
os.rmdir(pylocker)
os.rmdir('{{{{}}}}\__pycache__'.format(dirc))"""

f=open('{1}.pylocker.txt','w',8192)
print(gc.collect())
f.write(pycode.format(filedict,repr(pycode)))
f.close()
f='{1}.pylocker.txt'
base=os.path.splitext(f)[0]
os.rename(f,base+'.py')
pc.compile("{1}.pylocker.py")
os.remove('{1}.pylocker.py')
os.replace("{{}}\__pycache__\{1}.pylocker.cpython-39.pyc".format(dirc),"{{}}\{1}.pylocker.pyc".format(dirc))
os.rmdir(pylocker)
os.rmdir('{{}}\__pycache__'.format(dirc))'''

f=open('{}.pylocker.txt'.format(lockername),'w')
f.write(code.format(placeholder,lockername))
f.close()
f='{}.pylocker.txt'.format(lockername)
base=os.path.splitext(f)[0]
os.rename(f,base+'.py')
pc.compile('{}.pylocker.py'.format(lockername))
os.remove('{}.pylocker.py'.format(lockername))
os.replace("{0}\__pycache__\{1}.pylocker.cpython-39.pyc".format(dirc,lockername),"{0}\{1}.pylocker.pyc".format(dirc,lockername))
os.rmdir('{}\__pycache__'.format(dirc))
print("File generated in",dirc)
print("you may close this window now")
while True:
    pass

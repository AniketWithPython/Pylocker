import gzip
import zlib
file=open("C:\\Users\\User\\Desktop\\dummy files\\Binder2.tiff",'rb')
data=file.read()
zip=gzip.open("C:\\Users\\User\\Desktop\\dummy files\\Binder2.tiff.gz","wb")
zip.write(data)
zip.close()

'''file=gzip.open("C:\\Users\\User\\Desktop\\dummy files\\Binder2.tiff.gz")
unzip=open("C:\\Users\\User\\Desktop\\dummy files\\Binder2.tiff",'wb')
unzip.write(file.read())
unzip.close()'''
# Pylocker
This software generates an encrypted locker which is protected by a password. This uses [`pycryptodome`](https://pypi.org/project/pycryptodome/) library.<br><br>
Updates:<br>
* Added gzip for better memory and storage management.
* Added password mask

<br><br>
To install pycryptodome:<br>
```
pip install -r requirements.txt
```
<br>

To use the software:<br>
* Run the pylockergenerator to generate a pylocker folder (a `.pyc` file will be generated with the name "filename.pylocker")
* open the `.pyc` file and enter the password in the terminal window to access the folder
* once completed, press enter in the terminal window. The software will close automatically once all the files have been encrypted.

Notes: 
* This works only if [Python 3.9](https://www.python.org/downloads/) is installed.
* DO NOT put any folders within the pylocker folder
* It is recommended to not put too many large files (>300MB) otherwise your system may freeze due to limited memory. Multiple small files are ok.

> Pylocker for Microsoft® Windows™ (Python™ 3.9) ©Aniket Maity All Rights Reserved

> Created for educational purposes only.

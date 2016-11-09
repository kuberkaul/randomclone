**randomclone**

This is a clone of /dev/random functionality with its own entropy pool and the source of entropy being sucked in form of json from http://qrng.anu.edu.au over network.

http://qrng.anu.edu.au is a open source free source of truly random number and has been used as source of entropy here. This project has been inspired from a multiple papers from Columbia University, open source projects and python package - random.(https://docs.python.org/2/library/random.html)


**Installation**

Clone the project and run the command ```python setup.py install``` from the root of the project directory. Run ```randomc``` as entry point after that from terminal.

You would need root permissions to run this 

**Requirements**

This project has been tested under ```python -V : Python 2.7.12``` and Linux/Mac

Other requirements for randomclone should be automatically installed as part the install.

**Brief**

This project took 2 hours 49 minutes to code and document starting from researching into how /dev/random works, how it is different from /dev/urandom and entropy pool for linux. A decision was taken by me to use the http://qrng.anu.edu.au as source of entropy instead of connecting to a device driver and collecting entropy for sake of speed of demo and time limitations.

**Demo**

To get a stream of binary randomness :

```randomc -b ```

To get a stream of hex randomness :

```randomc -h ```

To get a stream of binary or hex randomness but limit by count (1 count = 1024 chars):

binary : ```randomc -b --count 2```
hex: ```randomc -h --count 2```

**Simplified version of how randomclone works ?**

As you hit the entry point randomc, the tool uses json parsing libraries to get random data from http://qrng.anu.edu.au in form of json and depending upon the type of data type it converts hex to binary or leaves it be. It then pushes this data into buffer which is a python list and acts as a buffer(Last In First Out) till the buffer is completely repenished. As soon as it replenishes the data it then goes according to the count argument given pipes out that amount of randomness to the standard output which can be piped to wherever the user wants.

- Note : The size of the buffer is kept at 5 for the demo but can be increased to whatever. keeping it at 5 allows for quick replenishing of the buffer.

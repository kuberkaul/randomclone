"""
CLI Entry point for randomclone
"""

#imports for use of functionality
from __future__ import print_function

import sys
import randomclone
import traceback
import time
from errors import RandomCloneResourceError

#entropy list here acts as the entropy pool for randomclone. I have limited the size to 5 just to keep the tool fast for a demo. It obviously could be increased to whatever size you would want the entropy to be. As a list you dont have to increase for more entropy space as list in python automatically increases/decreases in size as more slots are filled/removed
MAX_BUFFER = 5
entropy = []

#Entropy buffer method just creates the entropy and replenishes it before piping it out for use. Commenting out print commands as they are not needed. Can be uncommented to just track progress better.
def entropy_buffer(type):
    running = False
    # print("Replenishing Buffer")
    global entropy
    running = True
    #based on type of argument we call different function in init.
    if type == 'binary':
        randomness = randomclone.binary()
    elif type == 'hex':
        randomness = randomclone.hex()
    else:
        RandomCloneResourceError('incorrect type mentioned; has to be either -b or -h')
        sys.exit(1)
    try:
        while running:
            #make sure the entropy pool is filled completely before piping out values.
            if len(entropy) > MAX_BUFFER:
                # print("Buffer at capacity; thread sleeping")
                time.sleep(1)
                break
            entropy.append(randomness)
            # print("New random data buffered")
    except:
        print(traceback.format_exc())
    running = False

#command line attrib randomc calls th main which in turn checks for argument and calls the entropy_buffer method.
def main():
    scheme = ("Usage: %s [--binary -b|--hex -h]" +
             " [--count BLOCKS]") % sys.argv[0]
    generator = None
    argvalue = None
    #http://qrng.anu.edu.au pipes out both binary and hex randomness to use as a TRNG
    if '--binary' in sys.argv or '-b' in sys.argv:
        generator = entropy_buffer('binary')
        argvalue = 1
    if '--hex' in sys.argv or '-h' in sys.argv:
        generator = entropy_buffer('hex')
        argvalue = 1
    if not argvalue:
        print(scheme)
        sys.exit(1)
    try:
        # to pipe as much randomness as user wants.
        maxcounts = 0
        counts = -1
        if '--count' in sys.argv:
            maxcounts = int(sys.argv[sys.argv.index('--count') + 1])
            counts = 0
        #keep popping randomness from the entropy pool till we are emptyand begin repleneishing.
        while True:
            if maxcounts and counts >= maxcounts:
                break
            print(entropy.pop())
            counts += 1
    except:
        pass


if __name__ == '__main__':
    main()

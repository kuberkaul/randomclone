"""
init method for randomclone.
"""
import binascii
import math
import sys
import six
from randomclone import errors

# making sure we have json parser/urllib to parse JSON from  http://qrng.anu.edu.au and work with all version of python 2.x
try:
    from urllib.parse import urlencode
    from urllib.request import urlopen
except ImportError:
    from urllib import urlencode
    from urllib2 import urlopen
try:
    import json
except ImportError:
    import simplejson as json

# http://qrng.anu.edu.au acts as the source of truly random quantum number. The entropy pool is filled with this as a source till the buffer is replenished and then is piped out from the comman dline tool randomc that acts as a clone to /dev/random
RANDOMURL = 'https://qrng.anu.edu.au/API/jsonI.php'

def get_randomness(randomness_type='hex16', array_length=1, size_of_block=1):
    random_url = RANDOMURL + '?' + urlencode({
        'type': randomness_type,
        'length': array_length,
        'size': size_of_block,
    })
    data = load_json(random_url)
    assert data['success'] is True, data
    assert data['length'] == array_length, data
    return data['data']


#system check for python 2.x, may not work with python 3 and above
if sys.version_info[0] == 2:
    def load_json(random_url):
        return json.loads(urlopen(random_url).read(), object_hook=_object_hook)

    def _object_hook(obj):
        if obj.get('randomness_type') == 'string':
            obj['data'] = [s.encode('ascii') for s in obj['data']]
        return obj

else:
    #To make sure porgram doesnt quit.
    def load_json(random_url):
        return json.loads(urlopen(random_url).read().decode('ascii'))

# get binaries
def binary(array_length=100, size_of_block=100):
    return binascii.unhexlify(six.b(hex(array_length, size_of_block)))
#get hex
def hex(array_length=100, size_of_block=100):
    return ''.join(get_randomness('hex16', array_length, size_of_block))

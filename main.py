from string import ascii_lowercase
from string import ascii_uppercase
from itertools import product
import hashlib
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-hash", "--hash", dest = "hash", help="Hash Value", type=str)
parser.add_argument("-word", "--word", dest = "word", help="If you have a word you want to test.", type=str)
parser.add_argument("-i", "--intensity", dest = "intensity", default = "1", help="Intensity", type=str)
args = parser.parse_args()

MAX_RANGE = 25

def convertToMD5(word):
    return hashlib.md5(word.encode()).hexdigest()

def crack_hash(CHAR_SET, hsh, maxrange):
    for i in range(maxrange+1):
        for i in product(CHAR_SET, repeat=i):
            newHash = convertToMD5(''.join(i))
            if newHash == hsh:
                p = ''.join(i)
                return '{}:{}'.format(p, newHash)

def main():
    if args.intensity == '1':
        intensity = ascii_lowercase
    elif args.intensity == '2':
        intensity = ascii_lowercase+ascii_uppercase
    elif args.intensity =='3':
        intensity = ascii_lowercase + ascii_uppercase + "1234567890"
    else: 
        intensity = ascii_lowercase + ascii_uppercase + "1234567890" + " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    start_time=time.time()
    print(crack_hash(intensity, args.hash, MAX_RANGE))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()

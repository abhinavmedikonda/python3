import hashlib
import uuid
import random

def decode(hsh, sto):
    return sto.get(hsh, None)

def encoede(url, sto):
    # hsh = hash()
    hsh = get_random(4)
    itr = 1
    while hsh in sto:
        hsh = hash()
        itr += 1
    print("tries: ", itr)
    sto[hsh] = url
    return hsh

def get_random(lnt):
    chr = '0123456789_abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _out = []
    for _ in range(lnt):
        rnd = random.randint(0, len(chr)-1)
        _out.append(chr[rnd])
    return ''.join(reversed(_out))

# def hash():
#     uid = uuid.uuid4().bytes
#     bts = hashlib.blake2b(uid, digest_size=1).digest()
#     print(bts, len(bts))
#     num = int.from_bytes(bts)

if __name__ == '__main__':
    sto = dict()
    while True:
        print(f'''\ntoatl: {len(sto)}\n1. Encode\n2. Decode\n3. Exit''')
        match input('Enter choice: '):
            case '1':
                url = input('Enter URL to encode: ')
                hsh = encoede(url, sto)
                print(f'Encoded URL: {hsh}')
            case '2':
                hsh = input('Enter hash to decode: ')
                url = decode(hsh, sto)
                if url:
                    print(f'Decoded URL: {url}')
                else:
                    print('Hash not found')
            case '3':
                break
            case _:
                print('Invalid choice')
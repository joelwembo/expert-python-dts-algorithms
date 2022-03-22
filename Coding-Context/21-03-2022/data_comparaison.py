import hashlib, sys

files = [sys.argv[1], sys.argv[2]]

def md5(fname):
    md5hash = hashlib.md5()
    with open(fname) as handle:
        for line in handle:
            md5hash.update(line.encode('utf-8'))
    return (md5hash.hexdigest())     


print('Comparing files:', files[0], 'and', files[1])

if md5(files[0]) == md5(files[1]):
    print('Matched')
else:
    print('Not Matches')               
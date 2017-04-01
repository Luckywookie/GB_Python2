import os
import random
import hashlib
from work_file_md5 import func_hex_file


def hash_str(stroka, method):
    res = hashlib.new(method, stroka).hexdigest()
    return res


def break_file(orig_file, size_piece, directory):
    with open(orig_file, 'rb') as file_open:
        f = file_open.read()
        count = 0
        for i in f:
            if f:
                count += 1
                piece = f[:size_piece]
                hash_f = hash_str(piece, 'md5')
                open(directory + '/parts.md5', 'a').write(hash_f + '\n')
                open(directory + '/file' + str(random.randint(1, 10000)), 'wb').write(piece)
                f = f[size_piece:]
        return count


# break_file('file1/all_files.jpg', 100000, 'file3')


def hash_dir(path, out_file):
    # Create dictionary of key=hex and value=file
        file_list = os.listdir(path)
        n = 0
        for fil in file_list:
            if fil == 'parts.md5':
                continue
            hes = func_hex_file(path + '/', fil)
            open(path + out_file, 'a').write(hes + '\n')
            n += 1
        return n

# hash_dir('file3/', 'ffff.md5')


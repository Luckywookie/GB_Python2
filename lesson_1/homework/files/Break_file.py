import random
import hashlib


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


print(break_file('file1/all_files.jpg', 100000, 'file3'))


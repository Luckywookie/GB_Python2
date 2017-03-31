import os
import hashlib


# Count hex of file
def func_hex_file(path, file):
    with open(path + file, 'rb') as fl:
        hex_file = hashlib.md5(fl.read()).hexdigest()
        return hex_file


# Create dictionary of key=hex and value=file
def hex_dic(path):
    file_list = os.listdir(path)
    d = dict()
    for file in file_list:
        if file == 'parts.md5':
            continue
        hes = func_hex_file(path + '/', file)
        d.update({hes: file})
    return d


# Create list of hash from file parts.md5
def analys_md5_list(path):
    with open(path + '/parts.md5', 'r') as f:
        md5_list = []
        for row in f.readlines():
            md5_list.append(row[:-1])
    return md5_list


# Sorting of pieces in order from parts.md5
def file_order(path):
    file_list_order = []
    for i in analys_md5_list(path):
        file_list_order.append(hex_dic(path)[i])
    return file_list_order


# Function which write to file all of the pieces
def write_file_base(path, out_file):
    all_files = []
    for file in file_order(path):
        all_files.append(open(path + '/' + file, 'rb').read())

    with open(path + '/' + out_file, 'ab') as output:
        for i in all_files:
            output.write(i)


if __name__ == '__main__':
    write_file_base('file1', 'allfiles')
    write_file_base('file2', 'allfiles')

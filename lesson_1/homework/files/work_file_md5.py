import os
import hashlib


# Count hex of file
def func_hex_file(PATH, file):
    with open(PATH + file, 'rb') as fl:
        hex_file = hashlib.md5(fl.read()).hexdigest()
        return hex_file


# Create dictionary of key=hex and value=file
def hex_dic(PATH):
    file_list = os.listdir(PATH)
    d = dict()
    for file in file_list:
        if file == 'parts.md5':
            continue
        hes = func_hex_file(PATH + '/', file)
        d.update({hes: file})
    return d


# Create list of hash from file parts.md5
def analys_md5_list(PATH):
    with open(PATH + '/parts.md5', 'r') as f:
        md5_list = []
        for row in f.readlines():
            md5_list.append(row[:-1])
    return md5_list


# Sorting of pieces in order from parts.md5
def file_order(PATH):
    file_list_order = []
    for i in analys_md5_list(PATH):
        file_list_order.append(hex_dic(PATH)[i])
    return file_list_order


# Function which write to file all of the pieces
def write_file_base(PATH, OUTPUT):
    all_files = []
    for file in file_order(PATH):
        all_files.append(open(PATH + '/' + file, 'rb').read())

    with open(PATH + '/' + OUTPUT, 'ab') as output:
        for i in all_files:
            output.write(i)


if __name__ == '__main__':
    write_file_base('file1', 'allfiles')
    write_file_base('file2', 'allfiles')

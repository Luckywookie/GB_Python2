import hashlib
import csv


PATH_IN = 'need_hashes.csv'
PATH_OUT = 'output.csv'


with open(PATH_IN, 'r', newline='') as csvfile, open(PATH_OUT, 'w') as output_file:
    csv_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    writer = csv.writer(output_file, delimiter=';', quotechar='|')
    for row in csv_reader:
        func = row[1]
        s = row[0].encode(encoding='utf-8')
        if func == 'sha1':
            t = hashlib.sha1(s).hexdigest()
        elif func == 'md5':
            t = hashlib.md5(s).hexdigest()
        elif func == 'sha512':
            t = hashlib.sha512(s).hexdigest()
        else:
            t = ''
        writer.writerow(row[:-1] + [t])



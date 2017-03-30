import hashlib
import csv


with open('./homework/need_hashes.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    output_file = open('output.csv', 'w')
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
        writer.writerow(row[:-1] + [t])



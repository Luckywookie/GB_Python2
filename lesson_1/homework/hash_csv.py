import hashlib
import csv
import unittest


PATH_IN = 'need_hashes.csv'
PATH_OUT = 'output.csv'


def hash_str(stroka, method):
    stroka = stroka.encode(encoding='utf-8')
    res = hashlib.new(method, stroka).hexdigest()
    return res


with open(PATH_IN, 'r', encoding='utf-8', newline='') as csvfile, open(PATH_OUT, 'w', encoding='utf-8') as output_file:
    csv_reader = csv.reader(csvfile, delimiter=';')
    writer = csv.writer(output_file, delimiter=';')
    for row in csv_reader:
        s = row[0]
        method = row[1]
        writer.writerow(row[:-1] + [hash_str(s, method)])

#print(hashlib.md5('Тили-мили-трямзия'.encode(encoding='utf-8')).hexdigest())
#print(hash_str('Я люблю Питон', 'md5'))


class TestSalary(unittest.TestCase):

    def test_hash_str_sha1(self):
        self.assertEqual(hash_str('I love Python', 'sha1'), '9233eac58259dd3a13d6c9c59f8001823b6b1fee')

    def test_hash_str_md5(self):
        self.assertEqual(hash_str('Я люблю Питон', 'md5'), '50b461d17299cc037a432307a2d93a55')

    def test_hash_str_md5_1(self):
        self.assertEqual(hash_str('Тили-мили-трямзия', 'md5'), 'd692436bc029b8c87916057990105098')


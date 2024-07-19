import csv
import os


def read_volumes():
    filename = r'C:\PATH\volumes.csv'
    if '_MEIPASS2' in os.environ:
        filename = os.path.join(os.environ['_MEIPASS2'], filename)

    with open (filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            out = []
            for r in row:
                out.append(int(r))
            return out


def write_volumes(volumes):
    with open(r'C:\PATH\volumes.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')

        writer.writerow(volumes)

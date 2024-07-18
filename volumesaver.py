import csv


def read_volumes():
    with open ('volumes.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            out = []
            for r in row:
                out.append(int(r))
            return out


def write_volumes(volumes):
    # Only do this every 5 minutes, counting this way to avoid tkinter causing lag because the entered waiting time is too high

    with open('volumes.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')

        writer.writerow(volumes)

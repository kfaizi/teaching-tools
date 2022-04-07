# generate mailing list from csv of student usernames

import argparse
import csv
import re

parser = argparse.ArgumentParser(description='select file')
parser.add_argument('-i', '--input', help='Full path to input file', required=True)
args = parser.parse_args()

with open(args.input, "r", newline='') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    emails = []
    for row in reader:
        emails.append(str(row[0]+"@ucsd.edu"))

# return copy-pasteable list
print(", ".join(i for i in emails))

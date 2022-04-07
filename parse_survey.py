# read short-answer survey responses from the csv generated by canvas
# extract answers from my students only
# group and present with option to anonymize

# maybe transition to a jupyter notebook?
# extract plain text from responses and plot word frequencies (quick sentiment analysis?)
# streamline process from reading responses to actionable changes:
#   - identify problems
#   - suggest keywords to focus on
#   - email template for responses?
#   - generate a report pdf with sections for each question, keywords highlighted


import argparse
import csv
import re

parser = argparse.ArgumentParser(description='select file')
parser.add_argument('-i', '--input', help='Full path to input file', required=True)
args = parser.parse_args()

with open(args.input, "r", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for col in row.keys():
            match = re.search('^\d', col)
            if match: # column starts with a number
                if len(col.split(': ')) > 1:
                    # then we have found the columns we're looking for
                    pass
        if row['section_id'] == '37000':
            # then we have found the rows we're looking for
            pass



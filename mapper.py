!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    # Split the line by comma (assuming no commas inside fields)
    fields = line.split(',')

    # Assuming the dataset has 7 columns and manufacturer is the 7th column (index 6)
    if len(fields) == 7:
        manufacturer = fields[6].strip()

        print(f"{manufacturer}\t1")

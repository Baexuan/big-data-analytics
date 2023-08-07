#!/usr/bin/env python3

import sys

#Dictionary to store the word count for the "manufacturer" column
manufacturer_count = {}

#Iterate through each line in the input data received from Hadoop Streaming
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespaces
    fields = line.split(',')  # Split the CSV line into fields

    # Assuming "manufacturer" is the 7th column (index 6) in your CSV data
    if len(fields) >= 7:
        manufacturer = fields[6].strip().lower()  # Extract and convert the manufacturer to lowercase

        # Increment the count of the manufacturer in the dictionary
        manufacturer_count[manufacturer] = manufacturer_count.get(manufacturer, 0) + 1
      
#Output the result
for manufacturer, count in manufacturer_count.items():
    print(f"{manufacturer}: {count}")

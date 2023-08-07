#!/usr/bin/env python3

import sys

# Initialize variables to keep track of the current manufacturer and count
current_manufacturer = None
current_count = 0

# Iterate through the input lines from the standard input (Hadoop Streaming)
for line in sys.stdin:
    line = line.strip()

    # Split the input line into 'manufacturer' and 'count' fields separated by '\t'
    manufacturer, count = line.split('\t', 1)

    try:
        count = int(count)  # Convert the count to an integer
    except ValueError:
        continue  # Skip this line if the count is not a valid integer

    # Check if the current manufacturer matches the previous one
    if current_manufacturer == manufacturer:
        current_count += count  # Accumulate the count for the current manufacturer
    else:
        # If the manufacturer changes, print the count for the previous manufacturer (if any)
        if current_manufacturer:
            print(f"{current_manufacturer}\t{current_count}")

        # Update the current manufacturer and reset the count to the current line's count
        current_manufacturer = manufacturer
        current_count = count

# Print the final count for the last manufacturer
if current_manufacturer:
    print(f"{current_manufacturer}\t{current_count}")

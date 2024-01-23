import csv
from datetime import datetime

# Function to convert date format
def convert_date_format(date_str):
    try:
        # Convert 'DD-MM-YY' to 'YYYY-MM-DD'
        return datetime.strptime(date_str, '%d-%m-%y').strftime('%Y-%m-%d')
    except ValueError:
        # Return the original string if it's not a valid date
        return date_str

# File paths
input_file_path = 'order.csv'  # File in the current directory
output_file_path = 'order-yy.csv'  # Output file in the current directory

# Read the input file and write to the output file
with open(input_file_path, 'r') as csvfile, open(output_file_path, 'w', newline='') as outputfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(outputfile)

    # Assuming the first row is the header
    headers = next(reader)
    writer.writerow(headers)

    # Process each row
    for row in reader:
        # Convert date in columns B and C (indexes 1 and 2)
        row[1] = convert_date_format(row[1])
        row[2] = convert_date_format(row[2])
        writer.writerow(row)

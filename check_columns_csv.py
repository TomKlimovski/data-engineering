import csv

filename = 'output_quack.csv'

# Open the CSV file for reading
with open(filename, 'r') as csv_file:
  # Create a CSV reader object
  reader = csv.reader(csv_file)
  
  # Iterate through the rows of the CSV file
  for row in reader:
    # Check if the row has 40 columns
    # print(f"Row has {len(row)} columns")
    if len(row) == 41:
      # The row has 40 columns, do something with it
      pass
    else:
      # The row does not have 40 columns, handle the error as desired
      print("Error: row does not have 41 columns")

# Open the CSV file for reading
with open(filename, 'r') as csv_file:
  # Move the file pointer to the desired position
  csv_file.seek(202707397)
  
  # Read the line from the file
  line = csv_file.readline()
  
  # Print the line
  print(line)
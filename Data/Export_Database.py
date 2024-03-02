import csv
# Columns to export
columns_to_export = ['Name', 'Crystal Structure','Diaphaneity','Specific Gravity','Optical','Refractive Index','Molar Mass','Molar Volume','Calculated Density']

# Open the input CSV file
with open('Mineral Database.csv', newline='') as infile:
    # Create a CSV reader object
    reader = csv.DictReader(infile)
    
    # Open the output CSV file
    with open('Database_Filtered.csv', 'w', newline='') as outfile:
        # Define the fieldnames for the output CSV file
        fieldnames = columns_to_export
        
        # Create a CSV writer object
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write the header row
        writer.writeheader()
        
        # Iterate over each row in the input CSV file
        for row in reader:
            # Create a dictionary containing only the columns to export
            selected_columns = {col: row[col] for col in columns_to_export}
            
            # Write the selected columns to the output CSV file
            writer.writerow(selected_columns)
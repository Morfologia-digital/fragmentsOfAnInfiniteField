import requests
import re
import csv


def findHashFromTokenId(token_id):
    base_url = "https://generator.artblocks.io/0xa7d8d9ef8d8ce8992df33d8b8cf4aebabd5bd270/"
    url = base_url + token_id
    response = requests.get(url)
    data = response.text
    
    match = re.search(r'let tokenData = {"tokenId":"' + token_id + '","hash":"(.+?)"}', data)
    if match:
        # Print the hash if it was found
        return match.group(1)
    
i = 1;
    
# Open the CSV file in read mode
with open('tokens.csv', 'r', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    # Skip the header row
    header = next(reader)
    # Create a list to hold the updated rows
    updated_rows = [header]
    # Iterate over the rows in the file
    for row in reader:
        # Update the value in the new column
        id = row[0] # Replace "1" with the index of the old column
        hash = findHashFromTokenId(id)
        row[10] = hash # Replace "2" with the index of the new column
        # Add the updated row to the list
        updated_rows.append(row)
        print("Updated row: " + str(i) + ": " + hash)
        i = i + 1

# Write the updated data back to the CSV file
with open('input.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    # Write the updated rows to the file
    writer.writerows(updated_rows)  
    










    
    


# token_ids = []

# with open('tokens.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         token_ids.append(row['tokenID'])

# # The base URL for the generator
# base_url = "https://generator.artblocks.io/0xa7d8d9ef8d8ce8992df33d8b8cf4aebabd5bd270/"

# # An array of token IDs to search for
# # token_ids = ["159000111", "159000112", "159000113"]

# # Loop through the token IDs and fetch the data
# for token_id in token_ids:
#     url = base_url + token_id
#     response = requests.get(url)
#     data = response.text

#     # Use regular expressions to find the hash in the data
#     match = re.search(r'let tokenData = {"tokenId":"' + token_id + '","hash":"(.+?)"}', data)
#     if match:
#         # Print the hash if it was found
#         print(match.group(1))

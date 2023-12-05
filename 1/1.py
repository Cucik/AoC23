# Define the file path
import re
file_path = 'input.txt'

# Open the file and read it line by line
results= ['','']
final_results = []
lineread = []
pattern = r'\d'
counter = 0
with open(file_path, 'r') as file:
    for line in file:
#        print(line.strip())  # strip() removes any leading/trailing whitespace including newline characters
        for character in line.strip():
            if results[0] is None:
                if re.match(pattern, character):
                    results[0]=character
            if re.match(pattern, character):
                results[1]=character
            print(results[0],results[1])
        final_results[counter]=int(results[0])+int(results[1])
        counter=counter+1
print(final_results)



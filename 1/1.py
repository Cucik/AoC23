# Define the file path
import re
file_path = 'input.txt'

# Open the file and read it line by line
results= ['','']
final_results = []
lineread = []
pattern = r'\d'
counter = 0

word_to_number = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

number_words = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','wordscannotdescribemyconfusion'
]
final_results=0

with open(file_path, 'r') as file:
    for line in file:
        converted_table = []
        match = re.search(pattern,line)
        #print(match.group())
        number_word_pattern = r'.*' + '|'.join(number_words) + r'.*'
        found_number_words = re.findall(number_word_pattern, line)

        print(found_number_words)

        if(found_number_words[0]) in word_to_number.keys():
            substring1 = word_to_number[found_number_words[0]]
        else:
            substring1=found_number_words[0]

        if(found_number_words[-1]) in word_to_number.keys():
            substring2 = word_to_number[found_number_words[-1]]
        else:
            substring2=found_number_words[-1]

        strings=str(substring1) + str(substring2)
        print(strings)
        final_results=int(strings)+final_results


print(final_results)
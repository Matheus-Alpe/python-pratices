import json
import csv
import re
from os import listdir
from os.path import isfile, isdir, join, splitext



##########################################
#
#
# input words that you expect to match
#
# 
match_words = ['camisa', 'bermuda', 'short']
#
#
#
#
#
#########################################



def send_message_and_exit(message): 
    print("\n<< " + message + " >>\n", "\n...Exiting...")
    exit()


if not len(match_words) > 0:
    send_message_and_exit("Enter at least one word on variable 'match_words' to match what you expect!")


apiKey = input("ApiKey folder path containing dumps (example: <apiKey>): ")


if apiKey == "":
    send_message_and_exit("Missing apiKey folder.")

files_path = "./" + apiKey + "/"

if not isdir(files_path):
    send_message_and_exit("There is no folder with this apiKey.")

onlyfiles = [file for file in listdir(files_path) if file and isfile(join(files_path, file)) and splitext(file)[1] == '']
files = sorted(onlyfiles)

if len(files) == 0:
    send_message_and_exit("There is no dump file on path '" + files_path + "'.")



product_ids = []
amount_per_file = 0

print('======================= Looking =======================')
for w in range(len(match_words)):
    for i in range(len(files)):
        print('|>>>> looking on:', files[i], 'for:', match_words[w])
        with open(files_path + files[i]) as f:
            line = f.readline()
            while line:
                data = json.loads(line)
                if re.search(match_words[w], data['name'], re.IGNORECASE):
                    amount_per_file += 1
                    product_ids.append({
                        'id': data['id'],
                        'name': data['name']
                    })
                line = f.readline()
        print('|-------- founded:', amount_per_file)
        amount_per_file = 0

print('======================= Finished! =======================')

if len(product_ids) == 0:
    send_message_and_exit("No product founded.")

print('Max quantity founded:', len(product_ids))

with open(apiKey + '_products_ids_match.csv', 'w') as csv_file:
    fieldnames = ['id', 'name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for founded_id in product_ids:
        writer.writerow(founded_id)





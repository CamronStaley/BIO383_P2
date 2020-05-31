import computation
import os
import display

query = 'C:/Users/econw/Documents/biotest/SARS-CoV-2.fasta'
data_dir = 'C:/Users/econw/Documents/biotest/data'
curr_dir = 'C:/Users/econw/Documents/biotest'

for file in os.listdir('C:/Users/econw/Documents/biotest'):
    if 'results.txt' in file or '.ndb' in file or '.nhr' in file or '.nsq' in file or '.not' in file or \
            '.nto' in file or '.ntf' in file or '.nin' in file:
        os.remove(file)

for file in os.listdir(data_dir):
    if 'results.txt' not in file:
        print(file)
        computation.compare(query, file)


display.display_results(curr_dir)

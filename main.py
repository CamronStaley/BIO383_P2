import computation
import os


query = 'C:/Users/camro/PycharmProjects/BIO383_P2/COVID19.fasta'
directory = 'C:/Users/camro/PycharmProjects/BIO383_P2/data'
for file in os.listdir(directory):
    if 'results.txt' not in file:
        print(file)
        computation.compare(query, file)

import os

curr_dir = 'C:/Users/camro/PycharmProjects/BIO383_P2'

def compare_dir(file, directory):
    this_path = curr_dir + '/' + directory + '/' + file
    for filename in os.listdir(directory):
        other_path = curr_dir + '/' + directory + '/' + filename
        os.system('blastn -query ' + this_path + ' -subject ' + other_path + ' -task blastn -max_hsps 2 -outfmt 6 >> '
                                                                             'file_results.txt')

import csv
#from cards.cardapp.models import CardCategory, Word
category_count = 1
word_count = 0
with open('/Users/sahildeswal/Documents/wordlist.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    for line in reader:
        print '//'.join(line)
        word_count += 1
        if(word_count < 100):
            print category_count

        else:
            word_count = 0
            category_count += 1
            print category_count





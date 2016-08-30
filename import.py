import sys
import os
import django
sys.path.append('/Users/sahildeswal/.virtualenvs/cat/project/cards')
os.environ["DJANGO_SETTINGS_MODULE"] = "cards.settings"
django.setup()
import csv
from cardapp.models import CardCategory, Word
category_count = 1
word_count = 0

with open('/Users/sahildeswal/Documents/wordlist.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quotechar='|')
    for line in reader:
        curr_line = '//'.join(line)
        array = curr_line.split("//")
        word_count += 1
        if(word_count < 100):
            CardCateg = CardCategory.objects.get(pk=category_count)
            if(len(array)==2):
                word = Word.objects.create(category=CardCateg, word = array[0], meaning=array[1])
                word.save()
                print word
                print category_count
        else:
            word_count = 0
            category_count += 1
            categ = CardCategory(category=category_count)
            categ.save()
            word = Word.objects.create(category = categ, word = array[0], meaning=array[1])
            print category_count

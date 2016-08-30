from model import CsvModel

class MyCsvModel(CsvModel):

    class Meta:
        delimiter = ","

my_csv_list = MyCsvModel.import_data(data = open('/Users/sahildeswal/Documents/wordlist.csv'))
first_line = my_csv_list[0]
print first_line.word + ', ' + first_line.meaning

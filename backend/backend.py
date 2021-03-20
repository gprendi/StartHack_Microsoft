
import csv
import json
class Datasets():
    def __init__(self):
        #Create the Dictionaries for python
        baseDataset = {}
        symptom_description = {}
        symptom_precaution = {}



        with open('datasets/dataset.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                
                loaded_line= list(line)
                key = loaded_line[0]
                for i in range(1,len(loaded_line)):
                    if loaded_line[i] !='':
                        try:
                            baseDataset[key].append(loaded_line[i])
                        except:
                            baseDataset[key]=[]
                            baseDataset[key].append(loaded_line[i])

        


if __name__ == "__main__":
    cd = Datasets()


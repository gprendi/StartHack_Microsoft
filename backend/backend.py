
import csv
import json
class Datasets():

     #Create the Dictionaries for python
    def __init__(self):
        #Create the Dictionaries for python
        self.baseDataset = {}
        self.symptom_severity = {}
        self.symptom_precautions = {}
        with open('../datasets/dataset.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                already_added = []
                loaded_line= list(line)
                key = loaded_line[0]
                if key not in already_added:
                    for i in range(1,len(loaded_line)):
                        if loaded_line[i] !='':
                            try:
                                self.baseDataset[key].append(loaded_line[i])
                            except:
                                self.baseDataset[key]=[]
                                self.baseDataset[key].append(loaded_line[i])
                                already_added.append(key)

        
        with open('../datasets/symptom_precaution.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:

                loaded_line = list(line)
                key = loaded_line[0]
                for i in range(1, len(loaded_line)):
                    if loaded_line[i] !='':
                        try:
                            self.symptom_precautions[key].append(loaded_line[i])
                        except:
                            self.symptom_precautions[key]=[]
                            self.symptom_precautions[key].append(loaded_line[i])


        with open('../datasets/Symptom-severity.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                loaded_line=list(line)
                self.symptom_severity[loaded_line[0].replace('_',' ')] = loaded_line[1]
                                   
                
                
if __name__ == "__main__":
    cd = Datasets()
    

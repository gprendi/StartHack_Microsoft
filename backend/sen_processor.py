


''' Data Preprocessing '''

from matplotlib.pyplot import phase_spectrum
import numpy as np
import pandas as pd


class Datasets():

    

    def __init__(self):
        self.PUNCTUATION = '.,;:"\'?!'
        self.dataset = pd.read_csv("datasets/dataset.csv")
        self.symptom_severity = pd.read_csv("datasets/Symptom-severity.csv")
        self.precautions = pd.read_csv("datasets/symptom_precaution.csv")


    def calc_symptoms(self):
        self.symptoms = [i.replace("_", " ") for i in self.symptom_severity.iloc[:,0]]
        self.weights = [i for i in self.symptom_severity.iloc[:,1]]

        self.sym_weight = {
                self.symptoms[i]:self.weights[i] for i in range(len(self.symptoms))
            }

    def calc_score(self, text):
        self.keywords = []
        sentence = ""
        sentences = [] 
        for i in text:
            sentence += i
            if i == ".":
                sentences.append(sentence)
                sentence = ""

        words = []
        for s in sentences:
            if s in self.PUNCTUATION:
                s = s.replace(s,' ')
            words.extend(s.split())

        sym = self.symptoms
        for s in sym:
            block = s.split()
            
            block_size = len(block)                   

            score = 0
            i = 0
            
            for w in words:
                if w == block[i]:
                    score += 1
                    if i < block_size - 1:
                        i += 1
                    
                elif score == block_size:
                    if not(s in self.keywords):
                        self.keywords.append(s)
                    score = 0
                    i = 0
           
        return self.keywords

def process_text(text):
    dt = Datasets()
    dt.calc_symptoms()
    keywords = dt.calc_score(text)
    print(keywords)
    return keywords

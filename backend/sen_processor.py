


''' Data Preprocessing '''

from matplotlib.pyplot import phase_spectrum
import numpy as np
import pandas as pd

class Datasets():

    def __init__(self):
        self.dataset = pd.read_csv("../datasets/dataset.csv")
        self.symptom_severity = pd.read_csv("../datasets/Symptom-severity.csv")
        self.precautions = pd.read_csv("../datasets/symptom_precaution.csv")


    def calc_symptoms(self):
        self.symptoms = [i.replace("_", " ") for i in self.symptom_severity.iloc[:,0]]
        self.weights = [i for i in self.symptom_severity.iloc[:,1]]

        self.sym_weight = {
                self.symptoms[i]:self.weights[i] for i in range(len(self.symptoms))
            }

    def calc_score(self, text): 
        for i in text:
            sentence += i
            if i == ".":
                sentences.append(sentence)
                sentence = ""

        #TODO find keywords
        for s in sentences:
            s = s.replace(".", " ")
            s = s.replace(",", " ")
            words = s.split()


            phrase = ""
            for w in words:
                phrase += w
                if w in self.symptoms:
                    self.keywords.append(w)
                    phrase = ""

                elif phrase in self.symptoms:
                    self.keywords.append(phrase)
                    phrase = ""

                print(phrase)
                phrase += " "

        return self.keywords

def process_text(text):
    dt = Datasets()
    dt.calc_symptoms()
    keywords = dt.calc_score(text)

    return keywords

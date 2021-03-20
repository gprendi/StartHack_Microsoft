


''' Data Preprocessing '''

import numpy as np
import pandas as pd

class Datasets():

    def __init__(self):
        self.dataset = pd.read_csv("../datasets/dataset.csv")
        self.symptom_severity = pd.read_csv("../datasets/Symptom-severity.csv")
        self.precautions = pd.read_csv("../datasets/symptom_precaution.csv")


    def calc_symptoms(self):
        self.symptoms = self.symptom_severity.loc[:, "Symptom"]
        self.weights = self.symptom_severity.loc[:, "weight"]

        for s in range(len(self.symptoms)):
            self.symptoms[s] = self.symptoms[s].replace("_", " ")

        self.sym_weight = {
                self.symptoms[i]:self.weights[i] for i in range(len(self.symptoms))
            }

    def calc_score(self, text):
        text_end = False
        self.keywords = []
        
        sentences = []

        sentence = ""
        for i in text:
            sentence += i
            if i == ".":
                sentences.append(sentence)
                sentence = ""

        word = ""
        for s in sentences:
            for w in s:
                word += w
                if w == " ":
                    if "itching" in self.symptoms:
                        self.keywords.append(itching)
                        word = ""

        return self.keywords


dt = Datasets()
dt.calc_symptoms()
print(dt.symptoms)
print("=====================================")
print(dt.calc_score("itching and swollen_legs are good for the health. geri. ola."))


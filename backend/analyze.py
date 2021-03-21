import numpy as np
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier


# datasets

df = pd.read_csv('datasets/dataset.csv')
df1 = pd.read_csv('datasets/Symptom-severity.csv')
df2 = pd.read_csv('datasets/symptom_Description.csv')
df3 = pd.read_csv('datasets/symptom_precaution.csv')


def train():
    cols = [i for i in df.iloc[:,1:].columns]
    # diseases = df['Disease'].unique()
    
    # ttttttt
    # get the rows
    # create the table
    # 
    # temporary
    tmp = pd.melt(df.reset_index() ,id_vars = ['index'], value_vars = cols )
    tmp['add1'] = 1

    # diseases table
    diseases = pd.pivot_table(tmp, 
                            values = 'add1',
                            index = 'index',
                            columns = 'value')

    # Add labels column
    diseases.insert(0,'label',df['Disease'])


    # Fill NaN with zero
    diseases = diseases.fillna(0)

    ds_train = diseases.sample(frac = 0.7, random_state = 1)
    ds_test = diseases.drop(index = ds_train.index)

    x_train =  ds_train.drop('label', axis = 1)
    y_train =  ds_train['label']


    x_test  =  ds_test.drop('label', axis = 1)
    y_test  =  ds_test['label']
                                    
    # 
    pd.crosstab(ds_train['label'], columns = 'n')
    pd.crosstab(ds_test['label'], columns = 'n')

    # 
    rfc = RandomForestClassifier()
    rfc.fit(x_train, y_train)
    return rfc
    # print(classification_report(y_true=y_test.values, y_pred=result))


# predict
def predict(keywords):
    cols = df1.iloc[1:, 0].unique()
    cols = sorted([i.replace("_", " ") for i in cols])
    vals = []
    append_0 = True
    

    for c in cols:

        for k in keywords:
            if k == c:
                vals.append(1.0)
                append_0 = False
                break
            append_0 = True
        
        if append_0:
            vals.append(0.0)
    
    print(vals)
    pd_cols = df1.iloc[1:, 0].unique()
    pd_cols = sorted([i for i in pd_cols])
    
    
    vals = [vals]           
    output = pd.DataFrame(vals, columns=pd_cols)   
    model = train()
    disease = model.predict(output)

    return disease[0]


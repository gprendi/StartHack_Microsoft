# Start Hack 2021

>
> # Start Hack Microsoft case
>  link : https://github.com/START-Global/Microsoft-STARTHACK21
>

## Group: 0x00000002
## Members:
    1. Gerald Prendi
    2  Eduardo Salvioni

## Goal:
    1. Simplify medical reports, to the point that they accessible to anyone.
    2. Analyze data from the report, and output to the user in simple and summarized way

## Abstract
_________________________________________________________________________________
Our idea about the project, was to create a WebApp using Python's Flask module, that would take the pdf, txt or an image file from the user. <br>
Then we would read throghout the diagnosis, and select some keywords, compare them to the a list of symptoms and output to the user. 
In the middle of this exchange there is a Dictionary  API, where we do the simple lookup of the keywords. <br>
Output given to the users, would be: <br>
    1. the list of keywords <br>
    2. definition of these keywords <br>
    3. precautions that they can follow


## Implementation
________________________________________
We separated our thinking and our program, in modules so it would be easier to work with in parallel and easier to debug.

-> There are 4 parts to the program:
    WebApp          : Frontend, the website that the users interact with
    OCR             : Optical Image Recognition, to scan and read through pdf
    backend         : On the backend we have a model, that based on some weighted symptoms, approximates the disease
    DictionaryAPI   : The dictionary that we fetch the keywords from


## MODEL
__________________________________________

In the backend in analyze.py, there is a model based on RandomForestClassifier will output the disease based on what are the symptoms of the user.
Our datasets have at least 131 symptoms, 5000 user datas, and the precautions for them to follow in case of the disease.
The model takes as input the keywords array, normalizes the inputs ( the array will be an array of [0.0 and 1.0]) and then takes the decision based on previous data fed to the model.

## OCR
__________________________________________
OCR is an implementation of pytesseract, where we read the document,i.e PDF, convert it to images, recognize the text in the images, append all the text together and remove the image.

## WebApp
__________________________________________
A simple development webapp, written in Python using FLask, that is just a simple UI, that is a compound webapp between python and html,css.
![Frontpage](/SH_Microsoft/test_cases/screenshot2.png)


## DICTIONARYAPI
__________________________________________
A medical dictionary, that accepts as input a string, with the keyword, and then returns in .json format the synonyms and an easier explanation of the keyword.

## DEPLOYMENT

Docker container up and running: https://hub.docker.com/repository/docker/gprendi30/easy-med <br>
WebApp deployed at heroku: https://easy-med-shack.herokuapp.com/
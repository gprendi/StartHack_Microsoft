# STARTHACK - Microsoft Case
# Group: 0x00000002

# Members:
     Gerald Prendi,
     Edoardo Salvioni
   
# GOAL:
    Help users read their medical diagnoses, simplifying the medical terms and outputting them to the user
# Our Idea

    1. A simple WebApp written in Flask
    2. Will ask user for input: a text file, a pdf or scan a png
    3. OCR of the input
    4. Process the keywords using our DL
    5. Return a report on the text
    6. Output to the user

# Timing
36 hours in total

    1. Planning: 3 hours
    2. UI + UX: 5 - 6 hours
    3. Backend: 12 hours
       1. Data Collecting
       2. OCR
       3. Text Processing
       4. Output

    4. TimeOff: 8 hours
    5. Testing + Debugging: 3 hours
    6. Presentation: 2 hours


# Deadline 
## 21 March 12 pm

# Progress
    1. Created the idea.
    2. Implemented OCR
    3. Flask WebApp up and running
    4. Dictionary API
    5. DL model
    6. Keywords selection
    7. Putting the modules together
    8. Running the webapp

# Install
    git clone https://github.com/GPrendi30/SH_Microsoft
    cd SH_Microsoft
    python3 -m venv .env
    source .env/bin/activate
    pip install -r requirements
    python3 main.py

You are ready to go.

# Sources

https://www.kaggle.com/itachi9604/disease-symptom-description-dataset

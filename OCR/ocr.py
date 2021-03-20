

from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 

outfile = "raw_out.txt"
def OCR_PDF(pdf_path):
    # Path of the pdf 
    PDF_file = pdf_path
    
    ''' 
    Part #1 : Converting PDF to images 
    '''
    
    # Store all the pages of the PDF in a variable 
    pages = convert_from_path(PDF_file, 500) 
    
    # Counter to store images of each page of PDF to image 
    image_counter = 1
    
    # Iterate through all the pages stored above 
    for page in pages: 
    
        # PDF page n -> page_n.jpg 
        filename = "page_"+str(image_counter)+".jpg"
        
        # Save the image of the page in system 
        page.save(filename, 'JPEG') 
    
        # Increment the counter to update filename 
        image_counter = image_counter + 1
    
    ''' 
    Part #2 - Recognizing text from the images using OCR 
    '''
    # Variable to get count of total number of pages 
    filelimit = image_counter-1
    
    # Open in append mode
    f = open(outfile, "a") 

    # loop through the images
    for i in range(1, filelimit + 1): 
    
        # Set filename to recognize text from 
        filename = "page_"+str(i)+".jpg"
            
        # Recognize the text as string in image using pytesserct 
        text = str(((pytesseract.image_to_string(Image.open(filename))))) 
    
        text = text.replace('-\n', '')     
        
        # Finally, write the processed text to the file. 
        f.write(text) 


        os.remove(filename)

    # Close the file after writing all the text. 
    f.close()


def OCR_image(image_path):
    image_file = image_path

    # opening the output file, in append mode
    f = open(outfile, "a") 

    # converting the image text to string
    text = str(((pytesseract.image_to_string(Image.open(image_file)))))

    text = text.replace('-\n', '')

    # writing the text to the file.
    f.write(text)

    # closing the output file
    f.close()

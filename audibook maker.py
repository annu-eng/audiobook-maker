import pyttsx3

import PyPDF2               #Its a python library built as a PDF toolkit
name=str(input('what is the name of your pdf ? '))    
book=open(name+'.pdf','rb')    #name of the pdf is concatenated with '.pdf' extension and given as input.
                             #"rb" mode opens the pdf file in binary format for reading, 

pdfReader = PyPDF2.PdfFileReader(book)  #to read from the pdf

pages=pdfReader.numPages   # Gets total number of pages in that pdf
 
speaker = pyttsx3.init()    

pgn=int(input('enter the page number from where you want to read. ')) 

for num in range(pgn,pages):     #for loop is used to read entire book/part of it,without it only a single page can be read.

    page =pdfReader.getPage(num)    # gets the first from where we want to read the pdf

    text=page.extractText()         # extracts text from the page selected

    speaker.say(text)               # makes the text extracted audible

    speaker.runAndWait()

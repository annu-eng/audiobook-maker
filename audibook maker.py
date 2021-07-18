import pyttsx3
import PyPDF2
book=open('BUKKI.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
pgn=int(input('enter the page number from where you want to read. ')) #enter page number from where you want to read
for num in range(pgn,pages):     #for loop is used to read entire book/part of it,without it only a single page can be read.
    page =pdfReader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()
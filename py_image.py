# import the following libraries 
# will convert the image to text string 
import pytesseract       
pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' 
# adds image processing capabilities 
from PIL import Image   

#translator
from googletrans import Translator
   
trans = Translator() 
 # opening an image from the source path 
img = Image.open('german.jpg')     

text = pytesseract.image_to_string(img)

print(text) 
print("----------------------------")
# converts the image to result and saves it into result variable 
result = trans.translate(text,dest="english") 
# write text in a text file and save it to source path    

print(result.text)
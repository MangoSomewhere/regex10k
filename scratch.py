import os
import pdfplumber
import re


def extract_name():
    os.chdir('/Users/drew/Desktop/pythonProject/regex10k/example')
    test = os.listdir('/Users/drew/Desktop/pythonProject/regex10k/example')

    for file in test:
        if file.endswith('.pdf'):
            result = ''
            with pdfplumber.open(file) as pdf:
                firstPage = pdf.pages[0]
                text = firstPage.extract_text()
                result = text

            companyNameSO = re.compile(r'(\w*) ?(\w*) (CO\.|CORPORATION|INC\.)')

            mo = companyNameSO.search(result)

            print(mo)


extract_name()






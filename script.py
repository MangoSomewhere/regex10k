
import pdfplumber

import os
import re



def extract_whole():
    os.chdir('/Users/drew/Desktop/pythonProject/regex10k/example')

    test = os.listdir('/Users/drew/Desktop/pythonProject/regex10k/example')

    for file in test:
        with pdfplumber.open(file) as pdf:
            firstPage = pdf.pages[0]
            text = firstPage.extract_text()
            result = text

        companyNameSO = re.compile(r'(\w*) ?(\w*) (CO\.|CORPORATION|INC\.)')

        mo = companyNameSO.search(result)

        print(mo)
        # open each file as the pdf var
        with pdfplumber.open(file) as pdf:
            # stores max number of pages within var
            all_pages = len(pdf.pages)
            # loop through the entire document to extract data from pages and store within var result
            result = ''
            for page in range(all_pages):
                data = pdf.pages[page].extract_text()
                data.split('\n')
                result = result + '\n' + data

    # close pdf to make room for another
    pdf.close()


extract_whole()

# if page.startswith('Unaudited Consolidated Balance Sheets'):
'''
for row in text.split('\n'):
    if row.startswith('Cash and cash equivalents'):
        cash2020 = row.split()[-1]
        cash2019 = row.split()[-2]
        cash2018 = row.split()[-3]
'''











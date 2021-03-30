
import pdfplumber

import os

os.chdir('/Users/drew/Desktop/pythonProject/regex10k/example')

test = os.listdir('/Users/drew/Desktop/pythonProject/regex10k/example')
print(test)
def extract_whole():



    for files in test:
        # open each file as the pdf var
        with pdfplumber.open(files) as pdf:
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











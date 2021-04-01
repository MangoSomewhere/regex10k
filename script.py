
import pdfplumber
import csv
import os
import re



def extract_whole():
    os.chdir('/Users/drew/Desktop/pythonProject/regex10k/example')
    test = os.listdir('/Users/drew/Desktop/pythonProject/regex10k/example')
    csv_fields = ['Company Name']
    with open('10kcsv.txt', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_fields)
        csv_file.close()
    for file in test:
        if file.endswith('.pdf'):
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
                so_coname = re.compile(r'(\w*) ?(\w*) (CO\.|CORPORATION|INC\.)')
                mo_coname = so_coname.search(result)
                row = [mo_coname]
                rows.append(row)
                rows = []
            pdf.close()

    with open('10kcsv.txt', mode='w') as csv_file:
        csv_writer.writerow(rows)
    csv_file.close()


extract_whole()












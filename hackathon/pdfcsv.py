pdffiletouse = 'Lecture_Schedule2.pdf'
import csv
import pandas as pd

columns = [('Subject', 'Start  Date', 'Start Time', 'End Date', 'End Time', 'All day event', 'Description', 'Location', 'Private')]
import csv
f = open('nameu.csv', 'w', newline='')
a = csv.writer(f)
a.writerow(columns[0]) 


with open('finaldateouput.txt', 'r') as f:
    for line in f.readlines():
        a.writerow((pdffiletouse,line,'',line,'','','','','','' )) 
f.close()
import requests
from bs4 import BeautifulSoup
import xlsxwriter

url = "user-html-page-data.xlsx"
response = requests.get(url)
html = response.content
html = html.decode('ascii', 'ignore')
soup = BeautifulSoup(html, "html.parser")

workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 0
for rec_date, rec_type, doc_num in zip(soup.select('table#datatable > tbody > tr > td:nth-child(4)'),
                                       soup.select('table#datatable > tbody > tr > td:nth-child(5)'),
                                       soup.select('table#datatable > tbody > tr > td:nth-child(6)')):
    worksheet.write(row, column, rec_date.text)
    worksheet.write(row, column + 1, rec_type.text)
    row += 1
workbook.close()

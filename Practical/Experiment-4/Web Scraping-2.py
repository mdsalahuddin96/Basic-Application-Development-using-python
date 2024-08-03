import requests
from bs4 import BeautifulSoup
import xlsxwriter

COLUMN_NAMES = ("Book title","Author")# excel header(first row)

# Capture article response
content = requests.get("http://www.worldswithoutend.com/lists_sf_masterworks.asp")

# Parse website HTML
soup = BeautifulSoup(content.text,"html.parser")
book_titles = soup.find_all("p",{"class": "title"})
book_authors = soup.find_all("p",{"class": "author"})

workbook = xlsxwriter. Workbook("SF Masterworks.xlsx")
worksheet = workbook.add_worksheet()

for index, column in enumerate(COLUMN_NAMES):
    worksheet.write(0, index , column)
row_index = 1
for book in book_titles:
    book = book.get_text()
    book = book.title()
    worksheet.write(row_index, 0, book)
    row_index += 1

row_index = 1
for author in book_authors:
    author = author.get_text()
    author = author.title()
    worksheet.write(row_index, 1, author)
    row_index += 1
workbook.close()

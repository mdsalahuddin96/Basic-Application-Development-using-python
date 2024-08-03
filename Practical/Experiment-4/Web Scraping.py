# import web grabbing client and
# HTML parser
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# variable to store website link as string
myurl = 'http://books.toscrape.com/index.html'

# grab website and store in variable uclient
uClient = uReq(myurl)

# read and close HTML
page_html = uClient.read()
uClient.close()

# call BeautifulSoup for parsing
page_soup = soup(page_html, "html.parser")

# grabs all the products under list tag
bookshelf = page_soup.findAll(
	"li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

# create csv file of all products
filename = ("Booklistandprice.csv")
f = open(filename, "w")

headers = "Book title, Price\n"
f.write(headers)

for books in bookshelf:

	# collect title of all books
	book_title = books.h3.a["title"]

	# collect book price of all books
	book_price = books.findAll("p", {"class": "price_color"})
	price = book_price[0].text.strip()

	print("Title of the book :" + book_title)
	print("Price of the book :" + price)

	f.write(book_title + "," + price+"\n")

f.close()

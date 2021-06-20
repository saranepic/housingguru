from selenium import webdriver
import csv
from bs4 import BeautifulSoup

# I always use request to extract news, but overhere I used selenium because using request I wasn't able to extract details.
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi")
element = driver.page_source
b = BeautifulSoup(element, 'html.parser')

# eclsred 3 variables price,location,housedetails.
price = b.select('.price')
location = b.select('.filter-pro-heading')
housedetails = b.select('.filter-pro-details')

# details a list to store all the values.
details = []
for i in range(len(price)):
    finalprice = price[i].getText()
    finallocation = location[i].getText()
    finalhousedetails = housedetails[i].getText()

    # cleaning the extracted details only for this particular thing.
    finalhousedetails1 = finalhousedetails.replace('\n', ' ')

    # I stored all these details in the form of dictionary inside the list.
    case = {'price': finalprice, 'location': finallocation,
            'house-details': finalhousedetails1}
    details.append(case)

# declaring feild name for the csv file.
fields = ['location', 'price', 'house-details']
filename = "housing.csv"

with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(details)
    print(f"Uploaded successfully into {filename}")

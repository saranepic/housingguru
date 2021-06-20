from selenium import webdriver
import csv
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi")
# selecting the BHK button using class name
maindropdown = driver.find_element_by_class_name('bedroomdropdown')
maindropdown.click()

# selecting the 3 bedroom houses using xpath
threebedroombutton = driver.find_element_by_xpath(
    '//*[@id="navbarNavDropdown"]/ul[1]/li[3]/ul/li/div/ul/li[3]/label')
threebedroombutton.click()

# selecting the 4 bedroom houses using xpath
fourbedroombutton = driver.find_element_by_xpath(
    '//*[@id="navbarNavDropdown"]/ul[1]/li[3]/ul/li/div/ul/li[4]/label')
fourbedroombutton.click()

# using time.sleep for 10 sec. The crawler has to wait for 10 sec to get the updated details.
time.sleep(10)

# Extracting the details using Beautiful soup.
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
filename = "3_4_bedroomhousing.csv"

with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(details)
    print(f"Uploaded successfully into {filename}")

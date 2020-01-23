import requests
from bs4 import BeautifulSoup
import time
#Imports the Mail_Bot function from a different project
from Email_Bot import Mail_Bot


# Enter the URL for the Amazon Product whose price you wish to track

URL = 'https://www.amazon.com/Apple-MWP22AM-A-AirPods-Pro/dp/B07ZPC9QD4/ref=sr_1_1_s' \
      'spa?crid=2RLCPMC9DXISA&keywords=airpods+pro&qid=1579226272&sprefix=air%2Caps%2C216&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVk' \
      'UXVhbGlmaWVyPUExMlRQSFBPRDBEM1IwJmVuY3J5cHRlZElkPUExMDQ3MDU1MjJRUUZKVExaMFFSNCZlbmNyeXB0ZWRBZElkPUEwMDA1NDE0M1JFWVNXODNIVV' \
      'pCMyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

#Enter User-Agent by Googling "What is my User Agent"

headers = {"User-Agent":
'#Enter User-Agent'}

#Function to check the price of an Amazon project by:
#Gathering the elements from the page
#From that element it sorts through for specific ids and then labels them accordingly

def Check_price(price_to_fall):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # Find the Product's Name
    title = soup.find(id="productTitle").get_text()

    # #Returns the current price of the product
    price = soup.find(id="priceblock_ourprice").get_text()

    # Converts the Price from a string to a float value
    converted_price = float(price[1:4])

    # When the price of the product is below or at the price you wish to buy the product at:
    #     An email will be sent to you telling you the current price along with a link to the email
    while(converted_price <= price_to_fall):

        if converted_price <= price_to_fall:
            Mail_Bot(title.strip() + ' Price has fallen!',
                   'The price of: ' + title.strip() +
                   ' has fallen to a price of: ' + '$' + str(price) + " Buy at:" + '\n\n' + URL,
                   '#Receiving Email')
            break
    while(converted_price > price_to_fall):
        print('Price has not fallen below ' + str(price_to_fall) + ', will check again tommorow')
        time.sleep(84000)



Check_price(200.00)

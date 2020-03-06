import time

# Needed to request the page's content
import requests

# Used to sort the page content for specific information
from bs4 import BeautifulSoup

# Imports the Mail_Bot function from a different project
from Email_Bot import Mail_Bot

URL = input('Please enter the URL of the item you wish to track: ')

try:
    price_track = float(input('What price would you like to be notified at? '))

except ValueError:
    print('Please enter a number')
    price_track = float(input('What price would you like to be emailed at?'))

email_response = input('Would you like to be emailed if the price falls below your target? [y/n]')

if email_response is 'y':
    email_given = input('Please enter your email: ')
else:
    email_given = None

# Enter User-Agent by Googling "What is my User Agent"

headers = {"User-Agent":
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit'
               '/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

# Function to check the price of an Amazon project by:
# Gathering the elements from the page
# From that element it sorts through for specific ids and then labels them accordingly

def check_Price(price_to_fall, email):
    print('Checking price...')

    # Requests the pages to be sorted by BeautifulSoup
    page = requests.get(URL, headers=headers)

    # Stores the content of the page into the variable named 'soup'
    soup = BeautifulSoup(page.content, 'lxml')

    # Searches the variable soup to find the Products Name
    title = soup.find(id="productTitle").get_text()

    # Searches the variable soup to find the current price of the item
    # .get_text() is simply to remove all white spaces that was created when pulling the data
    # If the first id doesn't exist, then it means the item is on sale
    # So it begins to check for that second id
    if 'amazon' in URL:
        try:
            price = soup.find(id="priceblock_ourprice").get_text()
        except AttributeError:
            price = soup.find(id="priceblock_dealprice").get_text()

    # Converts the Price from a string to a float value so that it can be used to
    # compare data

    converted_price = float(price[1:4])

    # When the price of the product is below or at the price you wish to buy the product at:
    # An email will be sent to you telling you the current price along with a link to the email
    # It's in a while loop to allow for it to continually run in the background without
    # The user having to check on it
    # Once an email is sent, the loop will break and will have to be rerun to track the price again
    # If the price didn't fall below the desired price:
    # The program sleeps for 43200 seconds, approximately half a day and then checks again
    # Repeating the process until the price has fallen

    while converted_price <= price_to_fall:

        if converted_price <= price_to_fall:
            if email_response is 'y':
                Mail_Bot(email, title.strip() + ' Price has fallen!',
                         'The price of {} has fallen to a price of {} '
                         '\n Your target price was originally: ${} \n ' \
                         'Buy now at: \n {}'
                         .format(title.strip(), price, price_track, URL))
            elif email_response is 'n':
                print('The current price is ${}'.format(converted_price))
        break

    while converted_price > price_to_fall:
        print('Price has not fallen below ${}, '
              'will check again tomorrow. '
              'Price is currently ${}'.format(price_to_fall, price))
        time.sleep(43200)
        check_Price(price_track, email)


if __name__ == '__main__':
    check_Price(price_track, email_given)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Ensure GUI is off
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)  # Pass the options parameter here
driver.get("https://www.car-part.com/")


def select_radio_button(selected_id):
    radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
    if selected_id.isdigit() and 1 <= int(selected_id) <= len(radio_buttons):
        radio_buttons[int(selected_id) - 1].click()
        radio_buttons[int(selected_id) - 1].send_keys(Keys.TAB)
        radio_buttons[int(selected_id) - 1].send_keys(Keys.ENTER)
    else:
        print("Invalid ID selected.")


def fill_form(driver, year, model, part, loc, sort, yard_zip):
    # Find Year
    search_year = driver.find_element(By.ID, "year")
    search_year.send_keys(year)
    search_year.send_keys(Keys.TAB)
    # Find Model
    search_model = driver.find_element(By.ID, "model")
    search_model.send_keys(model)
    search_model.send_keys(Keys.TAB)
    # Find Part
    search_part = driver.find_element(By.NAME, "userPart")
    search_part.send_keys(part)
    search_part.send_keys(Keys.TAB)
    # Location
    search_loc = driver.find_element(By.ID, "Loc")
    search_loc.send_keys(loc)
    search_loc.send_keys(Keys.TAB)
    # Sort
    search_sort = driver.find_element(By.NAME, "userPreference")
    search_sort.send_keys(sort)
    search_sort.send_keys(Keys.TAB)
    # Zip
    search_zip = driver.find_element(By.NAME, "userZip")
    search_zip.send_keys(yard_zip)
    search_zip.send_keys(Keys.TAB)
    search_zip.send_keys(Keys.TAB)
    search_zip.send_keys(Keys.ENTER)


year = "2005"
model = "Honda Civic"
part = "Engine"
loc = "USA"
sort = "price"
yard_zip = ""

fill_form(driver, year, model, part, loc, sort, yard_zip)

# Wait for the page to load
  # Adjust the sleep time as needed

# Parse the HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all radio buttons and their labels
radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
for i, button in enumerate(radio_buttons):
    label = button.find_element(By.XPATH, "following-sibling::label")
    print(f"{i + 1}. {label.text.strip()}")

# Store the selected_id in a variable
selected_id = input("Enter the ID of the radio button you want to select: ")

# Define a function to select a radio button

select_radio_button(selected_id)
soup = BeautifulSoup(driver.page_source, 'html.parser')


driver = webdriver.Chrome(service=service)



def all_foreign(driver, year, model, part, loc, sort, yard_zip, selected_id):

    # Open a new tab
    # driver.execute_script("window.open('');")
    # Switch to the new tab (assuming it is the next one)
    # driver.switch_to.window(driver.window_handles[-1])
    # Navigate to the website
    driver.get("https://www.car-part.com/")
    # Fill the form with the provided details but with zip as 12345
    fill_form(driver, year, model, part, loc, "zip", "15201")
    # Wait for the page to load
    time.sleep(3)
    # Adjust the sleep time as needed
    # Select the radio button
    select_radio_button(selected_id)
    # Uncomment this line
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # # Find all tables

    tables = soup.find_all('table')

    # # Select the second table and find all rows in it
    rows = tables[4].find_all('tr')


    for row in rows:
        # Get all columns in the row
        cols = row.find_all('td')

        # If "Dist mile" is 0
        # All Foreign Auto Parts
        # if stock no. has alphabets ignore
        if cols and cols[-1].text.strip() == '0':
            stock = cols[4].text.strip()
            if not any(char.isalpha() for char in stock):  # Check if 'Stock#' contains any alphabets
                # Print Year, Part, Model, Description, Miles, Part Grade, Stock#, US Price, Dealer Info
                print('Year, Part, Model:', cols[0].text.strip())
                print('Description:', cols[1].text.strip())
                print('Miles:', cols[2].text.strip())
                print('Part Grade:', cols[3].text.strip())
                print('Stock#:', stock)
                print('US Price:', cols[5].text.strip())
                dealer_info = cols[6].text.strip()
                print('Dealer Info:', dealer_info[:60])  # Limit dealer info to 60 characters

all_foreign(driver, year, model, part, loc, sort, yard_zip, selected_id)

def a_1_auto(driver, year, model, part, loc, sort, yard_zip, selected_id):

    # Open a new tab
    # driver.execute_script("window.open('');")
    # Switch to the new tab (assuming it is the next one)
    # driver.switch_to.window(driver.window_handles[-1])
    # Navigate to the website
    driver.get("https://www.car-part.com/")
    # Fill the form with the provided details but with zip as 11111
    fill_form(driver, year, model, part, loc, "zip", "89011")
    # Wait for the page to load
    time.sleep(3)
    # Adjust the sleep time as needed
    # Select the radio button
    select_radio_button(selected_id)
    # Uncomment this line
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # # Find all tables

    tables = soup.find_all('table')

    # # Select the second table and find all rows in it
    rows = tables[4].find_all('tr')


    for row in rows:
        # Get all columns in the row
        cols = row.find_all('td')

        # If "Dist mile" is 0
        # All Foreign Auto Parts
        # if stock no. has alphabets ignore
        if cols and cols[-1].text.strip() == '0':
            # Print Year, Part, Model, Description, Miles, Part Grade, Stock#, US Price, Dealer Info
            print('Year, Part, Model:', cols[0].text.strip())
            print('Description:', cols[1].text.strip())
            print('Miles:', cols[2].text.strip())
            print('Part Grade:', cols[3].text.strip())
            print('Stock#:', cols[4].text.strip())
            print('US Price:', cols[5].text.strip())
            dealer_info = cols[6].text.strip()
            print('Dealer Info:', dealer_info[:60])  # Limit dealer info to 60 characters

a_1_auto(driver, year, model, part, loc, sort, yard_zip, selected_id)



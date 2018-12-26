import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# grab the url as the first command line argument
_id = input('Enter a url id\n')
url = "https://www.youtube.com/watch?v=" + _id

# create a Chrome browser
options = Options()
opt_args = ['--headless', '--disable-gpu', 'start-maximized', 'disable-infobars',
            "--disable-extensions", "--enable-javascript", '--window-size=1420,1080']
for i in opt_args:
    options.add_argument(i)
driver = webdriver.Chrome('utilities/chromedriver.exe', chrome_options=options)

# open the url from the command line
driver.get(url)

# scroll to the bottom in order to load the comments
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(3)

# wait for the comments to load
while True:
    # if comments load, then break out of the while loop
    try:
        driver.find_element_by_id("content-text")
        break
    # otherwise, sleep for three seconds and try again
    except:
        time.sleep(2)
        continue

# print the comments, separated by a line and store them in a list
lst_comments = []
for item in driver.find_elements_by_id("content-text"):
    lst_comments.append(item.text)

print('\n'.join(lst_comments))
# close the browser
driver.close()

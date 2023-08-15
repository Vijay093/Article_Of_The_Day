from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common .by import By
from smtplib import SMTP

options = Options()
options.add_argument('--headless=new')

my_email = ""
my_password = ""

driver = webdriver.Chrome(options=options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_content = driver.find_element(By.CSS_SELECTOR, "#mp-tfa p")
links = driver.find_elements(By.CSS_SELECTOR, "#mp-tfa p b a")
link = links[-1].get_attribute('href')
content = article_content.text
# print(article_content.text)
# print(link)

with SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg=f"Subject: Today's Featured Article\n\n{content} {link}")

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

article_content = driver.find_element(By.XPATH, '//*[@id="mp-tfa"]')
link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Full article')
link = link.get_attribute('href')
content = article_content.text
# print(article_content.text)
# print(link)
content = content[:600]+"..."

with SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg=f"Subject: Today's Featured Article\n\n{content} {link}")

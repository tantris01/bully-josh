from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import environ
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def obfuscate_quote():
    url = 'https://lingojam.com/PigLatinTranslator'
    #setting up headless chrome browser
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    #getting html and finding all ads
    soup = BeautifulSoup(driver.page_source,'html.parser')



with open('beemovie.txt') as beetext:
    lines = beetext.read().split('\n')
    final_lines = []
    for i in range(len(lines)):
        if lines[i] != '' and lines[i] != '  ':
            final_lines += [lines[i]]


#obfuscate_quote()

# def email():

#     subject = 

#     #creating message and sending
#     message = Mail(from_email = environ['MAIL_DEFAULT_SENDER'], to_emails=environ['MAIL_DEFAULT_SENDER'], subject = subject, plain_text_content=)
#     sg = SendGridAPIClient(environ['SENDGRID_API_KEY'])
#     sg.send(message)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import environ
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# # Log the user in
# session = fbchat.Session.login(environ['EMAIL'], environ['PASSWORD'])


# # Send a message to yourself
# session.user.send_text("Hi me!")

# # Log the user out
# session.logout()

def obfuscate_quote():
    url = 'https://translate.google.com/'
    #setting up headless chrome browser
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(options=options,executable_path='bully-josh//chromedriver_win32//chromedriver.exe')
    driver.get(url)

    #getting html and finding all ads
    soup = BeautifulSoup(driver.page_source,'html.parser')
    print(soup)

obfuscate_quote()

# def email():

#     subject = 

#     #creating message and sending
#     message = Mail(from_email = environ['MAIL_DEFAULT_SENDER'], to_emails=environ['MAIL_DEFAULT_SENDER'], subject = subject, plain_text_content=)
#     sg = SendGridAPIClient(environ['SENDGRID_API_KEY'])
#     sg.send(message)
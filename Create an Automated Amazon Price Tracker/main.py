from email.message import EmailMessage

from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

smtp_email = os.getenv('SMTP_EMAIL')
smtp_password = os.getenv('SMTP_PASSWORD')
email_address = os.getenv('EMAIL_ADDRESS')

URL = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
headers = {"Accept-Language": "fr-FR,fr;q=0.9",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Safari/605.1.15"}

response = requests.get(URL, headers=headers)
product_webpage = response.text

soup = BeautifulSoup(product_webpage, 'html.parser')
price_eur = soup.select_one(selector=".a-price-whole")
price_cents = soup.select_one(selector=".a-price-fraction")
threshold = 100

print(f"Price of the product: {price_eur.getText()}{price_cents.getText()}")

msg = EmailMessage()
msg['Subject'] = 'Amazon Price Alert'
msg['From'] = smtp_email
msg['To'] = email_address
msg.set_content(f'Alert! your product is now below {threshold}')

smtp_server = 'smtp.gmail.com'
smtp_port = 587

if int(price_eur.getText().replace('.', '')) < threshold:
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_email, smtp_password)
            server.send_message(msg)
            print("Email sent successfully")
    except Exception as e:
        print(f'Failed to send email: {e}')

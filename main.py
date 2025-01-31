import os
from pprint import pprint
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import smtplib

static_url="https://appbrewery.github.io/instant_pot/"
live_url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

load_dotenv()
mail=os.getenv('from_email')
password=os.getenv('app_password')
to_mail=os.getenv('to_addrs')
'''header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 130.0.6723.126) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.126 Safari/537.36"
}'''
header={
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 130.0.6723.126) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.126 Safari/537.36",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
}
response=requests.get(url=live_url,headers=header)
print(response.raise_for_status())
data=response.text

soup=BeautifulSoup(data,'html.parser')
pprint(soup)
price=float(soup.find('span', class_="aok-offscreen").getText().split("$")[1])
Target_price=100.00
if price<Target_price:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=mail,password=password)
        connection.sendmail(from_addr=mail,to_addrs=to_mail,
                            msg=f"Amazon Price Tracker\n current price:{price}\n click here to buy {live_url} ")


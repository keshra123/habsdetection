import requests
import pandas as pd
from datetime import datetime
import random
from time import sleep
from scrapingbee import ScrapingBeeClient

df = pd.read_csv('googlenews2.csv',index_col=0)
df = df.head(1)
#print(df)

client = ScrapingBeeClient(api_key='FQRFGC6SASD9DPDAGQ4LAUSG3JOLGUNH5VPAVO5GJ1IPBHTN1Y4L71FMP1LA275XIG7WHIIB60Y5RIOZ')

results1 = []
timestamp = []
titles = []  
links = []


def instagram(df):
    num = 0
    for link in range(len(df)):
        url = df.iloc[link][0]

        try:
            response = client.get(url,
            params = { 
                'premium_proxy': 'True',
            }
            )
            driver.set_page_load_timeout(30)
            redirect_link = driver.current_url
            sleep(random.randint(10, 30))
        except:
            sleep(60)
        try:
                results = (driver.find_element(By.CSS_SELECTOR,'div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > section > main > div > div._aa6e > article > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.x78zum5.xdt5ytf.x1iyjqo2.xs83m0k.x2lwn1j.x1odjw0f.x1n2onr6.x9ek82g.x6ikm8r.xdj266r.x11i5rnm.x4ii5y1.x1mh8g0r.xexx8yu.x1pi30zi.x18d9i69.x1swvt13 > ul > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xggy1nq.x11njtxf > li > div > div > div._a9zr > div._a9zs > h1').text)
                results1.append(results)
                time = driver.find_element(By.XPATH,'//time[@class="_a9ze _a9zf"]')
                times = time.get_attribute("datetime")
                format_data = "%Y-%m-%dT%H:%M:%S.%fZ"
                new_datetime = datetime.strptime(times, format_data)
                time = new_datetime.strftime("%d %b %Y %H:%M:%S")
                timestamp.append(time)
                titles.append(get_title)
                links.append(redirect_link)
        except:
            print("Error Occured")    
        print(link)
        driver.quit()
        num +=1
        if num == 3: 
            sleep(60)
            num = 0

if __name__ == "__main__":
    instagram(df)
    dict = {'links': links, 'titles': titles, 'texts': results1, 'timestamp':timestamp}
    df = pd.DataFrame(dict)
    df.to_csv('instagram.csv')




print('Response HTTP Status Code: ', response.status_code)
print('Response HTTP Response Body: ', response.content)

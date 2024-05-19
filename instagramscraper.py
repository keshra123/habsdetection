from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options   
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import random
from time import sleep
import concurrent.futures
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium_stealth import stealth

df = pd.read_csv('googlenews2.csv',index_col=0)
df = df.head(10)
#print(df.iloc[1][0])
results1 = []
timestamp = []
titles = []  
links = []

proxies  = [
'192.73.244.36:80',
'12.186.205.120:80',
'104.225.220.233:80',
'50.223.239.185:80',
'50.172.75.127:80',
'50.223.239.166:80',
'50.223.239.167:80',
'50.168.72.116:80',
'50.144.166.226:80',
'50.218.57.67:80',
'50.218.57.68:80',
'50.218.57.70:80',
'50.222.245.42:80',
'50.168.72.112:80',
'50.171.122.30:80',
'12.186.205.122:80',
'50.174.7.158:80',
'50.222.245.50:80',
'50.223.242.97:80',
'50.222.245.46:80',
'50.218.57.65:80',
'50.223.242.103:80',
'50.232.104.86:80'
]
#print(df.to_string())
#proxy_number = random.random() * 9 
def instagram(df):
    """
    results1 = []
    timestamp = []
    titles = []  
    links = []
    """
    proxy_number = int(random.random() * 9)
    for link in range(len(df)):
        opts = Options()
        #opts.add_argument("start-maximized")

        opts.add_argument("--headless")

        opts.add_argument(f'--proxy-server={proxies[proxy_number]}')

        #opts.add_experimental_option("excludeSwitches", ["enable-automation"])
        #opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        #opts.add_experimental_option('useAutomationExtension', False)
        browser = Firefox(opts)
        url = df.iloc[link][0]
        #url = 'https://www.instagram.com/inspectorplanet/reel/C5WwGvruBCh/'
        #url = 'https://www.instagram.com/thesarahpilla/reel/Cy3oI0LpPml/'
        #url = 'https://www.instagram.com/theoaklandside/p/C4RVsw9pwUF/'
        try:
            browser.get(url)
            redirect_link = browser.current_url
            sleep(random.randint(0, 20))
        #if redirect_link.status >= 300:
        except:
            sleep(60)
        try:
            #get_title = browser.title 
            get_title = redirect_link.title
            results = (browser.find_element(By.CSS_SELECTOR,'div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > section > main > div > div._aa6e > article > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.x78zum5.xdt5ytf.x1iyjqo2.xs83m0k.x2lwn1j.x1odjw0f.x1n2onr6.x9ek82g.x6ikm8r.xdj266r.x11i5rnm.x4ii5y1.x1mh8g0r.xexx8yu.x1pi30zi.x18d9i69.x1swvt13 > ul > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xggy1nq.x11njtxf > li > div > div > div._a9zr > div._a9zs > h1').text)
            #results = soup.findAll("p")
            #results2 = soup.findAll("h1")
            results1.append(results)
            #timestamp = (browser.find_element(By.CSS_SELECTOR, 'div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > section > main > div > div._aa6e > article > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > div.x78zum5.xdt5ytf.x1iyjqo2.xs83m0k.x2lwn1j.x1odjw0f.x1n2onr6.x9ek82g.x6ikm8r.xdj266r.x11i5rnm.x4ii5y1.x1mh8g0r.xexx8yu.x1pi30zi.x18d9i69.x1swvt13 > ul > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xggy1nq.x11njtxf > li > div > div > div._a9zr > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1xmf6yo.x12nagc.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > span > time >datetime'),'time._a9ze._a9zf')
            time = browser.find_element(By.XPATH,'//time[@class="_a9ze _a9zf"]')
            times = time.get_attribute("datetime")
            format_data = "%Y-%m-%dT%H:%M:%S.%fZ"
            new_datetime = datetime.strptime(times, format_data)
            time = new_datetime.strftime("%d %b %Y %H:%M:%S")
            #times.strftime('%d %b %Y %H:%M:%S')
            #times = datetime.strptime(times,'%Y %b %d %H:%M:%S')
            timestamp.append(time)
            #timestamp.append(time.get_attribute("datetime"))
            titles.append(get_title)
            links.append(redirect_link)
        except:
            print("Error Occured")
        browser.quit()
    browser.close()
    #titles.append(browser.find_element(By.XPATH,'/html/head/meta[24]').text)
    #results1 =[results1, results2]

if __name__ == "__main__":
    #queries = ["toxic+algae","cyanobacteria","algal+bloom","algae bloom","blue-green+algae","red+tide"]
    #for query in queries:
        #pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
        #pool.submit(instagram(df))
        #pool.submit(instagram(df))
        #pool.shutdown(wait=True)
    instagram(df)
    #print(results1)
    #print(timestamp)
    #print(titles)
    #print(links)
    dict = {'links': links, 'titles': titles, 'texts': results1, 'timestamp':timestamp}
    df = pd.DataFrame(dict)
    df.to_csv('instagram.csv')
    #df = pd.DataFrame(results)
    #df.to_csv('file5.csv')
    #browser.quit()
#print("Instagram Completed")
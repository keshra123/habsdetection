from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options   
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime

df = pd.read_csv('serp1.csv',index_col=0)
#print(df.iloc[1][0])
results1 = []
timestamp = []
titles = []  
links = []
#print(df.to_string())
def instagram(df):
    """
    results1 = []
    timestamp = []
    titles = []  
    links = []
    """
    for link in range(len(df)):
        opts = Options()
        opts.add_argument("--headless")
        browser = Firefox(opts)
        url = df.iloc[link][0]
        #url = 'https://www.instagram.com/inspectorplanet/reel/C5WwGvruBCh/'
        #url = 'https://www.instagram.com/thesarahpilla/reel/Cy3oI0LpPml/'
        #url = 'https://www.instagram.com/theoaklandside/p/C4RVsw9pwUF/'
        browser.get(url)
        #get_title = driver.title 
        browser.implicitly_wait(20)
        #html = browser.page_source
        #soup = BeautifulSoup(html)
        #print(soup)
        get_title = browser.title 
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
        links.append(url)
    browser.quit()
    #titles.append(browser.find_element(By.XPATH,'/html/head/meta[24]').text)
    #results1 =[results1, results2]

if __name__ == "__main__":
    instagram(df)
    print(results1)
    print(timestamp)
    print(titles)
    print(links)
    dict = {'links': links, 'titles': titles, 'texts': results1, 'timestamp':timestamp}
    df = pd.DataFrame(dict)
    df.to_csv('instagram.csv')
    #df = pd.DataFrame(results)
    #df.to_csv('file5.csv')
    #browser.quit()

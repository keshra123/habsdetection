import bs4
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options   
from selenium.webdriver.common.by import By
import pandas as pd
import datetime

opts = Options()
opts.add_argument("--headless")
browser = Firefox(opts)
browser.get('https://www.facebook.com/story.php/?story_fbid=824808679693130&id=100064920150241&paipv=0&eav=AfbUMt7FPzK7cRP3U_v-88uWkJF5vMJQwwJ0lxGUk9_b81d6HSrKb0vOMJTIctR84g4&_rdr')
browser.implicitly_wait(20)
#html = browser.page_source
#print(soup)
titles = []
links = []
times = []
results = (browser.find_element(By.CSS_SELECTOR,'div > div > span > div').text)
time = (browser.find_element(By.CSS_SELECTOR,'span:nth-child(2) > span > a > span > span').text)
#\:R1al9aqqd9emhpapd5aqH1\: > span:nth-child(2) > span > a > span > span
#time = browser.find_element(By.XPATH,'//b[@class="xmper1u x1qlqyl8 x1r8a4m5 x1n2onr6 x17ihmo5"')
#times.append(browser.find_element(By.XPATH,'//*[@id=":R1al9aqqd9emhpapd5aqH1:"]/span[2]/span/a/span/span/b/b'))
#driver.find_elements_by_css_selector(".sc-eYdvao.kvdWiq [href]")
#links.append(browser.find_element(By.CSS_SELECTOR,'span.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv.xo1l8bm > a').get_attribute("href"))
#link = (browser.find_element(By.XPATH,'//*[@id=":R1al9aqqd9emhpapd5aqH1:"]/span[2]/span/a/span/span/b/b'))
#soup1 = BeautifulSoup(soup, 'html.parser')
#link = (browser.find_element(By.XPATH,'//a[@class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1lliihq x1lku1pv""]'))
#//*[@id=":R1al9aqqd9emhpapd5aqH3:"]/div[2]/div/a'))
#results = soup.findAll("p")
#results2 = soup.findAll("h1")

titles.append(results)
#times.append(link)
#results1 =[results1, results2]
print(titles)
#print(links)
print(time)

#df = pd.DataFrame(results)
#df.to_csv('file5.csv')
#results = soup.findAll("p")
#results2 = soup.findAll("h1")
#results1 =[results1, results2]
#df = pd.DataFrame(results)
#df.to_csv('file5.csv')
browser.quit()

import requests
import bs4
from bs4 import BeautifulSoup
import threading
def proxies(): 
    response = requests.get('https://www.us-proxy.org',headers = {'User-Agent': 'Mozilla/5.0'})
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    proxy_list = soup.textarea.text[75:]
    proxies = [] 
    #for proxy in range(len(proxy_list))
    i = 15 
    j = i-15
    while i !=(len(proxy_list)-1):
        proxies.append(proxy_list[j:i])
    print(proxies)


if __name__ =="__main__":
    t1 = threading.Thread(target=proxies)
    t2 = threading.Thread(target=proxies)
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
#print(proxy_list)
#print(len(proxy_list))
#link = proxy_list[0:15]
#print(link)
#print(proxy_list[:3595])


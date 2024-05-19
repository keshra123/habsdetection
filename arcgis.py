from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options   
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless")
browser = Firefox(opts)
url = df.iloc[link][0]
browser.get(url)
URL = "https://experience.arcgis.com/experience/471ac77822b34303ba3c4170ccf11a2f"
page = requests.get(URL)

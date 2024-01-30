from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json  # Import json module

search_phrase = input("Enter a search phrase: ")

print("STEP 1: Open Chrome browser")
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
driver.get(f"https://www.tiktok.com/search/video?q={search_phrase.replace(' ', '%20')}")

time.sleep(60)  # Adjust this sleep time as needed

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

print("STEP 2: Scrolling page")
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height * i) > scroll_height:
        break

className = "css-1as5cen-DivWrapper e1cg0wnj1"

script = "let l = [];"
script += "document.getElementsByClassName(\""
script += className
script += "\").forEach(item => { l.push(item.querySelector('a').href)});"
script += "return l;"

urls = driver.execute_script(script)

# Save to JSON file
print("STEP 3: Saving links to JSON file")
with open('tiktok_links.json', 'w') as file:
    json.dump(urls, file)

print(f"Saved {len(urls)} video links to tiktok_links.json")

driver.quit()
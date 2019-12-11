# Screen Shots on Python

options: `selenium` and `splinter`. 

## Links 

- this: https://medium.com/@ronnyml/website-screenshot-generator-with-python-593d6ddb56cb
- http://chromedriver.chromium.org/getting-started
- https://pythonspot.com/category/selenium/
- http://chromedriver.chromium.org/downloads
- full screen shot: https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver
- https://splinter.readthedocs.io/en/latest/

## Selenium 

### Simple Example 

```py
from selenium import webdriver
DRIVER = 'chromedriver' # driver location 
driver = webdriver.Chrome(DRIVER)
driver.get('https://www.spotify.com')
screenshot = driver.save_screenshot('my_screenshot.png')
driver.quit()
```

<center>
<b> Example of Scraped Image </b>
<img src="images/ex_simple.png" border="1" style="width:400px;">
</center>

### Full Screen Shot Example 

```py 
from selenium import webdriver
DRIVER = 'chromedriver' # driver location 
url = 'https://stackoverflow.com/'
driver = webdriver.Chrome(DRIVER)
driver.get(url)
el = driver.find_element_by_tag_name('body')
el.screenshot(images/ex_full.png)
driver.quit()
```

<center>
<b> Example of Scraped Image </b>
<img src="images/ex_full.png" border="1" style="width:400px;">
</center>

## Splinter 

- https://splinter.readthedocs.io/en/latest/install.html
- https://stackoverflow.com/questions/40188699/webdriverexception-message-geckodriver-executable-needs-to-be-in-path
- https://github.com/douglasmiranda/splinter-examples/blob/master/another_examples/screenshot.py

### Installation 

```
pip install splinter
brew install geckodriver
pip install Pillow
brew cask install chromedriver
```

### Example 

```py 
browser = Browser()
screenshot_path = browser.screenshot('absolute_path/your_screenshot.png', full=True)

browser.driver.save_screenshot('test.png')
```

```py 
from splinter import Browser

with Browser() as browser:
    # Visit URL
    url = "http://www.google.com"
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_name('btnG')
    # Interact with elements
    button.click()
    if browser.is_text_present('splinter.readthedocs.io'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")
```
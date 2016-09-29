from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = webdriver.Firefox(firefox_binary=FirefoxBinary(
    firefox_path='C:\\firefox\\Mozilla Firefox\\firefox.exe'    
))
#Edith has head about a cool new online to-do app.  She goes to check out its homepage.
browser.get('http://localhost:8000')

#She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

#She is invited to enter a to-do item straight away

#She type "Buy peacock feathers" into the text box (Edith's 
#hobby is tying fly fishing lures)

#When she hits enter, the page updates, and now the page lists
#"1: Buy peacock feathere" as an item in a to-do list

#There is still a text box inviting her to add another item.  
#She enters "Use peacock feathers to make a fly" (Edith is ver
#y methodical)

#The page updates again, and now shows both items on her list

#Edith wonders whether the site will remember her list.  Then 
#she sees that the site has generated a uniqu URL for her -- t
#here is some explanatory text to that effect.

#She visits that URL - her to-do list is still there.

#Satisfied, she goes back to sleep

browser.quit()


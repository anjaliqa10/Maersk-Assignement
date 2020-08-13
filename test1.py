from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://data.sfgov.org/")

SearchBox = driver.find_element_by_id("search-catalog-input").send_keys("Movies", Keys.ENTER)

Movies_in_SF = driver.find_element_by_link_text("Film Locations in San Francisco").click()

WebTable = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section[3]/div[2]/div").click()
rows = len(driver.find_elements_by_xpath("//*[@id='app']/div/div[2]/section[3]/div[2]/div/div/div[5]/div["
                                         "1]/div/table/tbody/tr"))  # Count rows present in a table

cols = len(driver.find_elements_by_xpath("//*[@id='app']/div/div[2]/section[3]/div[2]/div/div/div[5]/div["
                                         "1]/div/table/thead/tr/th"))

print(rows)
print(cols)

print(
    "Title" + "     " + "Release Year" + "     " + "Locations" + "     " + "Fun Facts" + "     " + "Production Company" + "    " +
    "Distributor" + "      " + "Director" + "     " + "Writer" + "     " + "Actor 1" + "     " + "Actor 2" + "    " + "Actor 3")

for r in range(2, rows + 1):
    for c in range(1, cols + 1):
        value = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section[3]/div[2]/div/div/div[5]/div["
                                              "1]/div/table/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(value, end='     ')

    print()

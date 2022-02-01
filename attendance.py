# Import webdriver module from selenium
from selenium import webdriver

# Import time module for waiting 20 mins
import time

# Create new driver object (change the file name based on your OS)
driver = webdriver.Chrome("./chromedriver.exe")

# Visit the moodle login page and fill in login details
driver.get("http://lms.cet.ac.in/")

# Define Moodle email and password
moodle_username = "<Enter your admission no>"
moodle_pass = "<Enter your password>"

# Find the field element and send the input keys to the element
username_ip = driver.find_element_by_name("username")
username_ip.send_keys(moodle_username)
pass_ip = driver.find_element_by_name("password")
pass_ip.send_keys(moodle_pass)

# Find the login button by id and click it
login_btn = driver.find_element_by_id("loginbtn")
login_btn.click()

# Define the list of attendance page URLs
attendance_page_urls = [
    "http://lms.cet.ac.in/mod/attendance/view.php?id=3272&view=5",
    "http://lms.cet.ac.in/mod/attendance/view.php?id=3252&view=5",
    "http://lms.cet.ac.in/mod/attendance/view.php?id=3232&view=5",
    "http://lms.cet.ac.in/mod/attendance/view.php?id=3222&view=5",
    "http://lms.cet.ac.in/mod/attendance/view.php?id=3202&view=5",
    "http://lms.cet.ac.in/mod/attendance/view.php?id=3192&view=5",
    "http://lms.cet.ac.in/mod/attendance/view.php?id=3182&view=5",

]

# Start infinite loop
while 1:
    # For every URL visit the page
    for url in attendance_page_urls:
        driver.get(url)

        # Get the list of all "Submit attendance" buttons on the page using XPATH
        submit_attendance_btns = driver.find_elements_by_xpath(
            "//*[contains(text(), 'Submit attendance')]"
        )

        # If the list is empty, do nothing and continue
        if len(submit_attendance_btns) == 0:
            continue

        # Else visit the link (HTML "href" attribute) specified by the first button
        submit_attendance_btn = submit_attendance_btns[0]
        att_link = submit_attendance_btn.get_attribute("href")
        driver.get(att_link)

        # Find the fist attendance status radio button, ie, the one corresponding to "Present"
        status_btn = driver.find_elements_by_xpath("//input[@type='radio']")[0]

        # Click the status button and then the submit button
        status_btn.click()
        driver.find_element_by_id("id_submitbutton").click()

    # Sleep for 20 mins before trying again
    time.sleep(20 * 60)
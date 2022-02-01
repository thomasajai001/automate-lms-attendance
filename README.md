# automate-lms-attendance
Automated attendance recording tool for Moodle built using Selenium.
To run the script, 

 1. Clone the repository using the git command `https://github.com/thomasajai001/automate-lms-attendance.git`
 2.  Ensure that python3 and pip3 are installed
 3.   Download and place the [chromedriver](https://chromedriver.chromium.org/downloads) from in the repository folder
 4. Edit the `individual.py` file
	  -  Modify the  `moodle_mail`  and  `moodle_pass`  variables with your credentials
	  -  Edit the  `attendance_page_urls`  variable with the URLs to all the attendance pages of your subjects
 5. Install Selenium package by executing

	`pip install selenium`

 6. Execute the script using 

	`python ./attendance.py`

(Try using pip3 if pip command does not work)

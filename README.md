# BDD_Project
Amazon BDD Automation Framework

Site tested: amazon.com\
Design pattern used: page object model\
Methodology: behavior driven development

To import project\
git clone https: https://github.com/DavidBojan/BDD_Project

Libraries to install:\
pip install -U selenium\
pip install behave\
pip install behave-html-formatter\
pip install webdriver-manager

Run tests:\
behave -f html -o behave-report.html

Run tests with tags: homepage, search, login, cart\
behave -f html -o behave-report.html --tags=search

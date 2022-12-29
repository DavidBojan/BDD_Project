pip install -U selenium
pip install behave
pip install behave-html-formatter
pip install webdriver-manager

run test
behave -f html -o behave-report.html

run tests with tags: homepage, search, login, cart
behave -f html -o behave-report.html --tags=search

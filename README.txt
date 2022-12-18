This is a Project Folder for "AT_Project_01"

There are two Folder:-

1.) Test_Codes - It consists of Test Files as mentioned below
                    > TC_Login_01   - OrangeHRM login website - Valid login
                    > TC_Login_02   - OrangeHRM login website - Vnvalid login
                    > TC_PIM_01     - OrangeHRM login website - Add new employee with personal details
                    > TC_PIM_02     - OrangeHRM login website - Edit existing employee
                    > TC_PIM_03     - OrangeHRM login website - Delete existing employee
                    > AT_Project_01 - It contains TC_Login_01, TC_Login_02, TC_PIM_01, TC_PIM_02 & TC_PIM_03

2.) Test_Data - It consists of Test Data's i.e. username, password, XPATH, ID, etc and file name mentioned below
                    > data

NOTE # If you want to run a Test File Kindly go to the Test_Codes to run a specific Python Selenium Automation File.


COMMAND TO RUN A TEST FILE:-
--------------------------
TC_Login_01:-
    pytest -v -s TC_Login_01.py
TC_Login_02:-
    pytest -v -s TC_Login_02.py
TC_PIM_01:-
    pytest -v -s TC_PIM_01.py
TC_PIM_02:-
    pytest -v -s TC_PIM_02.py
TC_PIM_03:-
    pytest -v -s TC_PIM_03.py
AT_Project_01:-
    pytest -v -s AT_Project_01.py

COMMAND TO RUN A TEST FILE REPORT:-
---------------------------------
TC_Login_01:-
pytest -v -s --capture=sys --html=C:\pytest_reports\TC_Login_01.html TC_Login_01.py
TC_Login_02:-
pytest -v -s --capture=sys --html=C:\pytest_reports\TC_Login_02.html TC_Login_02.py
TC_PIM_01:-
pytest -v -s --capture=sys --html=C:\pytest_reports\TC_PIM_01.html TC_PIM_01.py
TC_PIM_02:-
pytest -v -s --capture=sys --html=C:\pytest_reports\TC_PIM_02.html TC_PIM_02.py
TC_PIM_03:-
pytest -v -s --capture=sys --html=C:\pytest_reports\TC_PIM_03.html TC_PIM_03.py
AT_Project_01:-
pytest -v -s --capture=sys --html=C:\pytest_reports\AT_Project_01.html AT_Project_01.py
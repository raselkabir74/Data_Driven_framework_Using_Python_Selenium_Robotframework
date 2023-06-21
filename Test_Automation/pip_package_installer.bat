@ECHO OFF 
:: This batch file installs necessary python packages from requirements.txt
python -m pip install --upgrade pip
pip install -U pyautoit
pip install -r requirements.txt
pip install --upgrade robotframework-datadriver[XLS]
pip install robotframework-pabot
PAUSE

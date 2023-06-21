@ECHO ON

:: Get the datetime in a format. The report folder will be generated based on time stamp.
SET DATETIME=%date%_%time%
SET DATETIME=%DATETIME: =_%
SET DATETIME=%DATETIME::=%
SET DATETIME=%DATETIME:/=_%
SET DATETIME=%DATETIME:.=_%
:: Test runner bat file.

:: Configurable value: Webdriver default time out value, test environment, release quarter, browser, application url, user name, password, test suite, report path, test data prefix

SET DEFAULT_TIME_OUT_VALUE=60
SET TEST_ENVIRONMENT="Portal-Test"
SET RELEASE_QUARTER=2019.Jun
SET BROWSER=Chrome
SET APP_URL=https://kdp.amazon.com/en_US
SET USERNAME=---
SET PASSWORD=----
SET TEST_SUITE=./RobotFramework/Tests/TC_AutomateAmazonKDP*.robot
SET REPORT_PATH=./Automation_Reports/
SET TEST_DATA_PREFIX=Automation_

:: Please, do not update the below command
::CALL robot --pythonpath ./ --variable "BROWSER NAME":%BROWSER% --variable "TEST ENVIRONMENT":%TEST_ENVIRONMENT% --variable "LOGIN PAGE URL":%APP_URL% --variable "VALID USERNAME":%USERNAME% --variable "VALID PASSWORD":%PASSWORD%  -d %REPORT_PATH%/%DATETIME%  %TEST_SUITE%
CALL pabot --processes 4 --pythonpath ./ --variable "BROWSER NAME":%BROWSER% --variable "TEST ENVIRONMENT":%TEST_ENVIRONMENT% --variable "LOGIN PAGE URL":%APP_URL% --variable "VALID USERNAME":%USERNAME% --variable "VALID PASSWORD":%PASSWORD% -d %REPORT_PATH%/%DATETIME%  %TEST_SUITE%

*** Settings ***
Documentation     A resource file with reusable keywords and variables.

Resource          ../Resources/Pages/login_page_resource.robot

Library           ../../TestFramework/Libraries/TestFixture.py
Library           ../../TestFramework/Libraries/RobotTests/Home.py
Library           Collections

*** Variables ***
${DEFAULT TIME OUT VALUE}       120                                  # Webdriver default time out value. editable. should be greater than 0, Can't be empty
${TEST ENVIRONMENT}             Portal-Test                         # Test environment; Default Value: Production; Must be: Production/Staging/Client
${LOGIN PAGE URL}               https://kdp.amazon.com/en_US        # Application URL.
${BROWSER NAME}                 Chrome                              # Browser name.
${VALID USERNAME}               williamttuckeer@gmail.com           # Valid user name.
${VALID PASSWORD}               M#284591#                           # Valid password.
${LOGIN STATUS}                 False                               # Login status. Default value - False
${SIGN OUT STATUS}              False                               # Sign out status. Default value - False
${SCREENSHOT DIRECTORY}         ${EMPTY}                            # Screenshot directory, selected based on project output directory.
${IMAGE PATH}                   ${EMPTY}                            # Image path. is returned from test framework.
${TEST DATA PREFIX}             Automation_                         # Test data prefix. Default value: UAT_AUTO_. Editable.


*** Keywords ***
Validate SetUp
    Setup    ${BROWSER NAME}
    set time out value      ${DEFAULT TIME OUT VALUE}

Validate Login Into Application
    Goto    ${LOGIN PAGE URL}
    [Arguments]      ${USERNAME}=${VALID USERNAME}          ${PASSWORD}=${VALID PASSWORD}
    Submit Credentials    ${USERNAME}    ${PASSWORD}
    ${LOGIN STATUS} =    Login Should Be Succesfull
    [Teardown]    run keyword if    '${LOGIN STATUS}'=='False'    Log Screenshot

Validate Log Out Functionality
    ${SIGN OUT STATUS} =    Sign out
    [Teardown]    run keyword if    '${SIGN OUT STATUS}'=='False'    Log Screenshot

Validate Suite Teardown
    teardown

Log Screenshot
    ${SCREENSHOT DIRECTORY} =   get variable value      ${OUTPUT DIR}
    ${IMAGE PATH} =    capture screenshot     ${SCREENSHOT DIRECTORY}
    Log    <img src="${IMAGE PATH}">    HTML

Get Test Data Source Excel File Path
    [Arguments]     ${MODULE SPECIFIC EXCEL FILE}
    ${CURRENT DIRECTORY} =   get variable value      ${EXECDIR}
    ${MODULE SPECIFIC EXCEL FILE} =  set variable  ${MODULE SPECIFIC EXCEL FILE}
    ${TEST DATA EXCEL FILE} =      set variable  ${CURRENT DIRECTORY}${MODULE SPECIFIC EXCEL FILE}
    return from keyword  ${TEST DATA EXCEL FILE}

Read Test Data From Excel Sheet
    [Arguments]     ${FILE PATH}       ${SHEET NAME}
    ${RETRIEVED TEST DATA FROM EXCEL SHEET} =     read test data         ${FILE PATH}       ${SHEET NAME}
    return from keyword      ${RETRIEVED TEST DATA FROM EXCEL SHEET}

Write Test Data In Excel Sheet Column
    [Arguments]     ${FILE PATH}       ${SHEET NAME}     ${COLUMN NAME}    ${COLUMN VALUE}
    ${STATUS} =     set variable    False
    ${STATUS} =     write test data         ${FILE PATH}       ${SHEET NAME}     ${COLUMN NAME}    ${COLUMN VALUE}
    should be true      ${STATUS}

Verify If Organization Is Outsourcing
    [Arguments]     ${ORGANIZATION NAME}
    ${STATUS} =     is organization outsourcing     ${ORGANIZATION NAME}
    log     ${STATUS}
    [Return]       ${STATUS}
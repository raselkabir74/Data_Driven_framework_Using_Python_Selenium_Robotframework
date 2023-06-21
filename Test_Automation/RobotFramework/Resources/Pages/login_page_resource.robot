*** Settings ***
Documentation   Login Page Resource File With Valid, Invalid Credentials And Necessary Keywords.

Library         ../../../TestFramework/Libraries/RobotTests/Login.py
Library         ../../../TestFramework/Libraries/RobotTests/Home.py

*** Variables ***
${USERNAME}       ${EMPTY}
${PASSWORD}       ${EMPTY}
${STATUS}         False

*** Keywords ***
Submit Credentials
    [Arguments]    ${USERNAME}    ${PASSWORD}
    ${STATUS} =     perform login    ${USERNAME}    ${PASSWORD}
    should be true    ${STATUS}        Unable to submit credentials
    [Teardown]      run keyword if    '${STATUS}'=='False'    Log Screenshot

Login Should Be Succesfull
    ${STATUS} =    is login successful
    should be true    ${STATUS}     Unable to login into application
    return from keyword    ${STATUS}

Login Should Be Failed
    ${STATUS}=    is login successful
    should not be true    ${STATUS}     Able to login into application
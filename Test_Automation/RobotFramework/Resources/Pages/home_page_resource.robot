*** Settings ***
Documentation   Home Page Resource File With All Necessary Keywords.

Resource        ../common_resource.robot

Library     ../../../TestFramework/Libraries/RobotTests/Home.py
Library         Collections

*** Variables ***
${STATUS}                                                       False

*** Keywords ***
Verify publish paper
    [Arguments]         ${CurrentSheetName}      ${PreviouslyExecutedSheet}      ${language}          ${BookTtitle}           ${BookSubtitle}       ${primaryAuthorPrefix}       ${FirstName}        ${LastName}     ${Description}      ${Keywords}     ${PublishingRightsRadioButton}      ${Category}     ${SubCategory}      ${SubCategoryChild}     ${SubCategorySubChild}      ${AdultContentRadioButton}      ${TrimSizeWidthAndHeight}      ${BookNameToUpload}     ${BookCoverRadioButton}     ${BookCoverToUpload}        ${ListPrice}

    ${STATUS} =     kdp publish paper     ${CurrentSheetName}      ${PreviouslyExecutedSheet}        ${language}          ${BookTtitle}           ${BookSubtitle}       ${primaryAuthorPrefix}       ${FirstName}        ${LastName}     ${Description}      ${Keywords}     ${PublishingRightsRadioButton}      ${Category}     ${SubCategory}      ${SubCategoryChild}     ${SubCategorySubChild}      ${AdultContentRadioButton}      ${TrimSizeWidthAndHeight}      ${BookNameToUpload}     ${BookCoverRadioButton}     ${BookCoverToUpload}        ${ListPrice}

    should be true      ${STATUS}      Unable to publish paper
    [Teardown]      run keyword if    '${STATUS}'=='False'    Log Screenshot
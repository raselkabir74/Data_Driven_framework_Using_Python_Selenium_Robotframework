*** Settings ***
Documentation     A Test Suite With Set Of Tests To Validate My Organization- Plans and Units Tab Functionality

Resource          ../Resources/common_resource.robot
Resource          ../Resources/Pages/home_page_resource.robot
Library             DataDriver          TestData.xlsx      sheet_name=Sheet1

Suite Setup       Validate SetUp
Suite Teardown    Validate Suite Teardown
Test Setup        Validate Login Into Application
Test Template     publish paper

*** Variables ***

*** Test Cases ***
Validate Publish Papers using ${SL}

*** Keywords ***
publish paper
    [Arguments]        ${CurrentSheetName}      ${PreviouslyExecutedSheet}    ${language}          ${BookTtitle}           ${BookSubtitle}       ${primaryAuthorPrefix}       ${FirstName}        ${LastName}     ${Description}      ${Keywords}     ${PublishingRightsRadioButton}      ${Category}     ${SubCategory}      ${SubCategoryChild}     ${SubCategorySubChild}      ${AdultContentRadioButton}      ${TrimSizeWidthAndHeight}      ${BookNameToUpload}     ${BookCoverRadioButton}     ${BookCoverToUpload}        ${ListPrice}
    Verify publish paper        ${CurrentSheetName}      ${PreviouslyExecutedSheet}      ${language}          ${BookTtitle}           ${BookSubtitle}       ${primaryAuthorPrefix}       ${FirstName}        ${LastName}     ${Description}      ${Keywords}     ${PublishingRightsRadioButton}      ${Category}     ${SubCategory}      ${SubCategoryChild}     ${SubCategorySubChild}      ${AdultContentRadioButton}      ${TrimSizeWidthAndHeight}      ${BookNameToUpload}     ${BookCoverRadioButton}     ${BookCoverToUpload}        ${ListPrice}

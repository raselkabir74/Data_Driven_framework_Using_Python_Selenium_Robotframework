"""Implementing Home Screen Page objects repository"""
import os

from TestFramework.Libraries.Pages.base_page import BasePage
from TestFramework.Libraries.Pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import autoit
import time


class HomePage(BasePage):
    # Start: Home page locators
    welcome_message_locator = (By.XPATH, "h2[text()='Welcome']")
    logout_button_locator = (By.XPATH, "//a[text()='Sign out']")
    select_an_organization_text_box_locator = (By.XPATH, "//input[@class='k-input' and @placeholder='Select an organization']")

    paperback_button_locator = (By.ID, "create-paperback-button")
    language_dropdown_id = (By.ID, "data-print-book-language-native")
    list_price_text_field_locator = (By.XPATH, "//div[@id='data-pricing-print-us-price-input']//input")

    book_description = (By.ID, "data-print-book-description")
    category_chooser_save_button = (By.ID, "category-chooser-ok-button-announce")
    approve_book_preview = (By.ID, "printpreview_approve_button_enabled")

    loading_locator = (By.XPATH, "//span[@id='uploading-popover-content' and text()='Uploading...']")
    cover_upload_success_message_locator = (By.XPATH, "//div[@id='data-print-book-publisher-cover-file-upload-success']//span[@class='success-header' and text()='Cover uploaded successfully!']")
    your_book_has_been_assigned_message = (By.XPATH, "//div[@id='print-isbn-success-alert']/descendant::div[normalize-space(text())='Your book has been assigned a free KDP ISBN:']")
    print_previewer_page_header = (By.XPATH, "//div[@id='header-title' and normalize-space()='Print Previewer']")
    expanded_distribution_checkbox_locator = (By.XPATH, "//span[normalize-space()='Expanded Distribution']/../../../../..//input[@type='checkbox']")
    start_your_input_now_button_locator = (By.ID, "publish-confirm-popover-print-start-announce")
    select_button_locator = (By.XPATH, "//span[normalize-space()='Select']/..//input")
    black_and_white_interior_with_white_space_button_locatort = (By.ID, "a-autoid-1-announce")
    popup_close_icon_locator = (By.XPATH, "//button[@aria-label='Close']/i")
    not_locator = (By.XPATH, "//this is not a locator")
    # End: Home page locators


    def is_login_successful(self):
        """
        Implementing is login successful functionality
        :return: True/False
        """
        self.clear_existing_handles()
        is_successful = self.is_element_present(self.logout_button_locator, time_out=30)
        return is_successful

    def sign_out(self):
        """
        Implementing sign out functionality
        :return:
        """
        self.click_element(self.logout_button_locator, script_executor=True, error_message='Sign out failed, logout button locator not found before specified time out')
        login = LoginPage()
        self.refresh_window()
        self.wait(120).until(EC.visibility_of_element_located(login.login_button_locator), 'element in login page not found before specified time')

    def choose_category(self, category, sub_category, sub_category_child, sub_category_sub_child):
        """
        Implementing choose category functionality
        :param category:
        :param sub_category:
        :param sub_category_child:
        :param sub_category_sub_child:
        :return:
        """
        category_tree_plus_icon = (By.XPATH, "//ul[@id='category-chooser-root-list']/descendant::a[normalize-space(text())='"+category+"'] | //ul[@id='category-chooser-root-list']/descendant::span[normalize-space(text())='"+category+"']")
        self.click_element(category_tree_plus_icon)

        if sub_category_child.strip().lower() != "n":
            subcategoryLocator = (By.XPATH, "//a[@class='a-link-normal' and text()='"+category+"']/../..//a[@class='a-link-normal' and text()='" + sub_category + "']")
            self.click_element(subcategoryLocator)
            if sub_category_sub_child.strip().lower() != "n":
                subcategoryChildLocator = (By.XPATH, "//a[@class='a-link-normal' and normalize-space(text())='" + sub_category + "']/../..//a[@class='a-link-normal' and text()='" + sub_category_child + "']")
                self.click_element(subcategoryChildLocator)
                subcategorySubChildLocator = (By.XPATH, "//a[@class='a-link-normal' and normalize-space(text())='" + sub_category_child + "']/../..//span[@class='a-label a-checkbox-label' and text()='" + sub_category_child + "']")
                self.click_element(subcategorySubChildLocator)
            else:
                subcategoryChildLocator = (By.XPATH, "//a[@class='a-link-normal' and normalize-space(text())='" + sub_category + "']/../..//span[@class='a-label a-checkbox-label' and text()='" + sub_category_child + "']")
                self.click_element(subcategoryChildLocator)
        else:
            subcategoryLocator = (By.XPATH, "(//a[@class='a-link-normal' and text()='"+category+"']/../..//span[@class='a-label a-checkbox-label' and text()='"+sub_category+"'])[1]")
            self.click_element(subcategoryLocator)

        self.click_element(self.category_chooser_save_button, script_executor=True)

    def set_value_into_specific_input_field(self, field_label_name_or_placeholder, value, is_placeholder=False):
        """
        Implementing set value into specific input field functionality
        :param field_label_name_or_placeholder:
        :param value:
        :param is_placeholder:
        """
        if is_placeholder is False:
            input_field_locator = (By.XPATH, "(//span[normalize-space()='" + field_label_name_or_placeholder + "']/../../../following-sibling::div[1]//input)[1]")
            if self.is_element_visible(input_field_locator, 2) is False:
                input_field_locator = (By.XPATH, "//span[normalize-space()='" + field_label_name_or_placeholder + "']/../following-sibling::div[1]/input[1]")
        else:
            input_field_locator = (By.XPATH, "//input[@placeholder='" + field_label_name_or_placeholder + "']")
        self.set_value_into_input_field(input_field_locator, value)

    def click_on_specific_button(self, button_name, script_executor=False):
        """
        Implementing click on specific button functionality
        :param button_name:
        :param script_executor:
        :param is_span:
        """
        button_locator = (By.XPATH, "//button[normalize-space()='" + button_name + "']")
        if script_executor:
            self.click_element(button_locator, True)
        else:
            self.click_element(button_locator)

    def publish_paper(self, current_sheet_name, previously_executed_sheet, language, bookTitle, bookSubtitle, primaryAuthorPrefix, firstName, lastName, description, keywords,
                      publishingRightsRadioButton, category, sub_category, sub_category_child, sub_category_sub_child,
                      adultContentRadioButton, trimSizeWidthAndHeight, bookNameToUpload, bookCoverRadioButton, bookCoverToUpload, listPrice):
        """
        Implementing publish paper functionality
        :param current_sheet_name:
        :param previously_executed_sheet:
        :param language:
        :param bookTitle:
        :param bookSubtitle:
        :param primaryAuthorPrefix:
        :param firstName:
        :param lastName:
        :param description:
        :param keywords:
        :param publishingRightsRadioButton:
        :param category:
        :param sub_category:
        :param sub_category_child:
        :param sub_category_sub_child:
        :param adultContentRadioButton:
        :param trimSizeWidthAndHeight:
        :param bookNameToUpload:
        :param bookCoverRadioButton:
        :param bookCoverToUpload:
        :param listPrice:
        :return:
        """
        global mappaedcwd
        cwd = os.getcwd().split("\Test_Automation")[0]
        mappaedcwd = cwd + "\\Test_Automation"
        filePath = mappaedcwd + "\\RobotFramework\\Tests\\TestData.xlsx"
        if current_sheet_name == "Sheet1":
            self.write_test_data(filePath, "Sheet1", "IS FILES UPLOADED", "NO")
            self.write_test_data(filePath, "Sheet2", "IS FILES UPLOADED", "NO")
            self.write_test_data(filePath, "Sheet3", "IS FILES UPLOADED", "NO")
            self.write_test_data(filePath, "Sheet4", "IS FILES UPLOADED", "NO")
        self.click_element(self.paperback_button_locator)
        self.select_dropdown_item(self.language_dropdown_id, ""+language+"")
        self.set_value_into_specific_input_field("Book Title", ""+bookTitle+"")
        self.set_value_into_specific_input_field("Subtitle", ""+bookSubtitle+"")
        self.set_value_into_specific_input_field("Prefix", ""+primaryAuthorPrefix+"", is_placeholder=True)
        self.set_value_into_specific_input_field("First name", "" + firstName + "", is_placeholder=True)
        self.set_value_into_specific_input_field("Last name", "" + lastName + "", is_placeholder=True)
        self.set_value_into_input_field(self.book_description, ""+description+"")

        keywords = keywords.strip().split(",")
        length = len(keywords)

        if length > 0:
            if length > 7:
                length = 7
            for i in range(0, length):
                keyword_testbox_locator = (By.ID, "data-print-book-keywords-" + str(i) + "")
                self.set_value_into_input_field(keyword_testbox_locator, keywords[i])

        publishingRightsRadioButton = (By.XPATH, "//span[normalize-space(text())='"+publishingRightsRadioButton+"']/preceding-sibling::input[@type='radio']")
        element = self.wait().until(EC.presence_of_element_located(publishingRightsRadioButton))
        if element.is_selected():
            pass
        else:
            self.click_element(publishingRightsRadioButton, script_executor=True)
        self.click_on_specific_button("Choose categories")
        self.choose_category(category, sub_category, sub_category_child, sub_category_sub_child)
        adultContentRadioButton = (By.XPATH, "//input[@name='data[print_book][is_adult_content]-radio']/following-sibling::span[normalize-space(text())='"+adultContentRadioButton+"']")
        self.click_element(adultContentRadioButton)

        # Fist page save and continue button action
        self.click_on_specific_button("Save and Continue")

        self.is_element_visible(locator=self.black_and_white_interior_with_white_space_button_locatort, timeout=900)
        self.click_element(self.black_and_white_interior_with_white_space_button_locatort, script_executor=True)
        self.click_on_specific_button("Select a different size")
        trimSizeWidthAndHeight = trimSizeWidthAndHeight.split(",")
        self.set_value_into_specific_input_field("Width:", trimSizeWidthAndHeight[0])
        self.set_value_into_specific_input_field("Height:", trimSizeWidthAndHeight[1])
        self.click_element(self.select_button_locator, script_executor=True)

        # [Start:] File upload section

        # [Start:] Wait for the files to be uploaded for previous sheet
        if current_sheet_name != "Sheet1":
            end_time = time.time() + 3600
            while self.read_data_from_excel_file(filePath, previously_executed_sheet, "IS FILES UPLOADED") != "YES":
                time.sleep(3)
                if self.read_data_from_excel_file(filePath, previously_executed_sheet, "IS FILES UPLOADED") == "YES":
                    break
                if time.time() > end_time:
                    break
        # [End:] Wait for the files to be uploaded for previous sheet

        try:
            filePath = mappaedcwd + "\\RobotFramework\\Resources\\ExternalDataSource\\UploadFiles\\" + bookNameToUpload + ""
            if os.path.exists(filePath) is True:
                self.click_on_specific_button("Upload paperback manuscript")
                time.sleep(2)
                autoit.win_wait_active("Open")
                autoit.control_focus("Open", "Edit1")
                autoit.control_set_text("Open", "Edit1", filePath)
                time.sleep(1)
                autoit.control_click("Open", "Button1")
            else:
                raise ValueError("Unable to find any book named "+bookNameToUpload+", please enter a valid book name")
        except:
            raise
        self.wait_for_ajax_spinner_load(ajax_spinner_locator=self.loading_locator, timeout=1800)

        bookCoverRadioButton = (By.XPATH, "//h5[normalize-space(text())='"+bookCoverRadioButton+"']/../..")
        self.click_element(bookCoverRadioButton)

        try:
            filePath = mappaedcwd + "\\RobotFramework\\Resources\\ExternalDataSource\\UploadFiles\\" + bookCoverToUpload + ""
            if os.path.exists(filePath) is True:
                self.click_on_specific_button("Upload your cover file")
                time.sleep(2)
                autoit.win_wait_active("Open")
                autoit.control_focus("Open", "Edit1")
                autoit.control_set_text("Open", "Edit1", filePath)
                time.sleep(1)
                autoit.control_click("Open", "Button1")
            else:
                raise ValueError("Unable to find any book cover named "+bookCoverToUpload+", please enter a valid book cover name")
        except:
            raise
        filePath = mappaedcwd + "\\RobotFramework\\Tests\\TestData.xlsx"
        self.write_test_data(filePath, current_sheet_name, "IS FILES UPLOADED", "YES")
        self.is_element_visible(locator=self.cover_upload_success_message_locator, timeout=1800)
        # [End:] File upload section

        self.click_on_specific_button("Assign me a free KDP ISBN")
        self.click_on_specific_button("Assign ISBN")
        self.is_element_visible(locator=self.your_book_has_been_assigned_message, timeout=180)

        self.click_on_specific_button("Launch Previewer", True)
        self.is_element_visible(locator=self.print_previewer_page_header, timeout=1800)
        self.is_element_clickable(locator=self.approve_book_preview, timeout=300)
        self.click_element(self.approve_book_preview)

        # Second page save and continue button action
        self.click_on_specific_button("Save and Continue")
        self.is_element_visible(locator=self.list_price_text_field_locator, timeout=900)
        self.set_value_into_input_field(self.list_price_text_field_locator, ""+listPrice+"")
        self.click_element(self.expanded_distribution_checkbox_locator, script_executor=True)
        self.click_on_specific_button("Publish Your Paperback Book")
        self.is_element_visible(locator=self.popup_close_icon_locator, timeout=900)
        self.click_element(self.popup_close_icon_locator, script_executor=True)
        filePath = mappaedcwd + "\\RobotFramework\\Tests\\TestData.xlsx"
        self.write_test_data(filePath, current_sheet_name, "IS FILES UPLOADED", "NO")
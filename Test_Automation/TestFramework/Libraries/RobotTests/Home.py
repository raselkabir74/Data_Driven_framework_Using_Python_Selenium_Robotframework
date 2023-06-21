"""Implementing Home UI Page Actions"""
import os

from selenium.common.exceptions import WebDriverException
from TestFramework.Libraries.logger import Logger
from TestFramework.Libraries.Pages.home_page import HomePage


class Home:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    logger = Logger().get_logger('Home')

    def __init__(self):
        self._home_page = HomePage()

    def is_login_successful(self):
        """
        Returning user login success status
        Implementing logging for is login successful functionality
        :return: True/False
        """
        try:
            self.logger.info('Start: is login successful')
            return self._home_page.is_login_successful()
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            raise
        finally:
            self.logger.info('End: is login successful')

    def sign_out(self):
        """
        Returning sign out status
        Implementing logging for sign out functionality
        :return: True/False
        """
        is_successful = None
        try:
            self.logger.info('Start: sign out')
            self._home_page.sign_out()
            is_successful = True
        except WebDriverException as exp:
            self.logger.error(exp.msg)
            is_successful = False
        finally:
            self.logger.info('End: sign out')
            return is_successful

    def kdp_publish_paper(self, current_sheet_name, previously_executed_sheet, language, bookTitle, bookSubtitle, primaryAuthorPrefix, firstName, lastName, description, keywords,
                          publishingRightsRadioButton, category, sub_category, sub_category_child, sub_category_sub_child, adultContentRadioButton,
                          trimSizeWidthAndHeight, bookNameToUpload, bookCoverRadioButton, bookCoverToUpload, listPrice):
        """
        Returning kdp publish paper status
        Implementing kdp public paper functionality
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
        :return: True/False
        """
        status = None
        try:
            self.logger.info('Start: KDP Publish Paper')
            self._home_page.publish_paper(current_sheet_name, previously_executed_sheet, language, bookTitle, bookSubtitle, primaryAuthorPrefix, firstName, lastName, description, keywords,
                                          publishingRightsRadioButton, category, sub_category, sub_category_child, sub_category_sub_child,
                                          adultContentRadioButton, trimSizeWidthAndHeight, bookNameToUpload, bookCoverRadioButton, bookCoverToUpload, listPrice)
            status = True
        except Exception as exp:
            self.logger.error(str(exp))
            cwd = os.getcwd().split("\Test_Automation")[0]
            filePath = cwd + "\\Test_Automation\\RobotFramework\\Tests\\TestData.xlsx"
            self._home_page.write_test_data(filePath, current_sheet_name, "IS FILES UPLOADED", "YES")
            status = False
        finally:
            self.logger.info('End: KDP Publish Paper')
            return status

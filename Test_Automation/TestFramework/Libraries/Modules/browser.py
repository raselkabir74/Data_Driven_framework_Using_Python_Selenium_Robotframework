"""

"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os.path
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import TestFramework.Libraries.Helpers.html5_drag_and_drop as drag_and_drop_utility

_driver = None
_existing_handles = []
_screenshot_count = 0
_time_out_value = 60
_current_browser = None
_download_folder_name = 'Downloads'

@property
def driver():
    """
    Global variable of WebDriver
    :return: WebDriver instance
    """
    global _driver
    return _driver

def open_chrome():
    """
    Implementing launch Chrome browser functionality
    Create a new Chrome Driver instance by a dictionary of capabilities to request when
             starting the browser session.
    :return: driver instance
    """
    global _driver
    global _current_browser
    _current_browser = 'chrome'
    caps = DesiredCapabilities.CHROME
    caps['javascriptEnabled'] = True
    caps['acceptSslCerts'] = True
    from selenium.webdriver.chrome.options import Options

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument("--disable-plugins-discovery");
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument('--headless')



    # options = Options()
    # options.add_argument("--disable-extensions")
    # prefs = {"profile.default_content_settings.popups": 0,
    #          "profile.default_content_setting_values.automatic_downloads": 1,
    #          "download.default_directory": os.path.join(os.getcwd(), _download_folder_name),
    # #          "directory_upgrade": True}
    # options.add_experimental_option("prefs", prefs)
    _driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=chrome_options, executable_path=get_driver_path('chrome'))
    print(_driver.title)

def open_firefox():
    """
    Implementing launch Firefox browser functionality
    Create a new Firefox Driver instance by a dictionary of capabilities to request when
             starting the browser session.
    :return: driver instance
    """
    global _driver
    global _current_browser
    _current_browser = 'firefox'
    caps = DesiredCapabilities.FIREFOX
    caps['javascriptEnabled'] = True
    caps['acceptSslCerts'] = True
    _driver = webdriver.Firefox(capabilities=caps, executable_path=get_driver_path('firefox'))

def open_ie():
    """
    Implementing launch IE browser functionality
    Create a new Internext Explorer Driver instance by a dictionary of capabilities to request when
             starting the browser session.
    :return: driver instance
    """
    global _driver
    global _current_browser
    _current_browser = 'ie'
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps['ignoreProtectedModeSettings'] = True
    caps['ignoreZoomSetting'] = True
    caps['initialBrowserUrl'] = ""
    caps['ensureCleanSession'] = True  # Cleanup session in IE Browser
    caps['enableElementCacheCleanup'] = True  # Clear WebElement Cache from IE
    _driver = webdriver.Ie(capabilities=caps, executable_path=get_driver_path('ie'))

def goto(value):
    """
    Implementing load web page functionality
    Loads a web page in the current browser session.
    :param value: URL
    :return:
    """
    global _driver
    maximize_window()
    delete_cookies()
    _driver.get(value)

def goto_specific_url(value):
    """
    Implementing goto specific url functionality
    :param value:
    :return:
    """
    global _driver
    _driver.get(value)

def set_time_out_value(value):
    """
    Implementing set time out value functionality
    :param value: time in seconds
    :return:
    """
    global _time_out_value
    _time_out_value = value

def get_time_out_value():
    """
    Implementing get time out value functionality
    :return: time out value
    """
    global _time_out_value
    return _time_out_value

def wait(value):
    """
    Implementing web driver wait functionality
    WebDriver Wait instance
    :param value: Seconds
    :return:
    """
    global _driver, _time_out_value
    if value is not None:
        return WebDriverWait(_driver, value)
    else:
        return WebDriverWait(_driver, _time_out_value)

def hover(element):
    """
    Implementing mouse hover functionality
    Mouse hover on WebElement
    :param element: WebElement locator
    """
    global _driver
    ActionChains(_driver).move_to_element(element).perform()

def maximize_window():
    """
    Implementing maximize browser window functionality
    Maximizes the current window that webdriver is using
    """
    global _driver
    _driver.maximize_window()

def delete_cookies():
    """
    Delete all cookies of browser
    Implementing delete cookies functionality
    """
    global _driver
    _driver.delete_all_cookies()
    _driver.refresh()

def refresh_window():
    """
    Implementing refresh current page functionality
    Refreshes the current page.
    """
    global _driver
    _driver.refresh()

def page_title():
    """
    Implementing get page title functionality
    Returns the title of the current page.
    """
    global _driver
    return _driver.title

def text_contains_on_page_source(text):
    """
    Implementing check text contains in html source functionality
    Returns True if text is present in page source. If not False
    :param text:
    :return: True/False
    """
    global _driver
    return text in _driver.page_source

def script_executor_click(element, execute_async_script):
    """
    Implementing executor click functionality
    Using JavaScript Executor, click on WebElement
    :param element: WebElement locator
    :param execute_async_script:
    """
    global _driver
    #TODO: Will implement the execute_async_script in future
    if execute_async_script is True:
        pass
    _driver.execute_script("var elem=arguments[0]; setTimeout(function() {elem.click();}, 50)", element)

def script_executor(element, script):
    """
    Implementing script executor functionality
    Using JavaScript Executor
    :param script: Java script command
    :param element: WebElement
    """
    global _driver
    if script is None:
        return _driver.execute_script(element)
    else:
        return _driver.execute_script(script, element)

def scroll_into_view(element):
    """
    Implementing scroll into view functionality
    :param element:
    :return:
    """
    global _driver
    _driver.execute_script("arguments[0].scrollIntoView(true);", element)

def close_browser():
    """
    Implementing close current window functionality
    Closes the current window.
    :return:
    """
    global _driver
    _driver.close()

def quit():
    """
    Implementing close browser functionality
    Quits the driver and closes every associated window.
    :return:
    """
    global _driver
    _driver.quit()

def switch_to_default_content():
    """
    Implementing switch back to parent frame functionality
    Get back to the parent frame
    :return:
    """
    global _driver
    _driver.switch_to_default_content()

def capture_screenshot(directory):
    """
    Implementing capture screenshot functionality
    :return: image path
    """
    global _screenshot_count
    file_name = "screenshot_"  + str.replace(str.replace(str(datetime.datetime.now()), ' ', '_'), ':', '') + "_" + str(_screenshot_count) + ".png"
    file_path = directory + "\\" + file_name
    _driver.get_screenshot_as_file(file_path)
    _screenshot_count += 1
    return file_name

def drag_and_drop(source, target, with_action_chain=False, with_custom_action_chain=False):
    """
    Implementing drag and drop functionality
    :param source:
    :param target:
    :param with_action_chain:
    :param with_custom_action_chain:
    :return:
    """
    global _driver
    if with_action_chain is True:
        actions = ActionChains(_driver)
        actions.drag_and_drop(source, target).perform()
    elif with_custom_action_chain is True:
        actions = ActionChains(_driver)
        actions.move_to_element(source).perform()
        actions.click_and_hold(source).move_to_element(target).perform()
        actions.release().perform()
    else:
        drag_and_drop_utility.execute_drag_and_drop(_driver, source, target)

def switch_to_frame(frame_element):
    """
    Implementing switch to frame functionality
    :param frame_element:
    :return:
    """
    global _driver
    _driver.switch_to_frame(frame_element)

def switch_to_previous_window():
    """
    Implementing switch to previous window functionality
    :return:
    """
    global _driver
    global _existing_handles
    _driver.switch_to_window(_existing_handles.pop())

def get_current_browser_name():
    """
    Implementing get current browser name functionality
    :return: _current_browser_name
    """
    global _current_browser
    return _current_browser

def double_click(element):
    """
    Implementing double click functionality
    :param element:
    :return:
    """
    global _driver
    actions = ActionChains(_driver)
    actions.double_click(element).perform()

def get_current_page_url():
    """
    Implementing get current page url functionality
    :return: current_url
    """
    return _driver.current_url

def get_driver_path(browser_name):
    """
    Implement return driver path based on browser name
    :param browser_name:
    :return:
    """
    _script_path = os.path.dirname(os.path.abspath(__file__))
    _driver_path = os.path.split(_script_path)[0]
    if(browser_name.lower() == 'chrome'):
        _browser_driver_path = os.path.join(_driver_path, 'Drivers', 'chromedriver.exe')
    elif(browser_name.lower() =='ie'):
        _browser_driver_path = os.path.join(_driver_path, 'Drivers', 'IEDriverServer.exe')
    else:
        _browser_driver_path = os.path.join(_driver_path, 'Drivers', 'geckodriver.exe')
    return _browser_driver_path

def clear_existing_handles():
    """
    Implementing clear existing handles functionality
    Clear _existing_handles
    :return:
    """
    global _existing_handles
    del _existing_handles[:]

def set_existing_handles():
    """
    Implementing set existing handles functionality
    Store current window handle into _existing_handles
    :return:
    """
    global _driver
    global _existing_handles
    _existing_handles.append(_driver.current_window_handle)

def switch_to_window(iteration=1, maximize=True, handler=None):
    """
    Implementing switch to child window functionality
    Switch to Child screen/window
    """
    global _driver
    global _existing_handles
    dummy_locator = (By.ID, "ThisIsDummyLocator")
    wait(10).until(lambda driver: len(driver.window_handles) > 1, 'New window not found before specified time.')
    found_handle = handler
    while found_handle is None and iteration <= 5:
        iteration += 1
        current_handles = set(_driver.window_handles)
        if len(current_handles) != len(_existing_handles):
            for current_handle in current_handles:
                if current_handle not in _existing_handles:
                    found_handle = current_handle
                    break
                else:
                    pass
        else:
            pass
        try:
            wait(5).until(EC.visibility_of_element_located(dummy_locator))
        except:
            pass
    if found_handle is not None:
        _driver.switch_to_window(found_handle)
        if maximize is True:
            maximize_window()
    else:
        raise WebDriverException(msg='Switch to new window failed.')

def switch_to_default_window():
    """
    Implementing switch to default window functionality
    Switch to default screen/window
    :return:
    """
    global _driver
    if len(_driver.window_handles) == 1:
        _driver.switch_to_window(_driver.window_handles[0])
    else:
        pass

def get_current_window_handle():
    """
    Implementing get current window handle functionality
    :return: _current_window_handle
    """
    return _driver.current_window_handle

def press_keyboard_key(key):
    """
    Implementing press keyboard key functionality
    :param key:
    :return:
    """
    global _driver
    actions = ActionChains(_driver)
    actions.send_keys(key)
    actions.perform()

def accept_alert():
    """
    Implementing accept alert functionality
    :return:
    """
    time.sleep(5)
    global _driver
    Alert(_driver).accept()

def move_to_element(element):
    """
    Implementing drag and drop functionality
    :param element:
    :return:
    """
    global _driver
    actions = ActionChains(_driver)
    actions.move_to_element(element).perform()

def select_multiple_element(element):
    """
    Implementing select multiple element functionality
    :param element:
    :return:
    """
    global _driver
    ActionChains(_driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

def press_key_combination(element, key1, key2):
    """
    Implementing press key combination functionality
    :param element:
    :param key1:
    :param key2:
    :return:
    """
    global _driver
    ActionChains(_driver).key_down(key1).send_keys(key2).key_up(key1).perform()
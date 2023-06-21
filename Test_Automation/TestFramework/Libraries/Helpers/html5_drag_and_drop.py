import os


class HTML5DragAndDrop:

    JQUERY_URL = "https://code.jquery.com/jquery-1.11.2.min.js"
    JQUERY_LOAD_HELPER = "jquery_load_helper.js"
    DRAG_AND_DROP_HELPER = "drag_and_drop_helper.js"

    @staticmethod
    def __load_jquery(driver, jquery_url=JQUERY_URL):
        """
        :param driver: WebDriver object
        :param jquery_url: STRING, url from which to import jq
        :return: None
        """
        with open(HTML5DragAndDrop.JQUERY_LOAD_HELPER) as f:
            load_jquery_js = f.read()

        # If JQ is already imported on the page, this wont overwrite it
        driver.execute_async_script(load_jquery_js, jquery_url)

    @staticmethod
    def drag_and_drop(driver, draggable, droppable):
        """
        :param driver: WebDriver object
        :param draggable: STRING, selector https://www.w3schools.com/jquery/jquery_selectors.asp
        :param droppable: STRING, selector https://www.w3schools.com/jquery/jquery_selectors.asp
        :return: None
        """
        HTML5DragAndDrop.__load_jquery(driver)  # for the drag and drop js script to work, it needs to have jq
        with open(HTML5DragAndDrop.DRAG_AND_DROP_HELPER) as f:  # getting js as a string from file and assigning to the variable
            drag_and_drop_js = f.read()
        drag_and_drop_command = "$(\"{draggable}\").simulateDragDrop({{ dropTarget: \"{droppable}\"}});"\
                                .format(draggable=draggable, droppable=droppable)
        driver.execute_script(drag_and_drop_js + drag_and_drop_command)


# HTML 5 Example
def execute_drag_and_drop(driver, source, destination):
    source_directory = os.getcwd()
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    HTML5DragAndDrop.drag_and_drop(driver, draggable=source, droppable=destination)
    os.chdir(source_directory)

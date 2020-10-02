from . import decorators
from .helpers import validate_time_settings
from collections import namedtuple


class WebDriverMixin:
    """
    Enhances the selenium.webdriver.remote.webdriver.WebDriver
    with several enhanced capabilities.
    """

    def __init__(self, *args, **kwargs):
        special_args = [
            "timeout",
            "poll_frequency",
            "recover",
            "implicit_wait",
            "debounce",
        ]
        self._selenious = namedtuple(
            "Selenius",
            special_args,
        )(0, 0.5, None, 0.0, 0.0)
        kwargs = {k: v for (k, v) in kwargs.items() if k not in special_args}
        print(args, kwargs)
        super().__init__(*args, **kwargs)

    def set_implicit_wait(self, time_to_wait):
        """
        Sets a sticky timeout to implicitly wait for an element to be found,
           or a command to complete. This method only needs to be called one
           time per session. To set the timeout for calls to
           execute_async_script, see set_script_timeout.

        Warning: The selenious package will fail if implicit_wait is larger
        than timeout or poll_frequency.  It is better to not set this and
        instead set_timeout.

        :Args:
         - time_to_wait: Amount of time to wait (in seconds)

        :Usage:
            driver.implicitly_wait(30)
        """
        validate_time_settings(
            time_to_wait, self._selenious.timeout, self._selenious.poll_frequency
        )

        self._selenious.implicit_wait = time_to_wait
        return super().set_implicit_wait(time_to_wait)

    def set_timeout(self, timeout):
        """Sets the default _selenious timout.

        The selenium webdriver has an implicitly_wait() command that
        once set cannot be overwritten.  There is also a WebDriverWait()
        facility to allow requests with a wait.  This command moves
        an equivalent to that capability directly into the select commands.
        You can specify a global wait timeout with set_timeout or pass
        a timeout parameter directly to the select command.

        :Args:
         - timeout - A number for the wait time for find commands.

        :Usage:
          driver.set_timeout(5)
        """
        validate_time_settings(
            self._selenious.implicit_wait, timeout, self._selenious.poll_frequency
        )

        self.selenius.timeout = timeout

    def set_debounce(self, debounce):
        """Sets the wait time for a select to have not changed.

        :Args:
        - debounce - Amount to wait for find_elements_* to not change.
          This may also be set to True which will use the poll_frequency,
          any falsey value will disable it.  By default it is 0.

        :Usage:
          driver.debounce(1.5)
        """

        self.selenius.debounce = debounce

    def set_poll_frequency(self, poll_frequency):
        """Sets the frequency polling will happen for the timeout.

        This is similar to the WebDriverWait polling frequency.  See
        set_timeout() for differences.

        :Args:
        - poll_frequency - Sleep interval between calls.
          By default, it is 0.5 second.

        :Usage:
          driver.set_poll_frequency(1.5)
        """
        validate_time_settings(
            self._selenious.implicit_wait, self._selenious.timeout, poll_frequency
        )

        self.selenius.poll_frequency = poll_frequency

    def set_recover(self, recover):
        """Sets the recover function.

        The recover function is run when a select fails or some
        actions like click fail.  The intent is to try to fix
        expected, but not typical web activities like an advertising
        popup covering the page being manipulated.

        The recovery function is guaranteed to be run at least once
        if there is an issue, but may be run multiple times at the
        poll_frequency if there is a timeout.

        :Args:
        - recover - The recover function to be run.  Parameters are:
          - webdriver - This webdriver (self)
          - function - The function calling the recover function.
          - kwargs - The kwargs sent to the function
          - elapsed - The time elapsed since the first attempt.
          - attempts - The number of attempts
        """
        self.selenius.recover = recover

    @decorators.find_element
    def find_element_by_id(self, *args, **kwargs):
        """Finds an element by id.

        :Args:
         - id_ - The id of the element to be found.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_id('foo')
        """
        return super().find_element_by_id(*args, **kwargs)

    @decorators.find_elements
    def find_elements_by_id(self, *args, **kwargs):
        """
        Finds multiple elements by id.

        :Args:
         - id_ - The id of the elements to be found.

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_id('foo')
        """
        return super().find_elements_by_id(*args, **kwargs)

    @decorators.find_element
    def find_element_by_xpath(self, *args, **kwargs):
        """
        Finds an element by xpath.

        :Args:
         - xpath - The xpath locator of the element to find.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_xpath('//div/td[1]')
        """
        return super().find_element_by_xpath(*args, **kwargs)

    @decorators.find_elements
    def find_elements_by_xpath(self, *args, **kwargs):
        """
        Finds multiple elements by xpath.

        :Args:
         - xpath - The xpath locator of the elements to be found.

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_xpath("//div[contains(@class, 'foo')]")
        """
        return super().find_elements_by_xpath(*args, **kwargs)

    def find_element_by_link_text(self, *args, **kwargs):
        """
        Finds an element by link text.

        :Args:
         - link_text: The text of the element to be found.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_link_text('Sign In')
        """
        return super().find_element_by_link_text(*args, **kwargs)

    @decorators.find_elements
    def find_elements_by_link_text(self, *args, **kwargs):
        """
        Finds elements by link text.

        :Args:
         - link_text: The text of the elements to be found.

        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not

        :Usage:
            elements = driver.find_elements_by_link_text('Sign In')
        """
        return super().find_elements_by_link_text(*args, **kwargs)

    @decorators.find_element
    def find_element_by_partial_link_text(self, *args, **kwargs):
        """
        Finds an element by a partial match of its link text.

        :Args:
         - link_text: The text of the element to partially match on.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_partial_link_text('Sign')
        """
        return super().find_element_by_partial_link_text(*args, **kwargs)

    @decorators.find_elements
    def find_elements_by_partial_link_text(self, *args, **kwargs):
        """
        Finds elements by a partial match of their link text.

        :Args:
         - link_text: The text of the element to partial match on.

        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not

        :Usage:
            elements = driver.find_elements_by_partial_link_text('Sign')
        """
        return super().find_elements_by_partial_link_text(*args, **kwargs)

    @decorators.find_element
    def find_element_by_name(self, *args, **kwargs):
        """
        Finds an element by name.

        :Args:
         - name: The name of the element to find.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_name('foo')
        """
        return super().find_element_by_name(*args, **kwargs)

    @decorators.find_elements
    def find_elements_by_name(self, *args, **kwargs):
        """
        Finds elements by name.

        :Args:
         - name: The name of the elements to find.

        :Returns:
         - list of webelement - a list with elements if any was found.  an
           empty list if not

        :Usage:
            elements = driver.find_elements_by_name('foo')
        """
        return super().find_elements_by_name(*args, **kwargs)

    @decorators.find_element
    def find_element_by_tag_name(self, *args, **kwargs):
        """
        Finds an element by tag name.

        :Args:
         - name - name of html tag (eg: h1, a, span)

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_tag_name('h1')
        """
        return super().find_element_by_tag_name(*args, **kwargs)

    @decorators.find_elements
    def find_elements_by_tag_name(self, *args, **kwargs):
        """
        Finds elements by tag name.

        :Args:
         - name - name of html tag (eg: h1, a, span)

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_tag_name('h1')
        """
        return super().find_elements_by_tag_name(*args, **kwargs)

    @decorators.find_element
    def find_element_by_class_name(self, *args, **kwargs):
        """
        Finds an element by class name.

        :Args:
         - name: The class name of the element to find.

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_class_name('foo')
        """
        return super().find_element_by_class_name(*args, **kwargs)

    @decorators.find_elements
    def find_elements_by_class_name(self, *args, **kwargs):
        """
        Finds elements by class name.

        :Args:
         - name: The class name of the elements to find.

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_class_name('foo')
        """
        return super().find_elements_by_class_name(*args, **kwargs)

    @decorators.find_element
    def find_element_by_css_selector(self, *args, **kwargs):
        """
        Finds an element by css selector.

        :Args:
         - css_selector - CSS selector string, ex: 'a.nav#home'

        :Returns:
         - WebElement - the element if it was found

        :Raises:
         - NoSuchElementException - if the element wasn't found

        :Usage:
            element = driver.find_element_by_css_selector('#foo')
        """
        return super().find_element_by_css_selector(*args, **kwargs)

    @decorators.find_elements
    def find_elements_by_css_selector(self, *args, **kwargs):
        """
        Finds elements by css selector.

        :Args:
         - css_selector - CSS selector string, ex: 'a.nav#home'

        :Returns:
         - list of WebElement - a list with elements if any was found.  An
           empty list if not

        :Usage:
            elements = driver.find_elements_by_css_selector('.foo')
        """
        return super().find_elements_by_css_selector(*args, **kwargs)

    @decorators.find_element
    def find_element(self, *args, **kwargs):
        """
        Find an element given a By strategy and locator. Prefer the find_element_by_* methods when
        possible.

        :Usage:
            element = driver.find_element(By.ID, 'foo')

        :rtype: WebElement
        """
        return super().find_element(*args, **kwargs)

    @decorators.find_elements
    def find_elements(self, *args, **kwargs):
        """
        Find elements given a By strategy and locator. Prefer the find_elements_by_* methods when
        possible.

        :Usage:
            elements = driver.find_elements(By.CLASS_NAME, 'foo')

        :rtype: list of WebElement
        """
        return super().find_elements(*args, **kwargs)

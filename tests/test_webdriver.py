#!/usr/bin/env python

"""Tests for `selenious` decorators package."""

import pytest
from collections import namedtuple
from unittest.mock import patch, MagicMock
from selenium.common.exceptions import NoSuchElementException

from .mock_webdriver import MockDriver
from selenious import WebDriverMixin


def test_all_find_el_are_wrapped(snapshot):
    """All find_* functions are wrapped."""
    driver = MockDriver()
    result = []
    result.append(driver.find_element_by_id("ignored"))
    result.append(driver.find_elements_by_id("ignored"))
    result.append(driver.find_element_by_xpath("ignored"))
    result.append(driver.find_elements_by_xpath("ignored"))
    result.append(driver.find_element_by_link_text("ignored"))
    result.append(driver.find_elements_by_link_text("ignored"))
    result.append(driver.find_element_by_partial_link_text("ignored"))
    result.append(driver.find_elements_by_partial_link_text("ignored"))
    result.append(driver.find_element_by_name("ignored"))
    result.append(driver.find_elements_by_name("ignored"))
    result.append(driver.find_element_by_tag_name("ignored"))
    result.append(driver.find_elements_by_tag_name("ignored"))
    result.append(driver.find_element_by_class_name("ignored"))
    result.append(driver.find_elements_by_class_name("ignored"))
    result.append(driver.find_element_by_css_selector("ignored"))
    result.append(driver.find_elements_by_css_selector("ignored"))
    result.append(driver.find_element("ignored", "twice"))
    result.append(driver.find_elements("ignored", "twice"))
    snapshot.assert_match(result)
    snapshot.assert_match(driver.calls)


def test_time_validators():
    driver = MockDriver(poll_frequency=5, timeout=3)
    with pytest.raises(TypeError, match="timeout 3"):
        driver.implicitly_wait(4)

    driver = MockDriver()
    with pytest.raises(TypeError, match="poll_frequency 0.5"):
        driver.implicitly_wait(5)

    driver = MockDriver(poll_frequency=5, timeout=3)
    with pytest.raises(TypeError, match="timeout 3"):
        driver.implicitly_wait(5)

    driver = MockDriver()
    with pytest.raises(TypeError, match="poll_frequency 0.5"):
        driver.implicitly_wait(5)

    driver = MockDriver()
    driver.implicitly_wait(0.4)
    with pytest.raises(TypeError, match="timeout 0.1"):
        driver.timeout=0.1

    driver = MockDriver()
    driver.implicitly_wait(0.4)
    with pytest.raises(TypeError, match="poll_frequency 0.3"):
        driver.poll_frequency = 0.3
    
def test_stripped_selenious_args(snapshot):
    driver = MockDriver(timeout=1, implicitly_wait=0.1, debounce=1, recover=lambda: 1, poll_frequency=1)
    snapshot.assert_match(driver.calls)


def test_attached(snapshot, mocker):
    # https://changhsinlee.com/pytest-mock/
    # mocker.patch("selenious.decorators.sleep")
    print(type(mocker.patch("selenious.decorators.monotonic", side_effect=[1, 2, 3])))
    driver = MockDriver(timeout=3)
    driver.side_effect = [NoSuchElementException, NoSuchElementException, True]
    try:
        driver.find_element_by_id("whatever")
    except NoSuchElementException:
        pass
    print(driver.calls)
    print("hello")

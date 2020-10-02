#!/usr/bin/env python

"""Tests for `selenious` decorators package."""

import pytest
from collections import namedtuple
from unittest.mock import patch, MagicMock
from selenium.common.exceptions import NoSuchElementException

from .mock_webdriver import MockDriver
from selenious import WebDriverMixin


def test_can(snapshot):
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


def test_attached(snapshot, mocker):
    # https://changhsinlee.com/pytest-mock/
    #mocker.patch("selenious.decorators.sleep")
    print(type(mocker.patch("selenious.decorators.monotonic", side_effect=[1, 2, 3])))
    driver = MockDriver(timeout=3)
    driver.side_effect = [NoSuchElementException, NoSuchElementException, True]
    try:
        driver.find_element_by_id("whatever")
    except NoSuchElementException:
        pass
    print(driver.calls)
    print("hello")

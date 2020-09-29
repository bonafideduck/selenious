#!/usr/bin/env python

"""Tests for `selenious` decorators package."""

import pytest
from collections import namedtuple

from .mock_webdriver import MockDriver


def test_can(snapshot):
    """All find_* functions are wrapped."""
    driver = MockDriver()
    result = []
    result.append(driver.find_element_by_id('ignored'))
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
    el = driver.find_element_by_css_selector()
    snapshot.assert_match(result)
    snapshot.assert_match(driver.calls)



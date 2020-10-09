#!/usr/bin/env python

"""Tests for `selenious` decorators package."""

import pytest
from collections import namedtuple
from unittest.mock import patch, MagicMock
from selenium.common.exceptions import NoSuchElementException

from .mock_webdriver import MockDriver
from selenious import WebDriverMixin
from selenious import decorators


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
        driver.timeout = 0.1

    driver = MockDriver()
    driver.implicitly_wait(0.4)
    with pytest.raises(TypeError, match="poll_frequency 0.3"):
        driver.poll_frequency = 0.3


def test_stripped_selenious_args(snapshot):
    driver = MockDriver(
        timeout=1, implicitly_wait=0.1, debounce=1, recover=lambda: 1, poll_frequency=1
    )
    snapshot.assert_match(driver.calls)


def test_setters():
    driver = MockDriver(
        timeout=1, implicitly_wait=0.1, debounce=1, recover=lambda: 1, poll_frequency=1
    )
    driver.timeout = 1
    assert driver.timeout == 1
    driver.debounce = 2
    assert driver.debounce == 2
    driver.recover = test_setters
    assert driver.recover == test_setters
    driver.poll_frequency = 1
    assert driver.poll_frequency == 1


@pytest.fixture
def driver_plus_decorator_mocks(mocker):
    driver = MockDriver(mocker)
    mocker.patch("selenious.decorators.monotonic", driver.mock_monotonic)
    mocker.patch(
        "selenious.decorators._find_element_next_state", driver.mock_next_state
    )
    return driver


def test_find_element_decorator_raise(snapshot, driver_plus_decorator_mocks):
    """Tests the state machine to test that the driver handles a raise"""
    driver = driver_plus_decorator_mocks
    driver.side_effect = [0, NoSuchElementException, 99, ("raise", 0)]
    with pytest.raises(NoSuchElementException):
        driver.find_element_by_id("_")

    snapshot.assert_match(driver.calls)


def test_find_element_decorator_recover_or_raise_null(
    snapshot, driver_plus_decorator_mocks
):
    """Tests the state machine to test that the driver handles a recover_or_raise with null recover"""
    driver = driver_plus_decorator_mocks
    driver.timeout = 200
    driver.side_effect = [0, NoSuchElementException, 99, ("recover_or_raise", 0)]
    with pytest.raises(NoSuchElementException):
        driver.find_element_by_id("_")

    snapshot.assert_match(driver.calls)



def test_find_element_decorator_recover_or_raise_nonnull(
    snapshot, driver_plus_decorator_mocks
):
    """Tests the state machine to test that the driver handles a recover_or_raise with nonnull recover"""
    driver = driver_plus_decorator_mocks
    driver.timeout = 200
    driver.recover = MagicMock()
    driver.side_effect = [0, NoSuchElementException, 99, ("recover_or_raise", 0), True]
    driver.find_element_by_id("_")
    driver.recover.assert_called()

    snapshot.assert_match(driver.calls)


# def test_find_elements_decorator_x(
#     snapshot, driver_plus_decorator_mocks
# ):
#     """Tests the state machine to test that the driver handles a recover_or_raise with nonnull recover"""
#     driver = driver_plus_decorator_mocks
#     driver.recover = MagicMock()
#     driver.side_effect = [0, NoSuchElementException, 1, ("recover_or_raise", 0), True]
#     driver.find_elements_by_id("_")
#     driver.recover.assert_called()

#     snapshot.assert_match(driver.calls)

    

#     #         return ("debounce", settle_time_remaining)
#     #         return ("success", None)
#     #         return ("recover_or_raise", 0)
#     #         return ("raise", None)
#     # return ("recover_and_retry", min(time_left, poll_frequency))

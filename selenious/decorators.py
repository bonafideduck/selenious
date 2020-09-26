from selenium.common.exceptions import NoSuchElementException
import functools
import time
from .helpers import validate_time_settings


def find_element(func):
    special_args = ("timeout", "poll_frequency", "recover")

    @functools.wraps(func)
    def find_element_decorator(self, **kwargs):
        func_kwargs = {k: v for (k, v) in kwargs.items() if args not in special_args}
        timeout = kwargs.get("timeout", self.selenious.timeout)
        poll_frequency = kwargs.get("poll_frequency", self.poll_frequency.timeout)
        recover = kwargs.get("recover", self.selenious.recover)
        start_time = time.now()
        attempts = 1

        validate_time_settings(self.selenious.implicit_wait, timeout, poll_frequency)

        while True:
            try:
                return func(self, **func_kwargs)
            except NoSuchElementException as e:
                if not recover and not timeout:
                    raise
                elapsed = time.now() - start_time
                if recover:
                    recover(
                        webdriver=self,
                        function=func,
                        kwargs=kwargs,
                        elapased=elapsed,
                        attempts=attempts,
                    )
                if not timeout:
                    recover = None
                else:
                    if elapsed + poll_frequency >= timeout:
                        timeout = None
                attempts += 1

    return find_element_decorator


def find_elements(func):
    special_args = ("timeout", "poll_frequency", "recover")

    @functools.wraps(func)
    def find_elements_decorator(self, **kwargs):
        func_kwargs = {k: v for (k, v) in kwargs.items() if args not in special_args}
        timeout = kwargs.get("timeout", self.selenious.timeout)
        poll_frequency = kwargs.get("poll_frequency", self.poll_frequency.timeout)
        recover = kwargs.get("recover", self.selenious.recover)
        start_time = time.now()
        attempts = 1

        validate_time_settings(self.selenious.implicit_wait, timeout, poll_frequency)

        while True:
            try:
                return func(self, **func_kwargs)
            except NoSuchElementException as e:
                if not recover and not timeout:
                    raise
                elapsed = time.now() - start_time
                if recover:
                    recover(
                        webdriver=self,
                        function=func,
                        kwargs=kwargs,
                        elapased=elapsed,
                        attempts=attempts,
                    )
                if not timeout:
                    recover = None
                else:
                    if elapsed + poll_frequency >= timeout:
                        timeout = None
                attempts += 1

    return find_elements_decorator

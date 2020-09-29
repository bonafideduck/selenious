from selenium.common.exceptions import NoSuchElementException
import functools
import time
from .helpers import validate_time_settings


def find_element(func):
    special_args = ("timeout", "poll_frequency", "recover")

    @functools.wraps(func)
    def find_element_decorator(self, *args, **kwargs):
        func_kwargs = {k: v for (k, v) in kwargs.items() if args not in special_args}
        timeout = kwargs.get("timeout", self._selenious.timeout)
        poll_frequency = kwargs.get("poll_frequency", self._selenious.poll_frequency)
        recover = kwargs.get("recover", self._selenious.recover)
        start_time = time.monotonic()
        attempts = 1

        validate_time_settings(self._selenious.implicit_wait, timeout, poll_frequency)

        while True:
            try:
                return func(self, *args, **func_kwargs)
            except NoSuchElementException as e:
                if not recover and not timeout:
                    raise
            elapsed = time.monotonic() - start_time
            if recover:
                recover(
                    webdriver=self,
                    function=func,
                    args=args,
                    kwargs=kwargs,
                    elapased=elapsed,
                    attempts=attempts,
                )
            time.sleep(max(0, min(timeout, poll_frequency)))
            if not timeout:
                recover = None
            else:
                if elapsed + poll_frequency >= timeout:
                    timeout = 0
            attempts += 1

    return find_element_decorator


def find_elements(func):
    special_args = ("timeout", "poll_frequency", "recover", "min", "debounce")

    @functools.wraps(func)
    def find_elements_decorator(self, *args, **kwargs):
        func_kwargs = {k: v for (k, v) in kwargs.items() if args not in special_args}
        timeout = kwargs.get("timeout", self._selenious.timeout)
        poll_frequency = kwargs.get("poll_frequency", self._selenious.poll_frequency)
        recover = kwargs.get("recover", self._selenious.recover)
        min = kwargs.get("min", 0)
        debounce = kwargs.get("debounce", self._selenious.debounce)
        debounce = poll_frequency if debounce is True else debounce
        start_time = time.monotonic()
        attempts = 1
        prev_len = 0
        prev_time = start_time

        validate_time_settings(self._selenious.implicit_wait, timeout, poll_frequency)

        while True:
            retval = func(self, *args, **func_kwargs)
            if not min and not debounce:
                return retval
            length = len(retval)
            now = None
            debouncing = False

            if length >= min:
                if debounce:
                    if timeout:
                        now = time.monotonic()
                        elapsed = now - start_time
                        if elapsed >= timeout:
                            return retval
                    if prev_len == length:
                        now = now or time.monotonic()
                        if now - prev_time >= debounce:
                            return retval
                    else:
                        prev_len = length
                        prev_start_time = now
                    debouncing = True
                else:
                    return retval
            elif min and not recover:
                now = time.monotonic()
                elapsed = now - start_time
                if elapsed >= timeout:
                    raise  NoSuchElementException(f'{length} elements is less than min of {min}')

            now = now or time.monotonic()
            elapsed = now - start_time
            if recover:
                recover(
                    webdriver=self,
                    function=func,
                    args=args,
                    kwargs=kwargs,
                    elapased=elapsed,
                    attempts=attempts,
                    elements=retval,
                )
            time.sleep(max(0, min(timeout, poll_frequency)))
            if not timeout:
                recover = None
            else:
                if elapsed + poll_frequency >= timeout:
                    timeout = 0
            attempts += 1

    return find_elements_decorator

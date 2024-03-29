# Selenious

[![version](https://img.shields.io/pypi/v/selenious.svg)](https://pypi.python.org/pypi/selenious)
[![downloads](https://img.shields.io/pypi/dm/selenious.svg)](https://pypi.python.org/pypi/selenious)
[![sanity](https://github.com/bonafideduck/selenious/workflows/Sanity/badge.svg)](https://github.com/bonafideduck/selenious/actions?query=branch%3Amaster+workflow%3A%22Sanity%22)
[![docs](https://readthedocs.org/projects/selenious/badge/?version=latest)](https://selenious.readthedocs.io/en/latest/?badge=latest)

Enhances Selenium with timeouts and recover capabilities.


* Free software: BSD license
* Documentation: https://selenious.readthedocs.io.


Introduction
============

Selenious enhances Selenium WebDriver ``find_element*`` functions to have a
``timeout``, ``poll_frequency``, and ``recover``.  The ``find_elements*``
functions are additionally enhanced with ``debounce`` and ``min`` settings.

Selenium already has an ``implicitly_wait`` and a ``WebDriverWait`` function.
Neither of these have the versatility and natural feel that Selenious gives
the code.  To add a 5 second timeout to a single call, Selenious would
be::

    driver.find_element_by_id('popup', timeout=5)

While with ``implicitly_wait`` the code would be::

    driver.implicitly_wait(5)
    driver.find_element_by_id('popup')
    driver.implicitly_wait(hopefully_you_know_what_the_setting_was_before)

And ``WebDriverWait`` would be::

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "popup"))
    )

Features
========

Enhancement to the find_element function
----------------------------------------

* ``timeout`` - The maximum time in seconds to wait for a succesful find.

* ``poll_frequency`` - How often to poll the driver for the element

* ``debounce`` - For ``find_elements*`` wait for this time period for the count to not change.

* ``min`` - For ``find_elements*`` the minimum count to find.

* ``recover`` - If the item or min items are not found, call this periodically and try again.

Drop-in replacement for selenium webdriver
------------------------------------------

Instead of ``from selenium.webdriver import Chrome`` a convenience
of ``from selenious.webdriver import Chrome`` can be used that
imports the ``SeleniousMixin`` for you.


Settings can be set in the function or globally
-----------------------------------------------

Locally, `webdriver.find_element_by_id('id', timeout=5)`, or globaly,
``webdriver.timeout = 5``.


Support of recover() for click()
-------------------------------

If a click() command raises an exception, if set, the `recover()` function 
will be called once and the click attempted again.  This allows for recovering
from such events as a modal popup being shown or the button has scrolled out
of view.


No deprecation of the find_element[s]_by_* methods
--------------------------------------------------

The developers of selenium have made the decision to deprecate redundant
functions such as `find_element_by_id(id_)` with the common function
and a `By` parameter.  `find_element(By.ID, id_)`.  Selenious will continue
to support these convenience functions and not print a warning.



Credits
=======

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

* [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [`audreyr/cookiecutter-pypackage`](https://github.com/audreyr/cookiecutter-pypackage)

# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots["test_can 1"] = [
    True,
    [True],
    True,
    [True],
    True,
    [True],
    True,
    [True],
    True,
    [True],
    True,
    [True],
    True,
    [True],
    True,
    [True],
    True,
    [True],
]

snapshots["test_can 2"] = [
    {"args": ("ignored",), "kwargs": {}, "name": "find_element_by_id", "retval": True},
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_elements_by_id",
        "retval": [True],
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_element_by_xpath",
        "retval": True,
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_elements_by_xpath",
        "retval": [True],
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_element_by_link_text",
        "retval": True,
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_elements_by_link_text",
        "retval": [True],
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_element_by_partial_link_text",
        "retval": True,
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_elements_by_partial_link_text",
        "retval": [True],
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_element_by_name",
        "retval": True,
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_elements_by_name",
        "retval": [True],
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_element_by_tag_name",
        "retval": True,
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_elements_by_tag_name",
        "retval": [True],
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_element_by_class_name",
        "retval": True,
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_elements_by_class_name",
        "retval": [True],
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_element_by_css_selector",
        "retval": True,
    },
    {
        "args": ("ignored",),
        "kwargs": {},
        "name": "find_elements_by_css_selector",
        "retval": [True],
    },
    {
        "args": ("ignored", "twice"),
        "kwargs": {},
        "name": "find_element",
        "retval": True,
    },
    {
        "args": ("ignored", "twice"),
        "kwargs": {},
        "name": "find_elements",
        "retval": [True],
    },
]
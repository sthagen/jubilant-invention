# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest  # type: ignore

from subtractor.subtractor import process, slugify


def test_process_ok_test_mock_valid_handler():
    def mock_valid_message(arg):
        _ = arg
        return True, "test"

    good, bad = 42, -1
    ok, message, good, bad = process(None, mock_valid_message, good, bad)
    assert ok is True
    assert message == "test"
    assert good == 42 + 1
    assert bad == -1


def test_process_nok_test_mock_invalid_handler():
    def mock_invalid_message(arg):
        _ = arg
        return False, "test"

    good, bad = 42, -1
    ok, message, good, bad = process(None, mock_invalid_message, good, bad)
    assert ok is False
    assert message == "test"
    assert good == 42
    assert bad == 0


def test_slugify_ok_empty():
    assert slugify('') == ''


def test_slugify_ok_no_newline():
    assert slugify("one line") == "one line"


def test_slugify_ok_with_single_newline():
    assert slugify("one line\nanother line") == "one line another line"


def test_slugify_as_to_bs_ok():
    assert slugify("aaabb", these=("a",), those=("b",)) == "bbbbb"


def test_slugify_as_and_bs_to_cs_ok():
    assert slugify("aaabb", these=("a", "b"), those=("c",)) == "ccccc"


def test_slugify_as_and_bs_to_cs_and_ds_resp_ok():
    assert slugify("aaabb", these=("a", "b"), those=("c", "d")) == "cccdd"


def test_slugify_as_to_bs_and_cs_mok():
    with pytest.raises(ValueError):
        slugify("aaabb", these=("a",), those=("b", "c"))


def test_slugify_nok_with_single_newline_but_empty_source_and_target():
    text = "one line\nanother line"
    assert slugify(text, these=[], those=[]) == text


def test_slugify_nok_with_single_newline_but_empty_source():
    text = "one line\nanother line"
    assert slugify(text, these=[]) == text


def test_slugify_nok_with_single_newline_but_empty_target():
    text = "one line\nanother line"
    assert slugify(text, those=[]) == text

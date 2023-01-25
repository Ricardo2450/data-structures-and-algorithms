import pytest
from python.code_challenges.merge_sort import merge_sort



# @pytest.mark.skip("TODO")
def test_merge_sort_exists():
    assert merge_sort


# @pytest.mark.skip("TODO")
def test_merge_sort_input_list():
    actual = merge_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_merge_sort_reverse_sorted():
    actual = merge_sort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_merge_sort_few_uniques():
    actual = merge_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_merge_sort_nearly_sorted():
    actual = merge_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_merge_sort_empty_list():
    actual = merge_sort([])
    expected = []
    assert actual == expected



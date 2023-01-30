import pytest
from data_structures.hashtable import Hashtable
def test_exists():
    assert Hashtable

# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_get_silent():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.get("silent")
    expected = True
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_has_listen():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.has("listen")
    expected = True
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_has_not_in_table():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.has("jason")
    expected = False
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_keys_3():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.keys()
    expected = ["ahmad", "listen", "silent"]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_keys_diff_types():
    hashtable = Hashtable()
    hashtable.set(45, 30)
    hashtable.set("silent", True)
    hashtable.set(7.9, "to me")
    actual = hashtable.keys()
    expected = [7.9, 45, "silent"]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_keys_empty():
    hashtable = Hashtable()
    actual = hashtable.keys()
    expected = []
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_hash_silent():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.hash("silent")
    expected = hash("silent") % 10
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = []
    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())
    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]
    assert actual == expected

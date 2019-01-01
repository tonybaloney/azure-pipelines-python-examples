from unittest import TestCase

from demolib import code


class ExampleTestCase(TestCase):
    def test_example():
        ret = code.example()
        assert ret == "banana!"

from unittest import TestCase

from demolib import code


class ExampleTestCase(TestCase):
    def test_example(self):
        ret = code.example()
        assert ret == "banana!"

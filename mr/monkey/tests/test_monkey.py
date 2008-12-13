from unittest import TestCase, defaultTestLoader
import warnings

from mr.monkey import replace, wrap
from mr.monkey import MonkeyWarning, MonkeySignatureWarning

import mock


class MonkeyTests(TestCase):
    def setUp(self):
        reload(mock)
        warnings.filterwarnings('ignore', category=MonkeyWarning)
        warnings.filterwarnings('ignore', category=MonkeySignatureWarning)

    def testReplace(self):
        self.assertEqual(mock.foo(), (1, 2, 3))
        self.assertEqual(mock.foo(3), 3)
        def bar(result=None):
            return 3, 2, 1
        replace(mock.foo, bar)
        self.assertEqual(mock.foo(), (3, 2, 1))
        self.assertEqual(mock.foo(3), (3, 2, 1))

    def testWrap(self):
        self.assertEqual(mock.foo(), (1, 2, 3))
        self.assertEqual(mock.foo(3), 3)
        def bar(func, *args, **kwargs):
            return func(*args, **kwargs) * 2
        wrap(mock.foo, bar)
        self.assertEqual(mock.foo(), (1, 2, 3, 1, 2, 3))
        self.assertEqual(mock.foo(3), 6)


def test_suite():
    return defaultTestLoader.loadTestsFromName(__name__)

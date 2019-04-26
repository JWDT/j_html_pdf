import unittest

from j_html_pdf.html_simple import HtmlReport


class TestHtmlSimple(unittest.TestCase):
    def test_all_empty(self):
        self.assertRaises(AttributeError, HtmlReport)

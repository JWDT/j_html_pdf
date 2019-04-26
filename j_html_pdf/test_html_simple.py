import unittest

from j_html_pdf.html_simple import HtmlReport


class TestHtmlSimple(unittest.TestCase):
    test_html_empty = (
        '''<p>This is a paragraph.</p>
        <p>This is another paragraph.</p>''',
        '''<p>
        This paragraph
        contains a lot of lines
        in the source code,
        but the browser 
        ignores it.
        </p>

        <p>
        This paragraph
        contains         a lot of spaces
        in the source         code,
        but the        browser 
        ignores it.
        </p>
        ''',
        '<ul>\n'
        '<li>Coffee</li>\n'
        '<li>Tea</li>\n'
        '<li>Milk</li>\n'
        '</ul>\n'
        ''
    )
    test_html_1 = {
        '''<p>This is a $name$.</p>
        <p>This is another $website$.</p>''': '''<p>This is a John Thomson.</p>
        <p>This is another https://jwdt.co.uk.</p>''',
        '''<p>
        This paragraph
        contains a lot of lines
        in the source code,
        but the browser 
        ignores it.
        </p>
    
        <p>
        This $email$
        contains         a lot of spaces
        in the source         code,
        but the        browser 
        ignores it.
        </p>
        ''': '''<p>
        This paragraph
        contains a lot of lines
        in the source code,
        but the browser 
        ignores it.
        </p>
    
        <p>
        This john@example.com
        contains         a lot of spaces
        in the source         code,
        but the        browser 
        ignores it.
        </p>
        ''',
        '<ul>\n'
        '<li>$name$</li>\n'
        '<li>$email$</li>\n'
        '<li>$website$</li>\n'
        '</ul>\n'
        '': '<ul>\n'
        '<li>John Thomson</li>\n'
        '<li>john@example.com</li>\n'
        '<li>https://jwdt.co.uk</li>\n'
        '</ul>\n'
        ''
    }
    test_data_1 = {
            'name': 'John Thomson',
            'email': 'john@example.com',
            'website': 'https://jwdt.co.uk'
        }

    def test_all_empty(self):
        self.assertRaises(AttributeError, HtmlReport)

    def test_with_both_template_and_template_file(self):
        self.assertRaises(AttributeError, HtmlReport, template='<html></html>', template_file='index.html')

    def test_with_just_template(self):
        for sample in self.test_html_empty:
            self.assertEqual(sample, HtmlReport(template=sample).to_html())

    def test_with_template_and_data(self):
        for sample in self.test_html_empty:
            self.assertEqual(sample, HtmlReport(data=self.test_data_1, template=sample).to_html())
        for sample, result in self.test_html_1.items():
            self.assertEqual(result, HtmlReport(data=self.test_data_1, template=sample).to_html())

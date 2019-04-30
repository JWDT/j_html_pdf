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
    test_files_empty = (
        'basic_html_template.html',
        'complex_html_template.html'
    )

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

    def test_with_just_template_file(self):
        for file_name in self.test_files_empty:
            with open('test_data/' + file_name) as file:
                self.assertEqual(file.read(), HtmlReport(template_file='test_data/' + file_name).to_html())
                # HtmlReport(template_file='test_data/' + file_name).to_pdf('test_data/' + file_name + '.pdf')

    # def test_with_template_file_and_data(self):
    #     with open('test_data/basic_html_template_with_output.html') as output_file:
    #         self.assertEqual(output_file.read(),
    #                          HtmlReport(self.test_data_1, template_file='test_data/basic_html_template_with_data.html')
    #                          .to_html())
            # HtmlReport(data=self.test_data_1, template_file='test_data/basic_html_template_with_data.html').\
            #     to_pdf('test_data/basic_html_template_with_output.html.pdf')
        # with open('test_data/basic_html_template_with_output.html.pdf', mode='rb') as output_file:
        #     self.assertEqual(output_file.read(),
        #                     HtmlReport(self.test_data_1, template_file='test_data/basic_html_template_with_data.html')
        #                      .to_pdf())
        # Apparently you can't test PDF files, as they have a "created date" somewhere which messes up this.

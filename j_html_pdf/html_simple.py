class HtmlReport:
    template: str
    data: dict

    def __init__(self,
                 data: dict = None,
                 template: str = None,
                 template_file=None):
        if template and template_file:
            raise AttributeError("HTMLReport requires either template OR template_file.")
        if template:
            self.template = template
        elif template_file:
            with open(template_file) as file:
                self.template = file.read()
        else:
            raise AttributeError("HTMLReport requires either template or template_file.")
        self.data = data

    def to_html(self):
        html = self.template
        if not self.data:
            return html
        for key, value in self.data.items():
            if type(value) is list:
                new_val = ''
                for item in value:
                    new_val = f'<li>{item}</li>'
                value = new_val
            html = html.replace(f'${key}$', str(value))
        return html

    def to_pdf(self, outfile=None, page_size='A4', margin='0.33cm'):
        html = self.to_html()
        from weasyprint import HTML, CSS
        css = f'''
        @page {{
            size: {page_size};
            margin: {margin};
        }}
        '''
        return HTML(string=html).write_pdf(target=outfile, presentational_hints=True,
                                           stylesheets=[CSS(string=css)])


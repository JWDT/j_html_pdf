class HtmlReport:
    template: str
    data: dict

    def __init__(self, data: dict = None, template: str = None, template_file=None):
        if not template and not template_file:
            raise AttributeError("HTMLReport requires either template or template_file.")
        elif template and template_file:
            raise AttributeError("HTMLReport requires either template OR template_file.")
        if template:
            self.template = template
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

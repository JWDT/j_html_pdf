class HtmlReport:
    def __init__(self, data: dict={}, template=None, template_file=None):
        if not template and not template_file:
            raise AttributeError("HTMLReport Requires either template or template_file.")

class ModuleDeclarationMissingException(Exception):
    def __init__(self, filename):
        self.message = """\
-- EMPTY MODULE --------------------------------------------- {0}

I ran into something unexpected when parsing your code!


I am looking for one of the following things:

    a definition or type annotation
    a port declaration
    a type declaration
    an import
    an infix declaration
    whitespace""".format(filename)
        super().__init__(self.message)

    def __call__(self, *args, **kwargs):
        raise self
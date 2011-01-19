# Middleware to translate request headers

class TranslateHeaders(object):
    def __init__(self, app, translations):
        self.translations = translations
        self.app = app
        
    def __call__(self, environ, start_response):
        for (name, repl) in self.translations.iteritems():
            if name in environ:
                environ[repl] = environ.pop(name)
        return self.app(environ, start_response)
    
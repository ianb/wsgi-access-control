## FIXME: should add Access-Control-Max-Age

class AccessControlMiddleware(object):

    def __init__(self, app, allow_origin, allow_methods, allow_headers=None,
                 expose_headers=None):
        self.app = app
        self.allow_origin = allow_origin
        if not isinstance(allow_methods, basestring):
            allow_methods = ', '.join(allow_methods)
        self.allow_methods = allow_methods
        if allow_headers and not isinstance(allow_headers, basestring):
            allow_headers = ', '.join(allow_headers)
        self.allow_headers = allow_headers
        if expose_headers and not isinstance(expose_headers, basestring):
            expose_headers = ', '.join(expose_headers)
        self.expose_headers = expose_headers
        self.base_headers = [
            ('Access-Control-Allow-Methods', self.allow_methods)]
        if self.allow_origin != '*':
            self.base_headers.append(
                ('Access-Control-Allow-Origin', self.allow_origin))
        if self.allow_headers:
            self.base_headers.append(
                ('Access-Control-Allow-Headers', self.allow_headers))
        if self.expose_headers:
            # FIXME: first, headers isn't the name
            # Second, like Allow-Origin, maybe this can't be folded?
            self.base_headers.append(
                ('Access-Control-Expose-Header', self.expose_headers))

    def __call__(self, environ, start_response):
        if environ['REQUEST_METHOD'] == 'OPTIONS':
            app = self.options_app
        else:
            app = self.app
        def repl_start_response(status, headers, exc_info=None):
            headers.extend(self.base_headers)
            # Fixes: http://code.google.com/p/chromium/issues/detail?id=67743
            if self.allow_origin == '*':
                origin = environ.get('HTTP_ORIGIN', '*')
                headers.append(
                    ('Access-Control-Allow-Origin', origin))
            if 'Chrome' in environ.get('HTTP_USER_AGENT', ''):
                headers = self.filter_chrome_headers(headers)
            return start_response(status, headers, exc_info)
        return app(environ, repl_start_response)

    def filter_chrome_headers(self, headers):
        new_headers = []
        for name, value in headers:
            if not name.lower().startswith('X-'):
                new_headers.append((name, value))
        return new_headers

    def remove_header(self, headers, remove_name):
        remove_name = remove_name.lower()
        for name, value in headers:
            if name.lower() == remove_name:
                headers.remove((name, value))
                break

    def options_app(self, environ, start_response):
        start_response('200 OK', [])
        return ['']

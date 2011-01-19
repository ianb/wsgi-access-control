WSGI Access-Control Middleware
==============================

This is a simple middleware for adding Access-Control-\* headers to
your application, allowing `Cross-Origin Resource Sharing
<http://www.w3.org/TR/cors/>`_ -- basically meaning that you can use
XMLHttpRequest from one domain to access resources on another domain.

The middleware is located in
`wsgiaccesscontrol.accesscontrol.AccessControl`.

Example of use
--------------

This is the code that we use to make the Firefox Sync web service available
across origins (domains)::

    application = AccessControlMiddleware(
        application, allow_origin='*',
        allow_methods=('GET','POST','PUT','DELETE','OPTIONS'),
        allow_headers=('X-Authorization', 'Authorization',
                       'X-If-Modified-Since', 'X-If-Unmodified-Since',
                       'Content-Type'),
        expose_headers=('X-Weave-Timestamp', 'X-Weave-Backoff',
                        'X-Weave-Alert', 'X-Weave-Records'))

Note that there is a little workaround for a `Chrome bug
<http://code.google.com/p/chromium/issues/detail?id=67743>`_ that
turns ``*`` into a dynamic Access-Control-Allow-Origin header (copying
the Origin request header).  A simple future feature is to allow a
whitelist of origins (instead of just a single domain or wildcard),
which also requires a dynamic Allow-Origin header (because the header
is only allowed to include one value).

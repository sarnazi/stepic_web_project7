def app(environ,start_response):
    status='200 ok'
    headers=[    
        ('Content-Type','text/plain')
    ]
    resp=environ['QUERY_STRING'].split('&')
    resp=[item +'\r\n' for item in resp]
    start_response(status,headers)
    return 'resp'


import cStringIO
def hello(env,st_res):
    statu='200 ok'
    headres=[
        ('Content-Type','text/plain')
    ]
    length=int(env.get('CONTENT_LENTH','0'))
    body=cStringIO.StringIO(env['wsgi.input'].read(length))
    sr_res(status,headers)
    return [ body ]


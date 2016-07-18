from flask import Flask, make_response

app = Flask(__name__)

@app.route('/string/')
def return_string():
    return"hello, world!"

@app.route('/object/')
def return_object():
    headers = {'Content-Type': 'text/plain'}
    return make_response("hello, world!", status=200,headers=headers)

@app.route('/tuple/')
def return_tuple():
    return "hello, world!", 200, {'Content-Type':'text/plain'}

from flask import request

def dump_request_detail(request):
    dump_request_detail(request):
    request_detail = """
#BEFORE REQUEST#
request.endpoint: {request.endpoint}
request.method: {request.method}
request.view_args: {request.view_args}
request.args: {request.args}
request.form: {request.form}
request.user_agent: {request.user_agent}
request.files: {request.files}
request.is_xhr: {request.is_zhr}

##request.headers##
{request.headers}
    """.format(request=request).strip()
    return request_detail

@app.before_request
def callme_after_every_request(request):
    #Demo only: the before_request hook.
app.logger.debug(dump_request_detail(request))

@app.after_request
def callme_after_every_response(response):
    #Demo only: the after_request hook.
app.logger.debug('# After Request #\n' + repr(response))
return response


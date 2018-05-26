def application(enviorn, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return '<b>Hello Yangying</b>'
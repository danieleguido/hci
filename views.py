from django.shortcuts import render_to_response
from django.template import RequestContext

# public features
def index(request):
	c = RequestContext(request, {})
	return render_to_response('hci/index.html', c)# Create your views here.

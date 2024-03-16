from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def hello(request):
  template = loader.get_template('mysecond.html')
  return HttpResponse(template.render())
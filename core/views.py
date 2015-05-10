from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from pprint import pprint


def generic_view(request, **data):
    pprint(request.META.get('HTTP_X_REQUESTED_WITH'))
    if request.is_ajax():
        data['base_template'] = 'ajax.html'
        html = render_to_string(data['template'], data)
        print 'in generic_view'
        return HttpResponse(html, content_type='text/html')
    print "outside if of generic_view "
    print "data: ", data
    print "template: ", data['template']
    return render(request, data['template'], data)
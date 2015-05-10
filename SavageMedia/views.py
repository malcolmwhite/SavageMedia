# from django.template.loader import render_to_string
# from django.shortcuts import render
# from django.http import HttpResponse
#
#
# def generic_view(request, **data):
#     if request.is_ajax():
#         data['base_template'] = 'ajax.html'
#         html = render_to_string(data['template'], data)
#         return HttpResponse(html, content_type='text/html')
#     return render(request, data['template'], data)
#

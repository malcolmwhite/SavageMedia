from django.conf.urls import patterns, url

from core.views import generic_view


home_template_info = {
    'base_template': 'core/base.html',
    'active_link': '#home',
    'template': 'home/index.html',
}

urlpatterns = patterns('',
                       url(r'^/?$', generic_view, home_template_info, name="home"),
                       )
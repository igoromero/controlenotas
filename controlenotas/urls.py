from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'boletim.views.index'),
    url(r'adiciona/$', 'boletim.views.adiciona'),
    url(r'item/(?P<id_disciplina>\d+)/$', 'boletim.views.item'),
    url(r'remove/(?P<id_disciplina>\d+)/$', 'boletim.views.remove'),
    url(r'login/', "django.contrib.auth.views.login", {
            "template_name": "login.html"}),
    url(r'logout/', "django.contrib.auth.views.logout_then_login", {
            'login_url': "/login/"}),
    # url(r'^controlenotas/', include('controlenotas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

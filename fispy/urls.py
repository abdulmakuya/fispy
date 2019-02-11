
from django.conf.urls import url
from django.contrib import admin
from events import views
from graduators import views

#for static root upload
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),

    url(r'^fispy/$', views.home, name='home'),

    #the error loading events view,was solved by assigning a view called
    #event in views of graduator app
    url(r'^events/$', views.newname2, name='event'),

    #/graduators/      (all graduators are listed)
    url(r'^graduators/$' , views.newname, name='graduator'),

    # /graduators/001  (single detailed response of individual graduator)
    url(r'^graduators/(?P<graduator_id>[0-9]+)/$', views.details, name='detail')
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

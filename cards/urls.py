from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'cards.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cardapp/', include('cardapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

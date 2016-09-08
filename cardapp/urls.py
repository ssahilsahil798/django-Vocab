from django.conf.urls import url, include
from tastypie.api import Api
from cardapp.api import LearntWordResource, CardStatusResource, WordStatusResource, UserResource, CardCategoryResource, WordResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(CardCategoryResource())
v1_api.register(WordResource())
v1_api.register(LearntWordResource())
v1_api.register(WordStatusResource())
v1_api.register(CardStatusResource())
urlpatterns = [
            url(r'^api/', include(v1_api.urls)),
        ]

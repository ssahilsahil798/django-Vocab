
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS, ALL
from cardapp.models import CardCategory, Word
from django.contrib.auth.models import User
from tastypie import fields
#from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication
from django.conf.urls import url
from tastypie.utils import trailing_slash
from django.contrib.auth import authenticate
#from tastypie.authorization import Authorization
#from tastypie.exceptions import Unauthorized
from tastypie.models import create_api_key
from django.db.models import signals
#import requests
from tastypie.http import HttpNotFound
from tastypie.serializers import Serializer
#import datetime
import logging
logger = logging.getLogger('djangoapp')
#from django.views.debug import CLEANSED_SUBSTITUTE
#from django.conf import settings
#from tastypie.utils.mime import determine_format
#from tastypie.exceptions import BadRequest, UnsupportedFormat
#from tastypie.serializers import Serializer
#from django.db import connection
#from decimal import Decimal
#from django.core.exceptions import ValidationError
#from django.contrib.auth import authenticate, login, logout
#from tastypie.fields import CharField, DecimalField


#import time

class MultipartResource(object):
    '''
    A class that enables us to put
    multipart resources on classes
    '''
    def deserialize(self, request, data, format=None):
            if not format:
                format = request.META.get('Content-Type', 'application/json')

            if format == 'application/x-www-form-urlencoded':
                return request.POST

            if format.startswith('multipart'):
                data = request.POST.copy()
                data.update(request.FILES)
                return data

            return super(MultipartResource, self).deserialize(request, data, format)




signals.post_save.connect(create_api_key, sender=User)

class UserResource(MultipartResource, ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'is_superuser']
	always_return_data = True
        allowed_methods = ['get','post']
        serializer = Serializer()


    def prepend_urls(self):

        return [
            url(r'^(?P<resource_name>%s)/auth/login%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login')),
            url(r'^(?P<resource_name>%s)/register%s$' %
            	(self._meta.resource_name, trailing_slash()),
            	self.wrap_view('register')),
            url(r'^(?P<resource_name>%s)/auth/(?P<username>[\w\d_.-]*)%s$' %
            	(self._meta.resource_name, trailing_slash()),
            	self.wrap_view('confirmation')),
    	]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        print 'sahil'
        data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/x-www-form-urlencoded'))
        username = data.get('username', '')
        password = data.get('password', '')
        print username + "this is username"
	print User.objects.filter(username=username).count()

        if User.objects.filter(username=username).count() == 0:
            print "reached here"
    	    return self.create_response(request, {"api_key": "username","HttpNotFound": "username doesnot exist"}, HttpNotFound)
        else:
            user = authenticate(username=username, password=password)

            return self.create_response(request, {"api_key": User.objects.get(username=username).api_key.key, "username": username })




    def register(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        data = self.deserialize(request, request.body, format='multipart')
        username = data.get('username', '')
        password = data.get('password', '')
        image = data.get('image', '')
        print image
        print str(User.objects.filter(username=username).count()) + "sahil"
        if User.objects.filter(username=username).count()==0:
            user = User(username=username, password=password)
            user.save()
            print user.username
            curr_user = authenticate(username=username, password=password)
            print curr_user.username
            return self.create_response(request, {"api_key": User.objects.get(username=username).api_key.key, "username": username, "created": 1})

        else:
            return self.create_response(request, {"error": "Username already in database. Chose different username"})


class CardCategoryResource(ModelResource):
    print 'reached'
    class Meta:
        queryset = CardCategory.objects.all()
        resource_name = 'cardcategory'
	always_return_data = True
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        filtering = {
                'alias': ALL
            }

class WordResource(ModelResource):
    category = fields.ForeignKey(CardCategoryResource, 'category', full=True)
    class Meta:
        queryset = Word.objects.all()
        resource_name = 'word'
	always_return_data = True
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        filtering = {
                'category': ALL_WITH_RELATIONS
            }






from django.conf.urls import url
from .views import *

urlpatterns = [
	# Index
    url(r'^$', index, name='index'),
]

"""mealcounter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# Import URLS
from mealcounter.core import urls as core_urls
from mealcounter.accounts import urls as accounts_urls 
from mealcounter.meal import urls as meal_urls 

urlpatterns = [
    url(r'^', include(core_urls, namespace='core')),
    url(r'^accounts/', include(accounts_urls, namespace='accounts')),
	url(r'^', include(meal_urls, namespace='meal')),
    url(r'^admin/', admin.site.urls),
]

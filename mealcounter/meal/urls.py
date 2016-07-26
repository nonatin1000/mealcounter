from django.conf.urls import url
from .views import *

urlpatterns = [
	# Autocomplete
	url(r'^item-meal-autocomplete/$', ItemMealAutocomplete.as_view(), name='item_meal_autocomplete'),
	# Meal
	url(r'^meal/list/$', MealList.as_view(), name='meal_list'),
    url(r'^meal/add/$', MealCreate.as_view(), name='meal_add'),
	url(r'^meal/details/(?P<pk>[0-9]+)/$', MealDetail.as_view(), name='meal_details'),
	url(r'^meal/edit/(?P<pk>[0-9]+)/$', MealUpdate.as_view(), name='meal_edit'),
	url(r'^meal/(?P<pk>[0-9]+)/delete/$', MealDelete.as_view(), name='meal_delete'), 
	# ItemMeal
	url(r'^itemmeal/list/$', ItemMealList.as_view(), name='item_meal_list'),
    url(r'^itemmeal/add/$', ItemMealCreate.as_view(), name='item_meal_add'),
	url(r'^itemmeal/details/(?P<pk>[0-9]+)/$', ItemMealDetail.as_view(), name='item_meal_details'),
	url(r'^itemmeal/edit/(?P<pk>[0-9]+)/$', ItemMealUpdate.as_view(), name='item_meal_edit'),
	url(r'^itemmeal/(?P<pk>[0-9]+)/delete/$', ItemMealDelete.as_view(), name='item_meal_delete'), 
	# Plate
	url(r'^plate/list/$', PlateList.as_view(), name='plate_list'),
    url(r'^plate/add/$', PlateCreate.as_view(), name='plate_add'),
	url(r'^plate/details/(?P<pk>[0-9]+)/$', PlateDetail.as_view(), name='plate_details'),
	url(r'^plate/edit/(?P<pk>[0-9]+)/$', PlateUpdate.as_view(), name='plate_edit'),
	url(r'^plate/(?P<pk>[0-9]+)/delete/$', PlateDelete.as_view(), name='plate_delete'), 
]

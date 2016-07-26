# -*- coding: utf-8 -*-

from django import forms
from .models import *
from dal import autocomplete
from django.db.models import Sum
from django.db.models.functions import Coalesce

class MealForm(forms.ModelForm):
	
	class Meta:
		model = Meal
		fields = ('__all__')
		widgets = {'item_meal': autocomplete.ModelSelect2Multiple(url='meal:item_meal_autocomplete')}

class ItemMealForm(forms.ModelForm):
	
	class Meta:
		model = ItemMeal
		fields = '__all__'

class PlateForm(forms.ModelForm):
	
	class Meta:
		model = Plate
		fields = '__all__'
		widgets = {'item_meal': autocomplete.ModelSelect2Multiple(url='meal:item_meal_autocomplete')}

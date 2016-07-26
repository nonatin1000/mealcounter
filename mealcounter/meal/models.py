# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from mealcounter.meal.models import *
from django.core.validators import MinValueValidator
from django.db.models import Sum
from django.db.models.functions import Coalesce

class AuditModel(models.Model):
	# Audit Fields
	created_on = models.DateTimeField('Criado em', auto_now_add=True)
	updated_on = models.DateTimeField('Autalizado em', auto_now=True)

	class Meta:
		abstract=True

class ItemMeal(AuditModel):

	name = models.CharField('Nome', max_length=100)
	amount = models.IntegerField('Quantidade')
	value = models.DecimalField('Valor', max_digits=9, decimal_places=2)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('meal:item_meal_list')

	class Meta:
		verbose_name = 'Item Refeição'
		verbose_name_plural = 'Itens da Refeição'
		ordering = ['-id']

class Meal(AuditModel):

	meal_date = models.DateField('Data da Refeição')
	name = models.CharField('Descricao', max_length=100)
	estimate = models.IntegerField('Estimativa')
	start_time = models.TimeField('Inicio da Refeição')
	end_time = models.TimeField('Fim da Refeição')
	amount = models.IntegerField('Quantidade', default=0)
	status = models.BooleanField('Ativo')

	item_meal = models.ManyToManyField(ItemMeal, verbose_name='Itens', related_name='meals')

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('meal:meal_list')

	class Meta:
		verbose_name = 'Refeição'
		verbose_name_plural = 'Refeições'
		ordering = ['-id']

class Plate(AuditModel):

	item_meal = models.ManyToManyField(ItemMeal)
	meal = models.ForeignKey(Meal, verbose_name='Refeição', related_name='plates')

	def __str__(self):
		return self.meal.name
		
	def get_absolute_url(self):
		return reverse('meal:plate_list')

	class Meta:
		verbose_name = 'Prato Feito'
		verbose_name_plural = 'Pratos Feitos'
		ordering = ['-id']
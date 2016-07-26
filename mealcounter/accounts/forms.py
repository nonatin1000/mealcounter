# -*- coding: utf-8 -*-

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import authenticate, get_user_model
from django import forms

User = get_user_model()

class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        
        # Valido o email para ser obrigatório
        if email == '':
        	raise forms.ValidationError('O endereço de email é obrigatório.')
        return email 

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('Este endereço de email já está em uso. Por favor, use um email difrerente.')
        return email

class PasswordResetForm(PasswordResetForm):
	def clean_email(self):
		amount = get_user_model()._default_manager.filter(
            email__iexact=self.cleaned_data.get('email'), is_active=True).count()
		if(amount < 1):
			raise forms.ValidationError('Lamentamos, mas não reconhecemos esse endereço de e-mail.')
		return self.cleaned_data.get('email')
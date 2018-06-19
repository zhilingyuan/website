from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
class LoginForm(forms.Form):
	username=forms.CharField(
		label='用户名',widget=forms.TextInput(
			attrs={'class':'form-control','placeholder':'y'}))
	password=forms.CharField(
		label='密码',widget=forms.PasswordInput(
			attrs={'class':'form-control','placeholder':'y'}))

	def clean(self):
		username=self.cleaned_data['username']
		password=self.cleaned_data['password']
		user=auth.authenticate(username=username,password=password)
		if user is None:
			raise forms.ValidationError('用户名密码错误')
		else:
			self.cleaned_data['user']=user 
		return self.cleaned_data

class RegForm(forms.Form):
	"""docstring for RegForm"""
	username=forms.CharField(
		label='用户名',max_length=30,min_length=3,widget=forms.TextInput(
			attrs={'class':'form-control','placeholder':'y'}))
	password=forms.CharField(
		label='密码',max_length=20,min_length=6,widget=forms.PasswordInput(
			attrs={'class':'form-control','placeholder':'y'}))
	email=forms.EmailField(
		label='邮箱',widget=forms.TextInput(
			attrs={'class':'form-control','placeholder':'y'}))
	password_again=forms.CharField(
		label='密码',max_length=20,min_length=6,widget=forms.PasswordInput(
			attrs={'class':'form-control','placeholder':'y'}))

	def clean_username(self):
		username=self.cleaned_data['username']
		if User.objects.filter(username=username).exist():
			raise forms.ValidationError('用户名存在')
		return username

	def clean_email():
		email=self.cleaned_data['email']
		if User.objects.filter(email=email).exist():
			raise forms.ValidationError('email存在')
		return email

	def clean_password():
		password=self.cleaned_data['password']
		password_again=self.cleaned_data['password_again']
		if password_again!=password:
			raise forms.ValidationError('密码不一致')
		return password
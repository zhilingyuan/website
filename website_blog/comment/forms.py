from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget
class CommentForm(forms.Form):
	"""docstring for CommentForm"""
	content_type=forms.CharField(widget=forms.HiddenInput)
	object_id=forms.IntegerField(widget=forms.HiddenInput)
	#text=forms.CharField(widget=forms.Textarea)
	text=forms.CharField(widget=CKEditorWidget(config_name='comment_ckeditor'),
		error_messages={'required':'评论不能为空'})
	def __init__(self,*args,**kwargs):
		if 'user' in kwargs:
			self.user=kwargs.pop('user')
		super(CommentForm,self).__init__(*args,**kwargs)

	def clean(self):
		if self.user.is_authenticated:
			self.cleaned_data['user']=self.user
		else:
			raise forms.ValidationError('未登录')
		content_type=self.cleaned_data['content_type']
		object_id=self.cleaned_data['object_id']
		try:
			model_class=ContentType.objects.get(model=content_type).model_class()
			model_obj=model_class.objects.get(pk=object_id)
			self.cleaned_data['content_object']=model_obj
		except ObjectDoesNotExist:
			raise forms.ValidationError('comment not exists')
		return self.cleaned_data



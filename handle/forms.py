from django import forms
from handle.models import usr

# Create your forms here.
class UserForm(forms.ModelForm):
	#uid=forms.CharField(label="Message: ",widget=forms.Textarea)
	usr_name_id = forms.CharField()
	class Meta:
		model = usr
		fields = "__all__"
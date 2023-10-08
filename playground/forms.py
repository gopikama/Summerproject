
from django import forms 
  
class FormForFileUpload(forms.Form): 
    name = forms.CharField() 
    file_field = forms.FileField()
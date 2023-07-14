from django import forms



class PersonForm(forms.Form):
    url = forms.CharField(label="GitHub person name:", max_length=100)





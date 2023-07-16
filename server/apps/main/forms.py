from django import forms



class PersonForm(forms.Form):
    name = forms.CharField(label="GitHub person name:", max_length=100)





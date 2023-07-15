from django import forms



class PersonForm(forms.Form):
    url = forms.CharField(label="GitHub person URL:", max_length=100)





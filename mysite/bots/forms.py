from django import forms


class Sessioncountform(forms.Form):
    YEARS = [x for x in range(1940, 2020)]
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

from django import forms
from.models import Report


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        widgets = {'date': DateInput(), 'time': TimeInput()}
        fields = ['profile', 'date', 'time', 'incident_type', 'incident_location', 'incident_description']




# NUMS= [
#     ('one', 'one'),
#     ('two', 'two'),
#     ('three', 'three'),
#     ('four', 'four'),
#     ('five', 'fives'),
#
# ]
#
#
# class CHOICES(forms.Form):
#     NUMS = forms.CharField(widget=forms.RadioSelect(choices=NUMS))
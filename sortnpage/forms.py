import datetime
from django import forms
from tempus_dominus.widgets import DatePicker

from .models import Incident


class CustomDateField(forms.DateField):
    def to_python(self, value):
        print(value)
        formatted_value = datetime.datetime.strptime(value, "%d-%m-%Y").strftime(
            "%Y-%m-%d"
        )
        return super().to_python(formatted_value)


class IncidentForm(forms.ModelForm):
    date = CustomDateField(widget=DatePicker(options={"format": "DD-MM-YYYY"}))

    class Meta:
        model = Incident
        fields = "__all__"

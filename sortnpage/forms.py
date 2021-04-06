import datetime
from django import forms
from django.db.models import fields
from tempus_dominus.widgets import DatePicker

from .models import Incident, DateRangeAndDuration


# class CustomDateField(forms.DateField):
#     def to_python(self, value):
#         print(value)
#         formatted_value = datetime.datetime.strptime(value, "%d-%m-%Y").strftime(
#             "%Y-%m-%d"
#         )
#         return super().to_python(formatted_value)


class IncidentForm(forms.ModelForm):
    # date = CustomDateField(widget=DatePicker(options={"format": "DD-MM-YYYY"}))

    class Meta:
        model = Incident
        fields = "__all__"
        widgets = {"date": DatePicker(options={"format": "DD-MM-YYYY"})}


class DateRangeAndDurationForm(forms.ModelForm):
    class Meta:
        model = DateRangeAndDuration
        fields = "__all__"
        widgets = {
            "start_date": DatePicker(options={"format": "DD-MM-YYYY"}),
            "end_date": DatePicker(options={"format": "DD-MM-YYYY"}),
        }

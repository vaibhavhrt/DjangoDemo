from django.forms import ModelForm, DateInput
from datetimewidget.widgets import DateTimeWidget, DateWidget

from .models import ChildA


class ChildACreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].required = False
        self.fields['parent'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = ChildA
        fields = '__all__'
        widgets = {
            # 'dt': DateInput(attrs={'type': 'date'})
            'dt': DateWidget(attrs={'id': "id_dt"}, usel10n=True, bootstrap_version=3)
        }

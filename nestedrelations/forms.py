from django.forms import ModelForm

from .models import ChildA


class ChildACreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].required = False
        self.fields['parent'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = ChildA
        fields = '__all__'

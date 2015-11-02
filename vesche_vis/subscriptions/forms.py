from django import forms
from crispy_forms.helper import FormHelper
from .models import Cooperant

class CooperantForm(forms.ModelForm):
#    helper = FormHelper()
#    helper.form_tag = False

    class Meta:
        model = Cooperant
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'street_and_number',
            'zip_code',
            'city',
        ]

#    @property
#    def helper(self):
#        self._helper.form_method = 'post'
#        self._helper = FormHelper();
#        self._helper.form_class = 'form-horizontal col-xs-12 col-md-6 col-lg-5'
#        self._helper.label_class = 'col-xs-3 col-md-2 col-lg-2'
#        self._helper.field_class = 'col-xs-9 col-md-10 col-lg-10'
#        return self._helper

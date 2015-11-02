from django import forms
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit, Button
from crispy_forms.bootstrap import TabHolder, Tab

from .models import Cooperant


# =============================================================================
# MIXINS
# =============================================================================
class NoFormTagCrispyFormMixin(object):
    @property
    def helper(self):
        if not hasattr(self, '_helper'):
            self._helper = FormHelper()
            self._helper.form_tag = False
        return self._helper

# =============================================================================
# COOPERANT FORM
# =============================================================================
class CooperantForm(forms.ModelForm):

    helper = FormHelper()

    helper.form_method = 'post'
    helper.form_class = 'form-horizontal col-xs-12 col-md-6 col-lg-5'
    helper.label_class = 'col-xs-3 col-md-4 col-lg-4'
    helper.field_class = 'col-xs-9 col-md-8 col-lg-8'
    #helper.add_input(Submit('submit', 'Save'))

#    helper.add_input(Button(
#        'cancel', 'Cancel', onclick='location.href="%s";' % \
#                                    reverse('dashboard')))

    # Remove the blank option from the select widget.
    #fields['category'].empty_label = None
    #fields['category'].required = False

    # Specify which time formats are valid for this field. This setting is
    # necessary when using the bootstrap-datetimepicker widget as it
    # doesn't allow inputting of seconds.
    #valid_time_formats = ['%H:%M', '%I:%M%p', '%I:%M %p']
    #fields['record_time'].input_formats = valid_time_formats

#    helper.layout = Layout(
#        Field('first_name', autofocus=True),
#        'last_name',
#        'phone',
#        'email',
#        'street_and_number',
#        'zip_code',
#        'city'
#    )
    helper.layout = Layout(
        'first_name',
        'last_name',
        'phone',
        'email',
    )

#        HTML(
#            '''
#            {% if messages %}
#            {% for message in messages %}
#            <p {% if message.tags %}
#            class="alert alert-{{ message.tags }}"
#            {% endif %}>{{ message }}</p>{% endfor %}{% endif %}
#            '''
#        ),
#        Field('value', placeholder='Value', required=True, autofocus=True,
#              min=0, step='any'),
#        'category',
#        'record_date',
#        'record_time',
#        'notes',
#        Field('tags', placeholder='e.g. fasting, sick, "after meal"'),
#        Field('submit_button_type', type='hidden')
#    )

    class Meta:
        model = Cooperant
        exclude = ('code',)

#    @property
#    def helper(self):
#        self._helper.form_method = 'post'
#        self._helper = FormHelper();
#        self._helper.form_class = 'form-horizontal col-xs-12 col-md-6 col-lg-5'
#        self._helper.label_class = 'col-xs-3 col-md-2 col-lg-2'
#        self._helper.field_class = 'col-xs-9 col-md-10 col-lg-10'
#        return self._helper

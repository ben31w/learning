"""
List of forms for the learning_logs app.

ModelForm enables users to create a record of a model using a form.
It includes a nested Meta class that specifies the model to create and the
fields on the form.
"""
from django import forms

from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    """Form where users can submit a new topic."""
    class Meta:
        model = Topic
        # This form will have only one field. Text is a CharField (specified in
        #  the Topic model). This will be converted to a textfield on the form
        fields = ['text']
        # Don't generate a label for this field; we'll just create our own label
        #  in the form
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """Form where users can submit an entry for a topic"""
    class Meta:
        model = Entry
        fields = ['text']
        # Don't generate a label for this field; we'll just create our own label
        #  in the form
        labels = {'text': ''}
        # normally, the field 'text' would be assigned a default textfield as
        #  the input widget, but we can use to customize this to a textarea
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


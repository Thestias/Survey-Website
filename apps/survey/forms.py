from django import forms
from .models import Survey, Question, Option, Submission, Answer


class SurveyForm(forms.ModelForm):
    '''
    This form applies TailwindCSS styles to the input fields.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['title'].widget.attrs.update({'class': 'custom_input_one'})
        self.fields['description'].widget.attrs.update({'class': 'custom_input_one'})
        self.fields['is_active'].label = 'Active?'

    class Meta:
        model = Survey
        fields = ('title', 'description', 'is_active')


class BaseChildrenFormset(forms.BaseInlineFormSet):
    def __init__(self, *args, participate, **kwargs):
        super().__init__(*args, **kwargs)
        self.participate = participate

    def add_fields(self, form, index):
        super(BaseChildrenFormset, self).add_fields(form, index)

    # save the formset in the 'nested' property
        if self.participate:
            form.instance_id = form.instance.id  # Used in the templates to differentiate differents OptionForms

            # The ModelChoiceField is added here to use the form.instance.id for the queryset, it overwrites the field from OptionForm
            OptionForm.base_fields['option'] = forms.ModelChoiceField(
                queryset=Option.objects.filter(question=form.instance.id),
                widget=forms.RadioSelect, empty_label=None)

            form.nested = OptionForm(participate=True)
        else:
            form.nested = OptionFormSet(
                instance=form.instance, data=form.data if form.is_bound else None, files=form.files
                if form.is_bound else None, prefix=f'option-{form.prefix}-{OptionFormSet.get_default_prefix()}',
                form_kwargs={'participate': self.participate})

    def is_valid(self):
        result = super(BaseChildrenFormset, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested'):
                    result = result and form.nested.is_valid()

        return result

    def save(self, commit=True):

        result = super(BaseChildrenFormset, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested'):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result


class QuestionForm(forms.ModelForm):
    '''
    This form applies TailwindCSS styles to the input fields.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['question'].widget.attrs.update({'class': 'custom_input_one'})

    class Meta:
        model = Question
        fields = ['question']


class OptionForm(forms.ModelForm):
    '''
    This form applies TailwindCSS styles to the input fields.
    '''

    def __init__(self, *args, participate, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        if participate is False:
            self.fields['option'].widget.attrs.update({'class': 'custom_input_one'})

    class Meta:
        model = Option
        fields = ['option']


# For EDITING Questions/Options
QuestionFormSet = forms.inlineformset_factory(
    Survey, Question, fields=('question',),
    form=QuestionForm, formset=BaseChildrenFormset, extra=1, can_delete=True)

OptionFormSet = forms.inlineformset_factory(
    Question, Option, fields=('option',),
    form=OptionForm, extra=1, can_delete=True)

# For ANSWERING Questions/Options
QuestionAnswerFormSet = forms.inlineformset_factory(
    Survey, Question, fields=('question',),
    form=QuestionForm, formset=BaseChildrenFormset, extra=0, can_delete=False)

OptionAnswerFormSet = forms.inlineformset_factory(
    Question, Option, form=OptionForm, extra=0, can_delete=False)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('submission', 'option', 'question',)

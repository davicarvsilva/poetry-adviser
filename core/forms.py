from django import forms

from . import poetry_extractor

class MainForm(forms.Form):
    p_e = poetry_extractor.PoetryExtractor()
    p_e.url = 'https://poetrydb.org/author'

    author_name = forms.ChoiceField(label='Author', widget=forms.Select, choices = p_e.get_data_tuple())

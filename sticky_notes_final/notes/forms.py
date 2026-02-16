from django import forms
from .models import Note


# Build the forms which are auto-generated for creating and editing notes.
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

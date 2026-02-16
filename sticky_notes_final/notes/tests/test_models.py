from django.test import TestCase
from notes.models import Note


class NoteModelTest(TestCase):
    """Tests for the Note model."""

    def test_note_str_returns_title(self):
        """__str__ should return the note title."""
        note = Note.objects.create(title="Test Note", content="Sample content")
        self.assertEqual(str(note), "Test Note")

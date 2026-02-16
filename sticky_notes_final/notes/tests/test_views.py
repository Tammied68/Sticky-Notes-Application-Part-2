from django.test import TestCase
from django.urls import reverse
from notes.models import Note


class TestCreateNoteView(TestCase):
    def test_create_note(self):
        # Arrange: define the data you want to send
        data = {
            "title": "My First Note",
            "content": "This is a test note."
        }

        # Act: send POST request to the create view
        response = self.client.post(reverse("note_create"), data)

        # Assert: note was created
        self.assertEqual(Note.objects.count(), 1)

        note = Note.objects.first()
        self.assertEqual(note.title, "My First Note")
        self.assertEqual(note.content, "This is a test note.")

        # Assert: user was redirected after creation
        self.assertEqual(response.status_code, 302)


class TestViewNotes(TestCase):
    def setUp(self):
        # Create sample notes to display in the list view
        Note.objects.create(title="Note 1", content="Content 1")
        Note.objects.create(title="Note 2", content="Content 2")

    def test_view_notes_list(self):
        # Act: send GET request to the list view
        response = self.client.get(reverse("note_list"))

        # Assert: page loads successfully
        self.assertEqual(response.status_code, 200)

        # Assert: correct template is used
        self.assertTemplateUsed(response, "notes/note_list.html")

        # Assert: notes appear in the response context
        notes = response.context["notes"]
        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0].title, "Note 1")
        self.assertEqual(notes[1].title, "Note 2")


class TestUpdateNote(TestCase):
    def setUp(self):
        # Create a note to update
        self.note = Note.objects.create(
            title="Old Title",
            content="Old content"
        )

    def test_update_note(self):
        # Arrange: new data for the update
        data = {
            "title": "Updated Title",
            "content": "Updated content"
        }

        # Act: send POST request to update view
        response = self.client.post(
            reverse("note_edit", args=[self.note.pk]),
            data
        )

        # Refresh the note from the database
        self.note.refresh_from_db()

        # Assert: note was updated
        self.assertEqual(self.note.title, "Updated Title")
        self.assertEqual(self.note.content, "Updated content")

        # Assert: user was redirected
        self.assertEqual(response.status_code, 302)

import argparse
from enum import Enum

class Note:
    def __init__(self, title, text, creation_date, important):
        self.title = title
        self.text = text
        self.creation_date = creation_date
        self.important = important

class Notebook:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Notebook, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def remove_note(self, note):
        self.notes.remove(note)

    def edit_note(self, note, new_title, new_text, new_important):
        note.title = new_title
        note.text = new_text
        note.important = new_important

    def view_notes(self):
        for note in self.notes:
            print(f"Title: {note.title}")
            print(f"Text: {note.text}")
            print(f"Creation Date: {note.creation_date}")
            print(f"Important: {note.important}")
            print()

class NoteFactory:
    @staticmethod
    def create_note(title, text, creation_date, important):
        return Note(title, text, creation_date, important)

class NoteObserver:
    def __init__(self, email):
        self.email = email

    def update(self, note):
        print(f"Note '{note.title}' has been updated. Sending email to {self.email}...")
        # Отправка email с уведомлением об изменении заметки

class SortStrategy(Enum):
    DATE = 1
    IMPORTANCE = 2

class NoteSorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort_notes(self, notes):
        if self.strategy == SortStrategy.DATE:
            sorted_notes = sorted(notes, key=lambda note: note.creation_date)
        elif self.strategy == SortStrategy.IMPORTANCE:
            sorted_notes = sorted(notes, key=lambda note: note.important, reverse=True)
        else:
            sorted_notes = notes

        return sorted_notes

class NoteFilter:
    def __init__(self, next_filter=None):
        self.next_filter = next_filter

    def apply(self, notes):
        filtered_notes = self.filter_notes(notes)

        if self.next_filter:
            return self.next_filter.apply(filtered_notes)
        else:
            return filtered_notes

    def filter_notes(self, notes):
        raise NotImplementedError

class ImportantNoteFilter(NoteFilter):
    def filter_notes(self, notes):
        return [note for note in notes if note.important]

class DateNoteFilter(NoteFilter):
    def __init__(self, start_date, end_date, next_filter=None):
        super().__init__(next_filter)
        self.start_date = start_date
        self.end_date = end_date

    def filter_notes(self, notes):
        return [note for note in notes if self.start_date <= note.creation_date <= self.end_date]

class NoteReportCommand:
    def __init__(self, filters):
        self.filters = filters

    def execute(self, notes):
        filtered_notes = self.filters.apply(notes)

        report = ""
        for note in filtered_notes:
            report += f"Title: {note.title}\n"
            report += f"Text: {note.text}\n"
            report += f"Creation Date: {note.creation_date}\n"
            report += f"Important: {note.important}\n\n"

        return report

def add_note_command(args):
    note = NoteFactory.create_note(args.title, args.text, args.creation_date, args.important)
    notebook.add_note(note)

def remove_note_command(args):
    note = find_note_by_title(args.title)
    if note:
        notebook.remove_note(note)
    else:
        print(f"Note with title '{args.title}' not found.")

def edit_note_command(args):
    note = find_note_by_title(args.title)
    if note:
        notebook.edit_note(note, args.new_title, args.new_text, args.new_important)
    else:
        print(f"Note with title '{args.title}' not found.")

def view_notes_command(args):
    notebook.view_notes()

def find_note_by_title(title):
    for note in notebook.notes:
        if note.title == title:
            return note
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Note Management Application")
    subparsers = parser.add_subparsers()

    add_note_parser = subparsers.add_parser("add_note", help="Add a new note")
    add_note_parser.add_argument("title", type=str, help="Note title")
    add_note_parser.add_argument("text", type=str, help="Note text")
    add_note_parser.add_argument("creation_date", type=str, help="Note creation date")
    add_note_parser.add_argument("--important", action="store_true", help="Mark note as important")
    add_note_parser.set_defaults(func=add_note_command)

    remove_note_parser = subparsers.add_parser("remove_note", help="Remove a note")
    remove_note_parser.add_argument("title", type=str, help="Note title")
    remove_note_parser.set_defaults(func=remove_note_command)

    edit_note_parser = subparsers.add_parser("edit_note", help="Edit a note")
    edit_note_parser.add_argument("title", type=str, help="Note title")
    edit_note_parser.add_argument("new_title", type=str, help="New note title")
    edit_note_parser.add_argument("new_text", type=str, help="New note text")
    edit_note_parser.add_argument("new_important", type=bool, help="New note importance")
    edit_note_parser.set_defaults(func=edit_note_command)

    view_notes_parser = subparsers.add_parser("view_notes", help="View all notes")
    view_notes_parser.set_defaults(func=view_notes_command)

    args = parser.parse_args()

    notebook = Notebook()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

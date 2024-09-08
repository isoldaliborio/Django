from django.shortcuts import render
from .models import Notes


def list(request):
    # Stores all the notes that we have
    all_notes = Notes.objects.all()
    return render(request, "notes/notes_list.html", {"notes": all_notes})

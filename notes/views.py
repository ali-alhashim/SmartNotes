from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView, UpdateView
# Create your views here.

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/notes/list'
    template_name = 'notes/notes_form.html'
    fields = ('title', 'text')

class NotesList(ListView):
    model = Notes 
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/note_detail.html'

class NotesUpdateView(UpdateView):
    model = Notes
    fields = ('title', 'text')
    success_url = '/notes/list'



    

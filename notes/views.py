from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/notes/list'
    template_name = 'notes/notes_form.html'
    form_class = forms.NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesList(LoginRequiredMixin,ListView):
    model = Notes 
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = 'home.login'

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/note_detail.html'

class NotesUpdateView(UpdateView):
    model = Notes
    form_class = forms.NotesForm
    success_url = '/notes/list'

class NotesDeleteView(DeleteView):
    model = Notes 
    success_url = '/notes/list'



    

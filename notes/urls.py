from django.urls import path
from . import views
urlpatterns = [

    path('notes/list',views.NotesList.as_view(), name='notes.list' ),

    path('notes/detail/<int:pk>', views.NotesDetailView.as_view(), name = 'note.detail'),

    path('notes/create', views.NotesCreateView.as_view(), name='note.create'),

    path('notes/update/<int:pk>',views.NotesUpdateView.as_view(), name="note.update"),

    path('notes/delete/<int:pk>',views.NotesDeleteView.as_view(), name="note.delete")
]
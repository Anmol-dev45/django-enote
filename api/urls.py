from django.urls import path
from .views import GradeListAPIView, SubjectListAPIView, ChapterListAPIView, NoteListAPIView

urlpatterns = [
    path('grades/', GradeListAPIView.as_view(), name='grade-list'),
    path('grades/<int:grade_id>/subjects/', SubjectListAPIView.as_view(), name='subject-list'),
    path('subjects/<int:subject_id>/chapters/', ChapterListAPIView.as_view(), name='chapter-list'),
    path('chapters/<int:chapter_id>/notes/', NoteListAPIView.as_view(), name='note-list'),
]

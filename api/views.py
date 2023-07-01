from rest_framework import generics
from .models import Grade, Subject, Chapter, Note
from .serializers import GradeSerializer, SubjectSerializer, ChapterSerializer, NoteSerializer

class GradeListAPIView(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class SubjectListAPIView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        grade_id = self.kwargs['grade_id']
        return Subject.objects.filter(grade__id=grade_id)

class ChapterListAPIView(generics.ListAPIView):
    serializer_class = ChapterSerializer

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Chapter.objects.filter(subject__id=subject_id)

class NoteListAPIView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        chapter_id = self.kwargs['chapter_id']
        return Note.objects.filter(chapter__id=chapter_id)

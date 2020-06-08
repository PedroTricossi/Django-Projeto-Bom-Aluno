from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Student


class StudentListView(ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'students/student_list.html'

class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'students/student_detail.html'

class SearchResultsListView(ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'students/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Student.objects.filter(
            Q(name__icontains=query) | Q(course__icontains=query)
        )
    

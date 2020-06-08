from django.urls import path
from .views import StudentListView, StudentDetailView, SearchResultsListView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('<uuid:pk>', StudentDetailView.as_view(), name='student_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results')
]
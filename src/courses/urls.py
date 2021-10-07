from django.urls import path
from .views import (
        CourseView,
        CourseListView,
        # my_fbv
        )

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]

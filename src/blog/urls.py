from django.urls import path
from .views import (
        ArticleListView
        )

app_name = 'article'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    #path('create/', product_create_view, name='article-list'),
    #path('<int:id>/', product_detail_view, name='article-detail'),
    #path('<int:id>/update/', product_update_view, name='article-update'),
    #path('<int:id>/delete/', product_delete_view, name='article-delete'),
]

from django.urls import path
from .views import (
        ArticleListView
        )

app_name = 'article'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    #path('create/', view_name, name='article-create'),
    #path('<int:id>/', view_name, name='article-detail'),
    #path('<int:id>/update/', view_name, name='article-update'),
    #path('<int:id>/delete/', view_name, name='article-delete'),
]
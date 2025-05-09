from django.urls import path
from .views import BlogCreateView, BlogUpdateView, BlogDeleteView, BlogListView, BlogDetailView

urlpatterns = [
        path('', BlogListView.as_view(), name='blog-list'),

    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('<int:pk>', BlogDetailView.as_view(), name="detail_view")
]

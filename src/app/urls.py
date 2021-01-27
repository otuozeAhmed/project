from django.urls import path

from .views import HomePageView, CardDetailView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/', CardDetailView.as_view(), name='card_detail'),
    path('', HomePageView.as_view(), name='home'),
    
]

from django.urls import path
from .views import NewsListView, RegisterNews, NewsDetailView, login_view, logout_view

urlpatterns = [
    path('news-list/', NewsListView.as_view(), name='news-list'),
    path('new_news/', RegisterNews.as_view(), name='register-news'),
    path('news-list/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout')
]

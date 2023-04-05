from django.urls import path
from .views import HomeView, PostView, PostCreateView, PostUpdateView, PostDeleteView
from users import views

# A list of strings representing the full Python import paths to call to get the URLconfs for each installed application.
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<pk>/<slug:slug>', PostView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('search/', views.search, name='search')

]

from django import views
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage, TaskReorder
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('home/', views.home, name='home'),
    path('review/', views.review, name='review'),
    path('contact/', views.contact, name='contact'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('addReview', views.addReview, name='addReview'),
    path('addContact', views.addContact, name='addContact'),
    

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]

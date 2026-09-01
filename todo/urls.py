from django.urls import path
from .import views
urlpatterns = [
    path('', views.HomeView.as_view()),
    path('add/', views.AddView.as_view(), name='add'),
    path('about/<str:name>/', views.AboutView.as_view),
    path('todo/<int:pk>/', views.DetailView.as_view(), name='todo'),
    path('update/<int:pk>/', views.UpdateTodoView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteTodoView.as_view(), name='delete'),
    path(
        'toggle/<int:id>/',
        views.ToggleTodoView.as_view(),
        name='toggle_todo'
    ),
]

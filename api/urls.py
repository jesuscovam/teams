from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path(r'^team/(?P<name>\w+)$', views.TeamDetailView.as_view(), name='team-detail')
]
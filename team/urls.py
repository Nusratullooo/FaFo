from django.urls import path
from team import views


urlpatterns = [
    path('team/', views.team, name='team'),
    path('team_detail/<int:id>', views.team_detail, name='team_detail')

]
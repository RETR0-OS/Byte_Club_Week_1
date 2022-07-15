from django.urls import path, include
from . import views

app_name = 'competitions'

urlpatterns = [
    path('', views.ListCompetitionsView, name='compete'),
    path('', include('django.contrib.auth.urls')),
    path('competition/<slug>/view', views.CompetitionDetails, name='competition_details'),
    path('competition/<slug>/register', views.RegisterUserForCompetition, name='competition_register'),
    path('competition/add', views.AddCompetitionView.as_view(), name='competition_add'),
    path('competition/<slug>/edit', views.EditCompetitionDetails.as_view(), name='competition_edit')
]

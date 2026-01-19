# add url patterns
from django.urls import path
from .views import AssignPlayerSchedule, AssignUserPlayer, CreatePlaySchedule, CreatePlayerView, DetailPlaySchedule, DetailPlayerView, DetailUserView, HomeView, ListPlaySchedule, ListPlayerView, LogoutView, RegisterView, LoginView, UserListView

app_name = 'account'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # players
    path('players/', ListPlayerView.as_view(), name='players'),
    path('players/create', CreatePlayerView.as_view(), name='players-create'),
    path('players/<pk>', DetailPlayerView.as_view(), name='player-details'),
    path('players/schedule/',AssignPlayerSchedule.as_view(), name='player-schedule-register'),
    
    # scheduling
    path('play-schedule', ListPlaySchedule.as_view(), name='scheduling'),
    path('play-schedule/create', CreatePlaySchedule.as_view(), name='scheduling-create'),
    path('play-schedule/<pk>', DetailPlaySchedule.as_view(), name='scheduling-details'),
    
    # parents
    path('care-takers', UserListView.as_view(), name='care-takers'),
    path('care-takers/<pk>', DetailUserView.as_view(), name='care-takers-details'),
    path('care-takers/assign/', AssignUserPlayer.as_view(), name='care-takers-assign-player')
]

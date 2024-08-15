from django.urls import path
from . import views

app_name= 'groups'

urlpatterns= [
    path('',views.ListGroups.as_view(),name="all"),
    path('new/',views.CreateGroup.as_view(), name='create'),
    path('<slug:slug>/',views.SingleGroup.as_view(),name='single'),           #posts/in/(?P<slug>[-\w]+)/$
    path('join/<slug:slug>/', views.JoinGroup.as_view(), name="join"),
    path('leave/<slug:slug>/', views.LeaveGroup.as_view(), name="leave"),

]
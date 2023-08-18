from.import views
from django.urls import path

urlpatterns = [
    path('',views.add,name='add'),
    path('done/<int:taskid>/',views.done,name='done'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk/',views.TaskDetailView.as_view(),name='cbvdetail'),
]
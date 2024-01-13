from django.urls import path
from webapp.views import ProductListView

app_name = "webapp"

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    # path('projects/<int:pk>', ProjectDetailView.as_view(), name="project_detail_view"),
    # path('project/add/', ProjectCreateView.as_view(), name="project_create"),
    # path('project/<int:pk>/update', ProjectUpdateView.as_view(), name="project_update_view"),
    # path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name="project_delete_view"),
    # path('project/<int:pk>/tasks/add/', TaskCreateView.as_view(), name="task_create"),
    #
    # path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    # path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    # path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    # path('projects/<int:pk>/change-users/', ChangeUsersInProjectView.as_view(), name="project_users_change"),
]
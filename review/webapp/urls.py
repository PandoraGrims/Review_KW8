from django.urls import path
from webapp.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = "webapp"

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('product/<int:pk>', ProductDetailView.as_view(), name="product_detail_view"),
    path('product/add/', ProductCreateView.as_view(), name="product_create"),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name="product_update_view"),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete_view"),

    # path('project/<int:pk>/tasks/add/', TaskCreateView.as_view(), name="task_create"),
    #
    # path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    # path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    # path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    # path('projects/<int:pk>/change-users/', ChangeUsersInProjectView.as_view(), name="project_users_change"),
]
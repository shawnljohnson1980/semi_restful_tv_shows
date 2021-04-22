from . import views
from django.urls import path


urlpatterns=[
    path('', views.index),
    path('shows/new',views.show_create),
    path('shows/create_show',views.create_show),
    path('shows/<int:show_id>/edit',views.edit),
    path('shows/<int:show_id>/edit_show',views.edit_show),
    path('shows/<int:show_id>',views.view_show),
    path('show/<int:show_id>/delete',views.delete),
]
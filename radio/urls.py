from django.urls import path
from . import views


app_name = 'radio'

urlpatterns = [
    # Display
    path('', views.IndexView.as_view(), name='index'),
    path('show/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('category/<str:category_name>/', views.category_view, name='category'),  

    # Create
    path('show-add/', views.ShowCreate.as_view(), name='show-add'),
    path('category-add/', views.CategoryCreate.as_view(), name='category-add'),
    path('show/<int:pk>/audio-add/', views.AudioCreate.as_view(), name='audio-add'),

    # Update
    path('show/<int:pk>/show-update/', views.ShowUpdate.as_view(), name='show-update'),

    # Delete
    path('show/<int:pk>/show-delete/', views.ShowDelete.as_view(), name='show-delete'),
    path('show/<int:show_id>/audio-delete/<int:audio_id>/', views.audio_delete, name='audio-delete'),

    # Favorite
    path('show/<int:show_id>/show-favorite/', views.show_favorite, name='show-favorite'),
    path('audio/<int:audio_id>/audio-favorite/', views.audio_favorite, name='audio-favorite'),

    # Search
    path('search/', views.search_view, name='search'),
]


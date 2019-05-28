from django.urls import path
from . import views

app_name = 'listings'
urlpatterns = [
    # /listings/
    path('', views.index, name='listings'),

    # /listings/{number} - get listing
    path('<int:listing_id>/', views.listing, name='listing'),

    # /search - search
    path('search', views.search, name='search'),


]

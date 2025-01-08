from django.urls import path
from website.views import home_view, about_view,contacet_view

urlpatterns = [
    path('', home_view),
    path('about', about_view),
    path('contact', contacet_view)
]
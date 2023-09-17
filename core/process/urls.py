"""
URL configuration for milk_processing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
from django.views.generic import RedirectView
urlpatterns = [
    path('',RedirectView.as_view(url='process/main')),
    path('process/main/',MainView.as_view(),name='main'),
    path('process/measuring/add/',MeasuringCreateView.as_view(),name='meas_add'),
    path('process/measuring/list/',MeasuringListView.as_view(),name='meas_list'),
    path('process/measuring/update/<int:pk>/',MeasuringUpdateView.as_view(),name='meas_update'),
    path('process/measuring/delete/<int:pk>/',MeasuringDeleteView.as_view(),name='delete_meas'),
    path('process/measuring/<int:pk>/',MeasuringDataView.as_view(),name='meas_data'),
    path('process/charts/',ChartsView.as_view(),name='cha'),
    path('process/train/',TrainView.as_view(),name='tra'),
]

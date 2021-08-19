from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:reeks_id>/', views.detail, name='detail'),
    path('<int:reeks_id>/training/<int:opgave_id>', views.training, name='training'),
    path('<int:reeks_id>/resultaten', views.resultaten, name='resultaten'),
    path('<int:reeks_id>/uitgewerkt/<int:opgave_id>', views.uitgewerkt, name='uitgewerkt')
    ]

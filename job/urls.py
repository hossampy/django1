
from django.urls import include, path
from .import views


urlpatterns = [
    path('', views.jobs_list),
    path('<int:id>', views.job_detail),
]

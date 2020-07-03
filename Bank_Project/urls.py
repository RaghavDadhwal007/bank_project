from django.contrib import admin
from django.urls import path
from Test import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('branches/', views.BranchesList.as_view()),

]
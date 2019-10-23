from django.urls import path

from AppSaudeMap.views import Index

urlpatterns = [
    path('',Index.as_view(), name="index"),
]

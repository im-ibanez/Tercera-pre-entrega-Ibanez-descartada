from django.urls import path
from .views import crear_expediente, index

app_name = "expediente"

urlpatterns = [
    path("", index, name="index"),
    path("crear", crear_expediente, name="crear"),
]
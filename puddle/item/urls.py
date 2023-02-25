from django.urls import path
from .views import detail, addNewItem, delete, editItem, items

app_name = "item"

urlpatterns = [
    path("", items, name="items"),
    path("<int:item_id>/", detail, name="detail"),
    path("<int:item_id>/delete", delete, name="delete"),
    path("int:item_id/edit", editItem, name="edit"),
    path("new/", addNewItem, name="new_item")
]

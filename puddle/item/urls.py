from django.urls import path
from .views import detail, addNewItem

app_name = "item"

urlpatterns=[
    path("<int:item_id>/", detail, name="detail" ),
    path("new/",addNewItem, name="new_item" )
]
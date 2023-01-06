from django.contrib import admin
from django.urls import path

import first.views as first_view

urlpatterns = [
    path("admin/", admin.site.urls),

    path("first/", first_view.FirstView.as_view())
]

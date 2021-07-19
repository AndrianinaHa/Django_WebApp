# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from core.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),

    path('upload', views.upload, name='upload-employe'),
    path('update/<int:employe_id>', views.update_employe, name='update'),
    path('delete/<int:employe_id>', views.delete_employe, name='delete'),

    # Pages employes
    path('liste', views.liste, name='liste'),
    path('todoap', views.todoap, name="todoap"),
]

# DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
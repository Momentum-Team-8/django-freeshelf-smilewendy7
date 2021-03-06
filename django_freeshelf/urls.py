"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from books import views as books_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    ### add registration path : what to do with this?
    path('', books_views.homepage, name='home'),
    path('accounts/', include('registration.backends.simple.urls')),
    # path('accounts/', include('registration.backends.default.urls')),
    path('books/', books_views.list_books, name='list_books'),
    ## show details
    path("details/<int:pk>", books_views.show_details, name="show_details"),
    path("categ/<slug:slug>",books_views.show_categ, name="show_categ"),
    path("favorite/<int:pk>",books_views.favorite_books, name = "favorite_book"),
    ### search books
    path('search_books', books_views.search_books, name='search_books'),

    path("admin/", admin.site.urls),
] + static(settings.STATIC_URL, docuement_root=settings.STATIC_ROOT )

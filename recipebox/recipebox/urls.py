"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from recipebox.views import mainpage, recipe, author, addrecipe, addauthor, signup, login_view
from recipebox.models import Author
from recipebox.models import Recipe


admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage, name='mainpage'),
    path('recipe/<int:r_id>', recipe),
    path('author/<int:a_id>', author),
    path('addrecipe/', addrecipe),
    path('addauthor/', addauthor),
    path('signup/', signup),
    path('login/', login_view)
]

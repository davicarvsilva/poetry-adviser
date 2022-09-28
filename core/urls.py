from django.urls import path, include

from . import views as core_views

app_name = 'core'

urlpatterns = [
    path('', core_views.home, name='home'),
    path('get-poem/', core_views.get_poem, name='get_poem')
]

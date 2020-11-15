from django.urls import path
from day_day import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.logIn_view, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logOut_view, name='logout'),
    path('TAA/<str:type_TAA>/<int:TAA_id>', views.TAA_API, name='TAA_API'),
    path('active/<str:type_TAA>/<int:TAA_id>', views.activeUnactive, name='activeAPI'),
    path('edit/<str:type_TAA>/<int:TAA_id>', views.editTAA, name='editAPI'),
    path('delete/<str:type_TAA>/<int:TAA_id>', views.deleteTAA, name='deleteAPI')
]

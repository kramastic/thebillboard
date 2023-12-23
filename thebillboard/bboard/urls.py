from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('action/<slug:action>/', by_action, name='by_action'),
    path('type/<slug:item_type>/', ByTypeView.as_view(), name='by_type'),
    path('type/<slug:item_type>/<slug:action>/', by_cat_act, name='by_cat_act'),
    path('type/<slug:item_type>/<int:adv_id>/', show_adv, name='show_adv'),

    path('add_bb/', AddBbCreateView.as_view(), name='add_bb'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('account/', personal_account, name='personal_account'),
    # path('account/my_adv', name='my_adv'),
    # path('add_bb/', cat_act_create_bb, name='add_bb'),
]
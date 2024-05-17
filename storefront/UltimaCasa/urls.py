from django.urls import path
from . import views

#urlconfig
urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('login/registreer', views.registreer, name='registreer'),
    path('', views.home,  name="home"),
    path('login/logout', views.logout_user, name="logout"),
    path('koper/', views.koper, name="koper"),
    path('koper/verwijder/<int:huis_id>', views.koperverwijderhuis, name="koperverwijderhuis"),
    path('koper/verkoop', views.verkoop, name="verkoop" ),
    path('koper/verkoop/form', views.verkoopform, name="verkoopform" ),
    path('koper/<int:bieding_id>', views.koperview, name="update_koper"),
    path('koper/account', views.account, name="account"),
    path('beheer/', views.beheer, name="beheer"),
    path('beheer/<int:adres_id>', views.beheeradres, name="beheeradres"),
    path('beheer/<int:bieding_id>', views.beheerview, name="update_beheer"),
    path('beheer/relaties/<int:relatie_id>', views.beheerrelaties, name="update_relaties"),
    path('beheer/relaties', views.relatieview, name="relaties"),
    path('beheer/adres', views.adresview, name="adres"),
    path('admin/', views.admin, name="admin"),
    path('admin/<int:status_id>', views.adminstatuswijzigen, name="adminstatuswijzigen"),  
    path('admin/rollen', views.adminrollen, name="adminrollen"),
    path('admin/accounts', views.adminaccounts, name='adminaccounts'),
    path('admin/voegen/', views.admin_status_voegen, name='adminstatus'),
    path('admin/rolvoegen/', views.adminrolvoegen, name='adminrolvoegen'),
    path('admin/rollen/<int:rol_id>', views.adminrolwijzigen, name='adminrolwijzigen'),
    path('admin/rollen/verwijderen/<int:rol_id>', views.adminrolverwijderen, name='adminrolverwijderen'),
    path('admin/accounts/<int:gebruiker_id>', views.adminaccountwijzigen, name='adminaccountwijzigen'),

]   
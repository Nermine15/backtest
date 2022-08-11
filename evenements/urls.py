from .import views
from django.urls import path,include
urlpatterns = [

   path('listevents/',views.evenementsList ),
   path('Detailevents/<str:id>/',views.DetailEvenement ),
   path('ajouterevents',views.AjouterEvenements),
   path('Updateevents/<str:pk>/',views.eventsUpdate ),
   path('deleteevents/<str:pk>/',views.DeleteEvents ),
  
   
]
 

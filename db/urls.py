from django.urls import path
from django.contrib.auth import urls as auth_urls

from . import views

urlpatterns = [
    path('', views.index, name='db-index'),
    path('newaccount/', views.newAccount, name='newAccount'),
    path('createaccount/', views.createAccount, name='db-createAccount'),
    path('allproposals/', views.allProposals, name='db-allProposals'),
    path('allvenues/', views.allVenues, name='db-allVenues'),
    path('newbatch/', views.newBatch, name='db-newBatch'),
    path('createbatch/', views.createBatch, name='db-createBatch'),
    path('batches/', views.batches, name='db-batches'),
    path('submit/', views.submit, name='db-submit'),
    path('musicForm/', views.musicForm, name='db-musicForm'),
    path('theatreForm/', views.theatreForm, name='db-theatreForm'),
    path('visualartForm/', views.visualartForm, name='db-visualartForm'),
    path('danceForm/', views.danceForm, name='db-danceForm'),
    path('literaryForm/', views.literaryForm, name='db-literaryForm'),
    path('filmForm/', views.filmForm, name='db-filmForm'),
    path('workshopForm/', views.workshopForm, name='db-workshopForm'),
    path('confirm/<int:id>/', views.confirmProposal, name='db-confirmProposal'),
    path('delete/<int:id>/', views.deleteProposal, name='db-deleteProposal'),
    path('undelete/<int:id>/', views.undeleteProposal, name='db-undeleteProposal'),
    path('venueForm/', views.venueForm, name='db-venueForm'),
    path('createVenue/', views.createVenue, name='db-createVenue'),
    path('confirmVenue/<int:id>/', views.confirmVenue, name='db-confirmVenue'),
    path('deleteVenue/<int:id>/', views.deleteVenue, name='db-deleteVenue'),
    path('undeleteVenue/<int:id>/', views.undeleteVenue, name='db-undeleteVenue'),
    path('addtobatch/<int:batchid>/<int:memberid>/', views.addToBatch, name='db-addToBatch'),
    path('addtobatch/', views.addToBatchForm, name='db-addToBatch'),
    path('removefrombatch/<int:batchid>/<int:memberid>/', views.removeFromBatch, name='db-removeFromBatch'),
    path('updateBatch/', views.updateBatch, name='db-updateBatch'),
    path('batchEmails/<int:id>/', views.batchEmails, name='db-batchEmails'),
    path('autoBatch/<int:id>/', views.autoBatch, name='db-autoBatch'),
    path('autoBatchRun/', views.autoBatchRun, name='db-autoBatchRun'),
    path('edit/<int:id>/', views.editEntity, name='db-editEntity'),
    path('update/', views.update, name='db-update'),
    path('updateVenue/', views.updateVenue, name='db-updateVenue'),
    path('addNote/', views.addNote, name='db-addNote'),
    path('reconfirm/<int:id>/', views.reconfirm, name='db-reconfirm'),
    path('<int:id>/', views.entity, name='db-entity')
]

urlpatterns += auth_urls.urlpatterns

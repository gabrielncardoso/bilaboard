from django.urls import path

from . import views

urlpatterns = [

    path("dashboard/", views.dashboard, name="dashboard"),

    #group
    path("group/create/", views.creategroup, name="creategroup"),
    path("group/store/", views.storegroup, name="storegroup"),
    path("group/<int:group_id>/", views.groupdetail, name="groupdetail"),
    path("group/<int:group_id>/edit/", views.editgroup, name="editgroup"),
    path("group/<int:group_id>/update/", views.updategroup, name="updategroup"),
    path("group/<int:group_id>/destroy/", views.destroygroup, name="destroygroup"),
    path("group/<int:group_id>/storeplayer/", views.storeplayer, name="storeplayer"),
    path("group/<int:group_id>/removeplayer/", views.removeplayer, name="removeplayer"),

    # match
    path("group/<int:group_id>/newmatch/", views.creatematch, name="newmatch"),
    path("group/<int:group_id>/storematch/", views.storematch, name="storematch"),
    path("group/<int:group_id>/match/<int:match_id>/editmatch/", views.editmatch, name="editmatch"),
    path("group/<int:group_id>/match/<int:match_id>/updatematch/", views.updatematch, name="updatematch"),
    path("group/<int:group_id>/match/<int:match_id>/destroymatch/", views.destroymatch, name="destroymatch"),

    #game
    path("game/<int:game_id>/", views.gamedetail, name="gamedetail"),

    #user
    path("userprofile/<int:user_id>/", views.userprofile, name="userprofie")
    
]

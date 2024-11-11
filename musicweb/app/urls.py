from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user),
    path('login/', views.login),
    path('get_users/', views.get_users),
    path('get_musics/', views.get_musics),
    path('get_marked_scores/', views.get_marked_scores),
    path('get_marked_clips/', views.get_marked_clips),
    path('create_marked_score/', views.create_marked_score),
    path('create_dimension_score/', views.create_dimension_score), ##
    path('create_music_emotion/', views.create_music_emotion), ##
    path('create_marked_clip/', views.create_marked_clip),
    path('get_user_scores/', views.get_user_scores),
    path('get_user_clips/', views.get_user_clips),
    path('get_user_scores_number/', views.get_user_scores_number),
    path('get_user_page_scores/', views.get_user_page_scores),
    path('get_a_song_random/', views.get_a_song_random),
    path('clip_get_a_song_random/', views.clip_get_a_song_random),
    path('find_song_of_vocal_version/', views.find_song_of_vocal_version), ##
    path('find_song_of_instrumental_version/', views.find_song_of_instrumental_version), ##
    path('update_marked_score/', views.update_marked_score),
    path('delete_marked_score/', views.delete_marked_score),
    path('update_marked_clip/', views.update_marked_clip),
    path('delete_marked_clip/', views.delete_marked_clip),
    path('get_a_song_id/', views.get_a_song_id),
    path('get_user_music_clips/', views.get_user_music_clips),
    path('get_marked_scores_by_query/', views.get_marked_scores_by_query),
    path('create_marked_dimension_score/', views.create_marked_dimension_score),
    path('get_user_music_dimension_scores/', views.get_user_music_dimension_scores),
    path('update_marked_dimension_score/', views.update_marked_dimension_score),
    path('delete_marked_dimension_score/', views.delete_marked_dimension_score),
    ## path('get_a_song_id/', views.get_a_song_id),
    path('update_music_genre/', views.update_music_genre),
    path('update_music_harmony_quantity/', views.update_music_harmony_quantity),
]
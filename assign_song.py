import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'musicweb.musicweb.settings'
import django
django.setup()
from musicweb.app.models import AssignUserMusic, User, Music

user_id_1 = '46'
song_ids_1 = [74, 75, 76]

user_id_2 = '47'
song_ids_2 = [74, 77, 78]

user_id_3 = '48'
song_ids_3 = [75, 77, 80]

user_id_4 = '49'
song_ids_4 = [76, 78, 80]

# 批量为用户分配歌曲
for song_id in song_ids_1:
    user = User.objects.get(user_id=user_id_1)
    music = Music.objects.get(music_id=song_id)
    AssignUserMusic.objects.create(user_id=user, music_id=music, is_mark=0)

for song_id in song_ids_2:
    user = User.objects.get(user_id=user_id_2)
    music = Music.objects.get(music_id=song_id)
    AssignUserMusic.objects.create(user_id=user, music_id=music, is_mark=0)

for song_id in song_ids_3:
    user = User.objects.get(user_id=user_id_3)
    music = Music.objects.get(music_id=song_id)
    AssignUserMusic.objects.create(user_id=user, music_id=music, is_mark=0)

for song_id in song_ids_4:
    user = User.objects.get(user_id=user_id_4)
    music = Music.objects.get(music_id=song_id)
    AssignUserMusic.objects.create(user_id=user, music_id=music, is_mark=0)

print('ALL RIGTH !')
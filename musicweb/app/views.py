from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils import timezone
import json
import random
from decimal import Decimal
from datetime import datetime
from .models import *

##
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q  
##


# json编码
class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, Decimal):
            # Convert Decimal to a string or a float
            return float(obj)  # or str(obj) if you prefer
        else:
            return json.JSONEncoder.default(self, obj)


# Create your views here.


########### 用户部分 ##########

# 注册
@csrf_exempt
def create_user(request):
    body = json.loads(request.body)
    if (User.objects.filter(user_name=body['user_name'])):
        return HttpResponse("用户名已存在", status=400)
    user = User(user_name=body['user_name'], user_password=body['user_password'], user_phone=body['user_phone'])
    user.save()
    # request.session['user_id'] = user.user_id
    # request.session['user_name'] = user.user_name
    return HttpResponse("注册成功")


# 登录
@csrf_exempt
def login(request):
    # if request.session.get('user_id') or request.COOKIES.get('user_id'):
    #     return HttpResponse("已登录", status=400)
    body = json.loads(request.body)
    user_name = body['user_name']
    user_password = body['user_password']
    if user_name and user_password:
        isexsit = User.objects.filter(user_name=user_name, user_password=user_password).count()
        if isexsit:
            user = User.objects.get(user_name=user_name)
            # request.session['is_login'] = True
            # request.session['user_id'] = user.user_id
            # request.session['user_name'] = user.user_name
            # return HttpResponse("登录成功")
            return JsonResponse({'loginstatus': 1, 'user_id': user.user_id, 'user_name': user.user_name},
                                safe=False)  # 登录成功返回1
        else:
            return HttpResponse("账号密码错误", status=400)
    else:
        return HttpResponse("请重新输入", status=400)


# 万能登录
def good_login(request):
    return HttpResponse({'loginstatus': 1, 'user_id': "0", 'user_name': "管理员"}, safe=False)


# 获取所有用户信息
def get_users(request):
    users = User.objects.all().values()
    users = list(users[:])
    data = json.dumps(users, cls=MyEncoder)
    return HttpResponse(data, content_type="application/json")


########### 歌曲部分 ##########

# 获取所有音乐歌曲信息
def get_musics(request):
    musics = Music.objects.all().values()
    musics = list(musics[:])
    data = json.dumps(musics)
    return HttpResponse(data, content_type="application/json")


# 根据music_id获取该首歌
@csrf_exempt
def get_a_song_id(request):
    body = json.loads(request.body)
    music_id = body['music_id']
    song = Music.objects.filter(music_id=music_id).values()
    song = list(song[:])
    data = json.dumps(song)
    return HttpResponse(data, content_type="application/json")


# 随机获取一首歌，歌的标注次数小于2，且用户没标过
@csrf_exempt
def get_a_song_random(request):
    body = json.loads(request.body)
    user_id = body['user_id']
    # 测试用户没有歌曲限制
    ## if user_id == '1' or user_id == 1 or user_id == '2' or user_id == 2:
    marked_music = MarkedScore.objects.filter(user_id=user_id).values('music_id')
    unmark_musics = list(Music.objects.exclude(music_id__in=marked_music).values())

    marked_count = marked_music.count()
    unmarked_count = len(unmark_musics)

    # # 专家
    # else:
    #     user_musics = AssignUserMusic.objects.filter(user_id=user_id)
    #     ### 每天标注歌曲数限制 ###
    #     marked_scores = MarkedScore.objects.filter(user_id=user_id)
    #     # 本次标注的歌曲数
    #     total_number = user_musics.count()
    #     # 统计当天标的歌曲数
    #     now = datetime.now()
    #     today_number = 0
    #     for marked_score in marked_scores:
    #         date = str(marked_score.mark_time)
    #         date = date.split(" ")[0].split("-")
    #         if int(date[0]) == now.year and int(date[1]) == now.month and int(date[2]) == now.day:
    #             today_number += 1
    #     # 每天标注的歌曲数为 本批次标注的歌曲数/2
    #     if total_number % 2 == 1:
    #         day_limit = (total_number + 1) / 2
    #     else:
    #         day_limit = total_number / 2
    #     # 若达上限则停止标注
    #     # if today_number >= day_limit:
    #     #     print("用户", user_id, "今日标注达到上限")
    #     #     return HttpResponse("今日标注结束")
    #     # 未标记的歌曲
    #     unmark_music_ids = user_musics.filter(is_mark=0).values('music_id')
    #     unmark_musics = list(Music.objects.filter(music_id__in=unmark_music_ids).values())

    end = len(unmark_musics) - 1
    if end < 0:
        print("用户", user_id, "本次标注达到上限")
        ## return HttpResponse("本次标注结束")
        return HttpResponse("没有需要标注的歌曲")
    index = random.randint(0, end)
    song = unmark_musics[index]
    info = {}
    info['music_id'] = str(song['music_id'])
    info['music_name'] = song['music_name']
    info['singer'] = song['singer']
    info['genre'] = song['genre']
    info['harmony_quantity'] = song['harmony_quantity']
    info['src'] = str(song['src'])
    info['marked_number'] = song['marked_number']

    info['marked_count'] = marked_count
    info['unmarked_count'] = unmarked_count

    data = json.dumps(info)
    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def clip_get_a_song_random(request):
    body = json.loads(request.body)
    user_id = body['user_id']
    # 测试用户没有歌曲限制
    if user_id == '1' or user_id == 1:
        marked_music = MarkedScore.objects.filter(user_id=user_id).values('music_id')
        unmark_musics = list(Music.objects.exclude(music_id__in=marked_music).values())
    # 专家
    else:
        user_musics = AssignUserMusic.objects.filter(user_id=user_id)
        ### 每天标注歌曲数限制 ###
        marked_clips = MarkedClip.objects.filter(user_id=user_id)
        # 本次标注的歌曲数
        total_number = user_musics.count()
        # 统计当天标的歌曲数
        now = datetime.now()
        today_number = 0
        for marked_clip in marked_clips:
            date = str(marked_clip.mark_time)
            date = date.split(" ")[0].split("-")
            if int(date[0]) == now.year and int(date[1]) == now.month and int(date[2]) == now.day:
                today_number += 1
        # 每天标注的歌曲数为 本批次标注的歌曲数/2
        if total_number % 2 == 1:
            day_limit = (total_number + 1) / 2
        else:
            day_limit = total_number / 2
        # 若达上限则停止标注
        # if today_number >= day_limit:
        #     print("用户", user_id, "今日标注达到上限")
        #     return HttpResponse("今日标注结束")
        # 未标记的歌曲
        unmark_music_ids = user_musics.filter(is_mark=0).values('music_id')
        unmark_musics = list(Music.objects.filter(music_id__in=unmark_music_ids).values())

    end = len(unmark_musics) - 1
    if end < 0:
        print("用户", user_id, "本次标注达到上限")
        return HttpResponse("本次标注结束")
    index = random.randint(0, end)
    song = unmark_musics[index]
    info = {}
    info['music_id'] = str(song['music_id'])
    info['music_name'] = song['music_name']
    info['singer'] = song['singer']
    info['genre'] = song['genre']
    info['harmony_quantity'] = song['harmony_quantity']
    info['src'] = str(song['src'])
    info['marked_number'] = song['marked_number']
    data = json.dumps(info)
    return HttpResponse(data, content_type="application/json")

## 
@csrf_exempt
def find_song_of_vocal_version(request):
    body = json.loads(request.body)
    song_name = body['song_name']
    singer_name = body['singer_name']
    
    try:
        song = Music_Vocal.objects.get(music_name=song_name, singer=singer_name)
        # print(f"Found song: {song}")

        info = {}
        info['music_id'] = str(song.music_id)
        info['music_name'] = song.music_name
        info['singer'] = song.singer
        info['genre'] = song.genre
        info['harmony_quantity'] = song.harmony_quantity
        info['src'] = str(song.src)
        info['marked_number'] = song.marked_number


        data = json.dumps(info)
        return HttpResponse(data, content_type="application/json")
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Song not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def find_song_of_instrumental_version(request):
    body = json.loads(request.body)
    song_name = body['song_name']
    singer_name = body['singer_name']

    song = Music_Instrumental.objects.get(music_name=song_name, singer=singer_name)

    info = {
        'music_id': str(song.music_id),
        'music_name': song.music_name,
        'singer': song.singer,
        'genre': song.genre,
        'harmony_quantity': song.harmony_quantity,
        'src': str(song.src),
        'marked_number': song.marked_number
    }

    data = json.dumps(info)
    return HttpResponse(data, content_type="application/json")

## 

# 修改歌曲流派
@csrf_exempt
def update_music_genre(request):
    body = json.loads(request.body)
    music_id = body['music_id']
    new_genre = body['new_genre']
    try:
        music = Music.objects.get(music_id=music_id)
    except Music.DoesNotExist:
        return HttpResponse("该记录不存在", status=400)
    music.genre = new_genre
    music.save()
    return HttpResponse("success")


# 修改歌曲和声
@csrf_exempt
def update_music_harmony_quantity(request):
    body = json.loads(request.body)
    music_id = body['music_id']
    new_harmony_quantity = body['new_harmony_quantity']
    try:
        music = Music.objects.get(music_id=music_id)
    except Music.DoesNotExist:
        return HttpResponse("该记录不存在", status=400)
    music.harmony_quantity = new_harmony_quantity
    music.save()
    return HttpResponse("success")


########### 评分部分 ##########

# 获取所有评分信息
def get_marked_scores(request):
    scores = MarkedScore.objects.all().values()
    scores = list(scores[:])
    data = json.dumps(scores, cls=MyEncoder)
    return HttpResponse(data, content_type="application/json")


# 获取用户所有的评分
@csrf_exempt
def get_user_scores(request):
    body = json.loads(request.body)
    user_id = body['user_id']
    scores = MarkedScore.objects.filter(user_id=user_id).values()
    scores = list(scores[:])
    infos = []
    for score in scores:
        music = Music.objects.filter(music_id=score['music_id_id']).values()
        music = list(music[:])
        info = {}
        info['score_id'] = score['score_id']
        info['music_name'] = music[0]['music_name']
        info['singer'] = music[0]['singer']
        info['score'] = score['score']
        info['mark_time'] = score['mark_time']
        infos.append(info)
    data = json.dumps(infos, cls=MyEncoder)
    return HttpResponse(data, content_type="application/json")


# 获取用户评分的总数
@csrf_exempt
def get_user_scores_number(request):
    body = json.loads(request.body)
    user_id = body['user_id']
    scores = MarkedScore.objects.filter(user_id=user_id).values()
    total_number = scores.count()
    return HttpResponse(total_number)


# 获取一页的用户评分
@csrf_exempt
def get_user_page_scores(request):
    body = json.loads(request.body)
    user_id = body['user_id']
    current_page = body['current_page']
    page_size = body['page_size']
    scores = MarkedScore.objects.filter(user_id=user_id).values()
    scores = list(scores[((current_page - 1) * page_size):(current_page * page_size)])
    infos = []
    for score in scores:
        music = Music.objects.filter(music_id=score['music_id_id']).values()
        music = list(music[:])
        ## 新增对于四个维度分的获取
        dimension_scores = DimensionScore.objects.filter(user_id=user_id, music_id=score['music_id_id']).values()
        dimension_score_0 = list(dimension_scores[:])[0]
        dimension_score_1 = list(dimension_scores[:])[1]
        dimension_score_2 = list(dimension_scores[:])[2]
        dimension_score_3 = list(dimension_scores[:])[3]
        ##
        info = {}
        info['score_id'] = score['score_id']
        info['music_id'] = music[0]['music_id']
        info['music_name'] = music[0]['music_name']
        info['singer'] = music[0]['singer']
        info['score'] = score['score']
        info['mark_time'] = score['mark_time']
        ## 新增对于四个维度分的获取
        info['dimension_score_0_id'] = dimension_score_0['dimension_score_id']
        info['dimension_score_0'] = dimension_score_0['dimension_score']
        info['dimension_score_1_id'] = dimension_score_1['dimension_score_id']
        info['dimension_score_1'] = dimension_score_1['dimension_score']
        info['dimension_score_2_id'] = dimension_score_2['dimension_score_id']
        info['dimension_score_2'] = dimension_score_2['dimension_score']
        info['dimension_score_3_id'] = dimension_score_3['dimension_score_id']
        info['dimension_score_3'] = dimension_score_3['dimension_score']
        ##
        infos.append(info)
    data = json.dumps(infos, cls=MyEncoder)
    return HttpResponse(data, content_type="application/json")


# 根据歌名查询评分记录
@csrf_exempt
def get_marked_scores_by_query(request):
    body = json.loads(request.body)
    query = body['query']
    user_id = body['user_id'] ##
    ## music_name_scores = MarkedScore.objects.filter(music_id__music_name__contains=query)
    music_name_scores = MarkedScore.objects.filter(music_id__music_name__contains=query, user_id=user_id)

    ## singer_scores = MarkedScore.objects.filter(music_id__singer__contains=query)
    ## score_scores = MarkedScore.objects.filter(score__contains=query)
    ## scores = score_scores.union(music_name_scores, singer_scores)
    ## music_name_scores = MarkedScore.objects.filter(music_id__music_name__contains=query, user_id = user_id)
    scores = music_name_scores
    # scores = MarkedScore.objects.filter(
    #     Q(music_id__music_name__contains=query) |
    #     Q(music_id__singer__contains=query) |
    #     Q(score__contains=query)
    # )
    ##

    # 无记录时返回查询不到？
    scores = scores.values()
    scores = list(scores[:])
    infos = []
    for score in scores:
        music = Music.objects.filter(music_id=score['music_id_id']).values()
        music = list(music[:])
        info = {}
        info['score_id'] = score['score_id']
        info['music_id'] = score['music_id_id']
        info['music_name'] = music[0]['music_name']
        info['singer'] = music[0]['singer']
        info['score'] = score['score']
        info['mark_time'] = score['mark_time']
        infos.append(info)
    data = json.dumps(infos, cls=MyEncoder)
    return HttpResponse(data, content_type="application/json")


# 创建新评分，若存在则覆盖
@csrf_exempt
def create_marked_score(request):
    body = json.loads(request.body)
    user = User.objects.get(user_id=body['user_id'])
    music = Music.objects.get(music_id=body['music_id'])
    if (MarkedScore.objects.filter(user_id=user, music_id=music).count() != 0):
        marked_score = MarkedScore.objects.get(user_id=user, music_id=music)
        marked_score.score = body['score']
        marked_score.mark_time = timezone.now()
        marked_score.save()
    else:
        marked_score = MarkedScore(user_id=user, music_id=music, score=body['score'])
        marked_score.save()
    music_id = body['music_id']
    marked_number = MarkedScore.objects.filter(music_id=music_id).count()
    Music.objects.filter(music_id=music_id).update(marked_number=marked_number)
    return HttpResponse("success")

## 维度分
@csrf_exempt
def create_dimension_score(request):
    body = json.loads(request.body)
    user = User.objects.get(user_id=body['user_id'])
    music = Music.objects.get(music_id=body['music_id'])
    dimension = body['dimension']
    if (DimensionScore.objects.filter(user_id=user, music_id=music, dimension=dimension).count() != 0):
        marked_score = DimensionScore.objects.get(user_id=user, music_id=music)
        marked_score.dimension_score = body['dimension_score']
        marked_score.mark_time = timezone.now()
        marked_score.save()
    else:
        marked_score = DimensionScore(user_id=user, music_id=music, dimension=body['dimension'], dimension_score=body['dimension_score'])
        marked_score.save()
    music_id = body['music_id']
    marked_number = DimensionScore.objects.filter(music_id=music_id).count()
    Music.objects.filter(music_id=music_id).update(marked_number=marked_number)
    return HttpResponse("success")
##


## 情感标签
@csrf_exempt
def create_music_emotion(request):
    body = json.loads(request.body)
    user = User.objects.get(user_id=body['user_id'])
    music = Music.objects.get(music_id=body['music_id'])
    emotion = body['emotion']
    if (MusicEmotion.objects.filter(user_id=user, music_id=music, emotion=emotion).count() != 0):
        marked_emotion = MusicEmotion.objects.get(user_id=user, music_id=music)
        marked_emotion.emotion = body['emotion']
        marked_emotion.mark_time = timezone.now()
        marked_emotion.save()
    else:
        marked_emotion = MusicEmotion(user_id=user, music_id=music, emotion=body['emotion'])
        marked_emotion.save()
    music_id = body['music_id']
    marked_number = MusicEmotion.objects.filter(music_id=music_id).count()
    Music.objects.filter(music_id=music_id).update(marked_number=marked_number)
    return HttpResponse("success")



# 修改单条评分
@csrf_exempt
def update_marked_score(request):
    body = json.loads(request.body)
    score_id = body['score_id']
    new_score = body['new_score']
    try:
        marked_score = MarkedScore.objects.get(score_id=score_id)
    except MarkedScore.DoesNotExist:
        return HttpResponse("该记录不存在", status=400)
    marked_score.score = new_score
    marked_score.mark_time = timezone.now()
    marked_score.save()
    return HttpResponse("success")


# 删除单条评分，并删除该评分相关的片段
@csrf_exempt
def delete_marked_score(request):
    body = json.loads(request.body)
    score_id = body['score_id']
    ## 新增删除四个维度分的评估结果
    dimension_score_0_id = body['dimension_score_0_id']
    dimension_score_1_id = body['dimension_score_1_id']
    dimension_score_2_id = body['dimension_score_2_id']
    dimension_score_3_id = body['dimension_score_3_id']
    ##
    try:
        marked_score = MarkedScore.objects.get(score_id=score_id)
    except MarkedScore.DoesNotExist:
        return HttpResponse("该记录不存在", status=400)
    ## 新增删除四个维度分的评估结果
    try:
        marked_dimension_score_0 = DimensionScore.objects.get(dimension_score_id=dimension_score_0_id)
    except DimensionScore.DoesNotExist:
        return HttpResponse("该维度分记录不存在", status=400)
    try:
        marked_dimension_score_1 = DimensionScore.objects.get(dimension_score_id=dimension_score_1_id)
    except DimensionScore.DoesNotExist:
        return HttpResponse("该维度分记录不存在", status=400)
    try:
        marked_dimension_score_2 = DimensionScore.objects.get(dimension_score_id=dimension_score_2_id)
    except DimensionScore.DoesNotExist:
        return HttpResponse("该维度分记录不存在", status=400)
    try:
        marked_dimension_score_3 = DimensionScore.objects.get(dimension_score_id=dimension_score_3_id)
    except DimensionScore.DoesNotExist:
        return HttpResponse("该维度分记录不存在", status=400)
    ##
    user_id = marked_score.user_id
    music_id = marked_score.music_id
    clips = MarkedClip.objects.filter(user_id=user_id, music_id=music_id)
    marked_score.delete()
    clips.delete()
    ## 新增删除四个维度分的评估结果
    marked_dimension_score_0.delete()
    marked_dimension_score_1.delete()
    marked_dimension_score_2.delete()
    marked_dimension_score_3.delete()
    ##
    return HttpResponse("success")


########### 维度评分部分 ##########

# 获取用户标记的该首歌的所有维度评价
@csrf_exempt
def get_user_music_dimension_scores(request):
    body = json.loads(request.body)
    user_id = body['user_id']
    music_id = body['music_id']
    response = []
    # 子维度
    ## dimension_scores = MarkedDimensionScore.objects.filter(user_id=user_id, music_id=music_id).exclude(dimension='加权平均分').values()
    ## dimension_scores = list(dimension_scores[:])
    ## response = response + dimension_scores
    # 将歌曲的流派和和声占比作为一个子维度放到维度列表中，使前端能够一并显示
    music = Music.objects.filter(music_id=music_id).values()
    ##
    ## print(music)
    ## music = Music.objects.filter(user_id=user_id, music_id=music_id).values()
    music = list(music[:])[0]
    music_genre = {}
    music_genre['dimension'] = '流派'
    music_genre['dimension_score'] = music['genre']
    ## music_harmony_quantity = {}
    ## music_harmony_quantity['dimension'] = '和声是否多'
    ## music_harmony_quantity['dimension_score'] = music['harmony_quantity']
    response.append(music_genre)
    ## response.append(music_harmony_quantity)
    # 将整体分数作为一个子维度放到维度列表中，使前端能够一并显示
    marked_score = MarkedScore.objects.filter(user_id=user_id, music_id=music_id).values()
    marked_score = list(marked_score[:])[0]
    marked_score['dimension'] = '整体分数'
    marked_score['dimension_score'] = marked_score['score']
    response.append(marked_score)
    ## 新增对四个维度的分数获取
    marked_dimension_score_0 = DimensionScore.objects.filter(user_id=user_id, music_id=music_id).values()
    marked_dimension_score_0 = list(marked_dimension_score_0[:])[0]
    response.append(marked_dimension_score_0)
    marked_dimension_score_1 = DimensionScore.objects.filter(user_id=user_id, music_id=music_id).values()
    marked_dimension_score_1 = list(marked_dimension_score_1[:])[1]
    response.append(marked_dimension_score_1)
    marked_dimension_score_2 = DimensionScore.objects.filter(user_id=user_id, music_id=music_id).values()
    marked_dimension_score_2 = list(marked_dimension_score_2[:])[2]
    response.append(marked_dimension_score_2)
    marked_dimension_score_3 = DimensionScore.objects.filter(user_id=user_id, music_id=music_id).values()
    marked_dimension_score_3 = list(marked_dimension_score_3[:])[3]
    response.append(marked_dimension_score_3)
    ##
    data = json.dumps(response, cls=MyEncoder)
    return HttpResponse(data, content_type="application/json")



# 创建新维度评分，若存在则覆盖

@csrf_exempt
def create_marked_dimension_score(request):
    body = json.loads(request.body)
    print(body)
    user = User.objects.get(user_id=body['user_id'])
    music = Music.objects.get(music_id=body['music_id'])
    dimension = body['dimension']
    if(MarkedDimensionScore.objects.filter(user_id=user, music_id=music, dimension=dimension).count()!=0):
        marked_dimension_score = MarkedDimensionScore.objects.get(user_id=user, music_id=music, dimension=dimension)
        marked_dimension_score.dimension_score = body['dimension_score']
        marked_dimension_score.mark_time = timezone.now()
        marked_dimension_score.save()
    else:
        marked_dimension_score = MarkedDimensionScore(user_id=user, music_id=music, dimension=body['dimension'], dimension_score=body['dimension_score'])
        marked_dimension_score.save()
    return HttpResponse("success")

# 修改单条维度评价
@csrf_exempt
def update_marked_dimension_score(request):
    body = json.loads(request.body)
    dimension_score_id = body['dimension_score_id']
    # new_dimension = body['new_dimension']
    new_dimension_score = body['new_dimension_score']
    try:
        ## marked_dimension_score = MarkedDimensionScore.objects.get(dimension_score_id=dimension_score_id)
        marked_dimension_score = DimensionScore.objects.get(dimension_score_id=dimension_score_id)
    ## except MarkedDimensionScore.DoesNotExist:
    except DimensionScore.DoesNotExist:
        return HttpResponse("该记录不存在", status=400)
    # marked_dimension_score.dimension = new_dimension
    marked_dimension_score.dimension_score = new_dimension_score
    marked_dimension_score.mark_time = timezone.now()
    marked_dimension_score.save()
    return HttpResponse("success")

# 删除单条维度评分
@csrf_exempt
def delete_marked_dimension_score(request):
    body = json.loads(request.body)
    dimension_score_id = body['dimension_score_id']
    try:
        dimension_score_id = MarkedDimensionScore.objects.get(dimension_score_id=dimension_score_id)
    except MarkedDimensionScore.DoesNotExist:
        return HttpResponse("该记录不存在", status=400)
    dimension_score_id.delete()
    return HttpResponse("success")


########### 歌唱片段部分 ##########

# 获取所有片段信息
def get_marked_clips(request):
    clips = MarkedClip.objects.all().values()
    clips = list(clips[:])
    data = json.dumps(clips, cls=MyEncoder)
    return HttpResponse(data, content_type="application/json")


# 获取用户的所有片段
@csrf_exempt
def get_user_clips(request):
    body = json.loads(request.body)
    user_id = body['user_id']
    music_id = body['music_id']
    clips = MarkedClip.objects.filter(user_id=user_id, music_id=music_id).values()
    clips = list(clips[:])
    infos = []
    for clip in clips:
        music = Music.objects.filter(music_id=clip['music_id_id']).values()
        music = list(music[:])
        info = {}
        info['clip_id'] = clip['clip_id']
        # info['music_name'] = music[0]['music_name']
        # info['singer'] = music[0]['singer']
        info['start_time'] = clip['start_time']
        info['end_time'] = clip['end_time']
        info['type'] = clip['type']
        # info['clip_score'] = clip['clip_score']
        # info['mark_time'] = clip['mark_time']
        infos.append(info)
    data = json.dumps(infos, cls=MyEncoder)
    return HttpResponse(data, content_type="application/json")


# 获取用户标记的该首歌的所有片段
@csrf_exempt
def get_user_music_clips(request):
    body = json.loads(request.body)
    user_id = body['user_id']
    music_id = body['music_id']
    clips = MarkedClip.objects.filter(user_id=user_id, music_id=music_id).values()
    clips = list(clips[:])
    data = json.dumps(clips, cls=MyEncoder)
    return HttpResponse(data, content_type="application/json")


# 创建新片段
@csrf_exempt
def create_marked_clip(request):
    body = json.loads(request.body)
    user_id = User.objects.get(user_id=body['user_id'])
    music_id = Music.objects.get(music_id=body['music_id'])
    # clip_score = body['clip_score']
    clip = MarkedClip(user_id=user_id, music_id=music_id, start_time=body['start_time'], end_time=body['end_time'], type=body['type'])
    # 更新标记次数
    AssignUserMusic.objects.filter(user_id=user_id, music_id=music_id).update(is_mark=1)
    clip.save()
    return HttpResponse("success")


# 修改单条片段
@csrf_exempt
def update_marked_clip(request):
    body = json.loads(request.body)
    clip_id = body['clip_id']
    # new_type = body['new_type']
    new_start_time = body['new_start_time']
    new_end_time = body['new_end_time']
    try:
        marked_clip = MarkedClip.objects.get(clip_id=clip_id)
    except MarkedClip.DoesNotExist:
        return HttpResponse("该记录不存在", status=400)
    # marked_clip.type = new_type
    marked_clip.start_time = new_start_time
    marked_clip.end_time = new_end_time
    marked_clip.mark_time = timezone.now()
    marked_clip.save()
    return HttpResponse("success")


# 删除单条片段
@csrf_exempt
def delete_marked_clip(request):
    body = json.loads(request.body)
    clip_id = body['clip_id']
    try:
        marked_clip = MarkedClip.objects.get(clip_id=clip_id)
    except MarkedClip.DoesNotExist:
        return HttpResponse("该记录不存在", status=400)
    marked_clip.delete()
    return HttpResponse("success")











from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30, default='', unique=True)
    user_phone = models.CharField(max_length=12)
    user_password = models.CharField(max_length=32)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)


class Music(models.Model):
    music_id = models.AutoField(primary_key=True)
    music_name = models.CharField(max_length=30, default='')
    singer=models.CharField(max_length=30, default='')
    genre = models.CharField(max_length=30, default='')
    harmony_quantity = models.IntegerField(default=0)  # 0不多1多
    src = models.FileField(max_length=300, default=None)
    marked_number = models.IntegerField(default=0)


class MarkedScore(models.Model):
    score_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=User, db_column='user_id', on_delete=models.CASCADE)
    music_id = models.ForeignKey(to=Music, db_column='music_id', on_delete=models.CASCADE)
    score = models.IntegerField(default=-1)
    mark_time = models.DateTimeField(default = timezone.now)


class MarkedClip(models.Model):
    clip_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=User, db_column='user_id', on_delete=models.CASCADE)
    music_id = models.ForeignKey(to=Music, db_column='music_id', on_delete=models.CASCADE)
    start_time = models.DecimalField(max_digits=10, decimal_places=3,default=0)  # Time in seconds with millisecond precision
    end_time = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    type = models.CharField(max_length=30, default='')
    # clip_score = models.IntegerField(default=-1)
    mark_time = models.DateTimeField(default = timezone.now)

class MarkedDimensionScore(models.Model):
    dimension_score_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=User, db_column='user_id', on_delete=models.CASCADE)
    music_id = models.ForeignKey(to=Music, db_column='music_id', on_delete=models.CASCADE)
    dimension = models.CharField(max_length=30, default='')
    dimension_score = models.IntegerField(default=-1)
    mark_time = models.DateTimeField(default = timezone.now)


class AssignUserMusic(models.Model):
    assign_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=User, db_column='user_id', on_delete=models.CASCADE)
    music_id = models.ForeignKey(to=Music, db_column='music_id', on_delete=models.CASCADE)
    is_mark = models.IntegerField(default=0) # 是否标注

class DimensionScore(models.Model):
    dimension_score_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=User, db_column='user_id', on_delete=models.CASCADE)
    music_id = models.ForeignKey(to=Music, db_column='music_id', on_delete=models.CASCADE)
    dimension = models.CharField(max_length=30, default='')
    dimension_score = models.IntegerField(default=-1)
    mark_time = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = 'DimensionScore'


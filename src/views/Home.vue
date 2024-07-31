<template>
  <el-row>
    <el-col :span="8">
      <el-card class="box-card" style="margin-top: 30px">
        <div class="user">
          <img src="../assets/images/xitured.jpg" alt="">
          <div class="userinfo">
            <p class="name">{{ username }}</p>
            <p class="access">教师</p>
          </div>
        </div>
        <div class="login-info">
          <p>本次登录时间：<span>{{ nowtime }}</span></p>
          <p>本次登录地点：<span>西安</span></p>
        </div>
      </el-card>
      <el-card style="margin-top: 20px; height: 430px">
        <el-table
            :data="tableData"
            style="width: 100%">
          <el-table-column
              prop="music"
              label="音乐"
              width="180">
          </el-table-column>
          <el-table-column
              prop="name"
              label="歌手"
              width="180">
          </el-table-column>
          <el-table-column
              prop="score"
              label="分数">
          </el-table-column>
        </el-table>
      </el-card>
    </el-col>
    <el-col :span="16">
      <el-card class="box-card" style="margin-left: 60px; margin-top: 80px;">
        <div class="demo1-video" style="margin-left: 40px;  width: 800px;height: 600px">
          <div class="song-name">使用说明</div>
          <div class="A-name">1.听到技巧后可点击后退1s,然后开始标注</div>
          <div class="B-name">2.对应技巧按钮点击第一下记录开始时间，再点一下记录结束时间</div>
          <br>
          <div class="B-name">3.进入评价页面先点击下一首获取歌曲</div>
          <div class="B-name">4.如果技巧起始时间标注错误，可点击重新标注</div>
          <div class="B-name">5.可在查看标注技巧那里查看已标注过的技巧，同时对于标注错误的，可在此删除后重新标注</div>
          <br>
          <div class="B-name">6.标注完一首歌，点击下一首切换歌曲</div>
          <div class="B-name">7.点击标记过的技巧可以播放对应技巧片段</div>
          <div class="B-name">
            8.拖动片段的两条红线可以修改开始结束时间，拖动后再点击技巧颜色部分可播放两条红线间的片段，修改完成后点击修改标注进行保存
          </div>
          <!--          <div class="B-name" style="color: crimson">9.按住（ctrl+鼠标滑轮）调节浏览器页面缩放，笔记本推荐页面为90%</div>-->
          <!--          <Video id="myVideo" class="自定义" controls preload="auto" style="margin-left: 40px;  width: 800px;height: 600px">-->
          <!--            <source src="../assets/mp4/陈奕迅-孤勇者.mp4" type="video/mp4">-->

          <!--          </Video>-->
        </div>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
import {getData} from '../api'
import Cookie from "js-cookie";

export default {
  data() {
    return {
      user_name: '',
      userid: '',
      user_id: '',
      username: '',
      tableData: [],
      nowtime: ""
    }
  },
  mounted() {
    getData().then(({data}) => {
      const {tableData} = data.data
      this.tableData = tableData
    })

    function getNowDate() {

    }

    function getusername() {

    }

    function getuserid() {

    }

    getuserid()
    {
      this.user_id = this.$route.params.user_id
      this.userid = sessionStorage.getItem('user_id');
      console.log(this.userid)
    }
    getNowDate()
    {
      var year = new Date().getFullYear()
      var month = new Date().getMonth() + 1;
      var day = new Date().getDate();
      this.nowtime = year + "/" + month + "/" + day;
      console.log(this.nowtime)
    }
    getusername()
    {
      this.user_name = this.$route.params.user_name
      this.username = sessionStorage.getItem('user_name');
      console.log(this.username)
    }
  },
}
</script>

<style lang="less" scoped>
.user {
  padding-bottom: 20px;
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
  display: flex;
  align-items: center;

  img {
    margin-right: 40px;
    width: 150px;
    height: 150px;
    border-radius: 50%;
  }

  .userinfo {
    .name {
      font-size: 32px;
      margin-bottom: 10px;
    }

    .access {
      color: #999999;
    }
  }
}

.login-info {
  p {
    line-height: 28px;
    font-size: 14px;
    color: #999999;

    span {
      color: #666666;
      margin-left: 60px;
    }
  }
}

.song-name {
  height: 25px;
  font-family: PingFangSC-Regular;
  font-size: 45px;
  color: #000000;
  text-align: center;
  font-weight: 400;
  margin-bottom: 15px;
}

.A-name {
  height: 25px;
  font-family: PingFangSC-Regular;
  font-size: 30px;
  margin-top: 45px;
  color: #000000;
  text-align: left;
  font-weight: 400;
  margin-bottom: 15px;
}

.B-name {
  height: 25px;
  font-family: PingFangSC-Regular;
  font-size: 30px;
  margin-top: 25px;
  color: #000000;
  text-align: left;
  font-weight: 400;
  margin-bottom: 15px;
}
</style>
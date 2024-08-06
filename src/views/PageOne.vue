<template>
  <div>
    <div>
      <el-dialog
          class="mydialog"
          :close-on-click-modal="false"
          :visible.sync="Visible"
          width="80%"
      >
        <!--    <el-button type="primary" size="medium" style="height: 50px;margin-top: 200px;margin-left: 350px;margin-bottom: 200px" @click="musicNext1">开始评价</el-button>-->
        <br><br>
        <el-button type="primary" size="small" @click="musicNext1" center width="50%"
                   style="margin-top: -30px;margin-left: 40%;width: 150px;height: 50px" class="dialog-box-center">开始评价
        </el-button>
        <br><br><br><br>
      </el-dialog>

      <el-dialog
          class="mydialog"
          :close-on-click-modal="false"
          :visible.sync="sb"
          width="80%"
          :before-close="sbClose">
        <el-button type="primary" size="small" center width="50%"
                   style="margin-top: -30px;margin-left: 40%;width: 150px;height: 50px" class="dialog-box-center">标注结束
        </el-button>
      </el-dialog>


    </div>
    <div class="audio-player" style="margin-top:10px; margin-left:10px">
      <div style="margin-top: 20px">
        <el-col :span="10">
          <el-card class="box-card" style="margin-top: 2px;width: 100%">
            <span>歌曲：{{ name }}</span>&nbsp&nbsp<span>id：{{ id }}</span>&nbsp&nbsp<span>流派：{{ genre }}</span>
            <br>
            <div style="margin-top: 5px">
              <el-button @click="musicPre" type="primary">上一首</el-button>
              <el-button @click="musicPlay" type="primary">暂停/播放</el-button>
              <el-button @click="musicNext" type="primary">下一首</el-button>
            </div>

            <div style="margin-top: 5px">
              <!--      <span>{{src}}</span>-->
              <audio ref="audio"
                     @timeupdate="onTimeupdate"
                     @loadedmetadata="onLoadedmetadata"
                     controls="controls"
              >
                <source :src='require("@/assets/mp3/" + singer + "-" + name + "_(Vocals)" + ".wav")' type="audio/wav">
                <!--                <source :src='require("@/assets/mp3/"+ name +".wav")' type="audio/wav">-->
              </audio>
              <!--              <audio src="../assets/wav/胡夏-那些年_(Vocals).wav" controls autoplay></audio>-->
            </div>
            <el-slider v-model="sliderTime" :format-tooltip="formatProcessToolTip" @change="changeCurrentTime"
                       class="slider">

            </el-slider>
            <span class="current">{{ audio.currentTime | formatSecond }}</span>
            <span class="duration">/{{ audio.maxTime | formatSecond }}</span>
            <br>
            <div style="margin-top: 1vh">
              <!--              <el-button @click="start" type="primary">开始</el-button>-->
              <!--              <el-button @click="end" style="margin-left: 10px;" type="primary">结束-->
              <!--              </el-button>-->
              <!--              <el-button @click="inputpd" type="primary">提交</el-button>&nbsp;&nbsp;起始时间：{{-->
              <!--                this.bb + ':' + this.cc-->
              <!--              }}&nbsp;结束时间：{{ this.dd + ':' + this.ee }}-->


            </div>
          </el-card>
          <el-card style="margin-top: 20px; height: 452px">

            <el-table
                :row-style="{height:'12px'}"
                :cell-style="{padding:'7px'}"
                :data="testData"
                style="width: 100%;font-size: 13px"
                :row-class-name="tableRowClassName">
              <el-table-column
                  prop="date"
                  label="种类"
                  width="120">
              </el-table-column>
              <el-table-column
                  prop="name"
                  label="描述"
                  width="435">
              </el-table-column>
            </el-table>


          </el-card>
        </el-col>
      </div>
      <el-col :span="14">
        <el-card class="box-card" style="margin-left: 30px; ">
          <div class="demo1-video" style="margin-left: 20px;  width: 900px;height: 710px">

            <el-form ref="form" label-width="70px" :inline="true" :model="form" :rules="rules"
                     style="margin: 5px 10px">

              <h3>整体质量</h3>
              <el-form ref="form" label-width="70px" style="margin-top: 20px;" :inline="true"
                       :model="form"
                       :rules="rules">
                <el-tooltip class="item" effect="dark" content="Right Bottom 提示文字" placement="left-start">
                  <div slot="content">
                    90-100分：表现完美，音色悦耳具有辨识度，技巧发挥成熟自然，<br/>情感张力大，能打动人心；<br/><br/>80-89分：
                    表现良好，音色悦耳，技巧发挥成熟自然，<br/>有一定的情感表现；
                    <br/><br/>70-79分： 个别音音准、节奏把握不准确，气息稳定，共鸣较好，<br/>但部分技巧使用发挥不够成熟，情感表现较弱；<br/><br/>60-69分：
                    个别乐句音准、节奏把握不准确，音域也基本可以达到歌曲要求<br/>但整体的气息不够稳定，声乐技巧上的使用不够成熟，情感表现弱；
                    <br/><br/>59分以下： 有1/3的音准节奏问题，音域达不到歌曲要求；<br/>其他共鸣技巧等发挥也都比较糟糕，大白嗓严重；
                  </div>
                  <el-button>评分</el-button>
                </el-tooltip>
                <el-form-item prop="score" style="margin-left: 90px">
                  <el-input v-model="form.score" placeholder="请输入分数"></el-input>
                </el-form-item>
                <!--              <el-form-item>-->
                <!--                <el-button @click="submit" type="primary">提交</el-button>-->
                <!--              </el-form-item>-->
              </el-form>
              
              <h3>旋律</h3>
              <el-form ref="form" label-width="70px" style="margin-top: 20px;" :inline="true"
                       :model="form"
                       :rules="rules">
                <el-tooltip class="item" effect="dark" content="Right Bottom 提示文字" placement="left-start">
                  <div slot="content">
                    90-100分：None，<br/>None；<br/><br/>80-89分：
                    None，<br/>None；
                    <br/><br/>70-79分： None，<br/>但部分技巧使用发挥不够成熟，情感表现较弱；<br/><br/>60-69分：
                    个别乐句音准、节奏把握不准确，音域也基本可以达到歌曲要求<br/>但整体的气息不够稳定，声乐技巧上的使用不够成熟，情感表现弱；
                    <br/><br/>59分以下： 有1/3的音准节奏问题，音域达不到歌曲要求；<br/>其他共鸣技巧等发挥也都比较糟糕，大白嗓严重；
                  </div>
                  <el-button>评分</el-button>
                </el-tooltip>
                <el-form-item prop="score2" style="margin-left: 90px">
                  <el-input v-model="form.score2" placeholder="请输入分数"></el-input>
                </el-form-item>
                <!--              <el-form-item>-->
                <!--                <el-button @click="submit" type="primary">提交</el-button>-->
                <!--              </el-form-item>-->
              </el-form>
              
              <h3>演唱</h3>
              <el-form ref="form" label-width="70px" style="margin-top: 20px;" :inline="true"
                       :model="form"
                       :rules="rules">
                <el-tooltip class="item" effect="dark" content="Right Bottom 提示文字" placement="left-start">
                  <div slot="content">
                    90-100分：表现完美，音色悦耳具有辨识度，技巧发挥成熟自然，<br/>情感张力大，能打动人心；<br/><br/>80-89分：
                    表现良好，音色悦耳，技巧发挥成熟自然，<br/>有一定的情感表现；
                    <br/><br/>70-79分： 个别音音准、节奏把握不准确，气息稳定，共鸣较好，<br/>但部分技巧使用发挥不够成熟，情感表现较弱；<br/><br/>60-69分：
                    个别乐句音准、节奏把握不准确，音域也基本可以达到歌曲要求<br/>但整体的气息不够稳定，声乐技巧上的使用不够成熟，情感表现弱；
                    <br/><br/>59分以下： 有1/3的音准节奏问题，音域达不到歌曲要求；<br/>其他共鸣技巧等发挥也都比较糟糕，大白嗓严重；
                  </div>
                  <el-button>评分</el-button>
                </el-tooltip>
                <el-form-item prop="score3" style="margin-left: 90px">
                  <el-input v-model="form.score3" placeholder="请输入分数"></el-input>
                </el-form-item>
                <!--              <el-form-item>-->
                <!--                <el-button @click="submit" type="primary">提交</el-button>-->
                <!--              </el-form-item>-->
              </el-form>
              
              <h3>编曲</h3>
              <el-form ref="form" label-width="70px" style="margin-top: 20px;" :inline="true"
                       :model="form"
                       :rules="rules">
                <el-tooltip class="item" effect="dark" content="Right Bottom 提示文字" placement="left-start">
                  <div slot="content">
                    90-100分：表现完美，音色悦耳具有辨识度，技巧发挥成熟自然，<br/>情感张力大，能打动人心；<br/><br/>80-89分：
                    表现良好，音色悦耳，技巧发挥成熟自然，<br/>有一定的情感表现；
                    <br/><br/>70-79分： 个别音音准、节奏把握不准确，气息稳定，共鸣较好，<br/>但部分技巧使用发挥不够成熟，情感表现较弱；<br/><br/>60-69分：
                    个别乐句音准、节奏把握不准确，音域也基本可以达到歌曲要求<br/>但整体的气息不够稳定，声乐技巧上的使用不够成熟，情感表现弱；
                    <br/><br/>59分以下： 有1/3的音准节奏问题，音域达不到歌曲要求；<br/>其他共鸣技巧等发挥也都比较糟糕，大白嗓严重；
                  </div>
                  <el-button>评分</el-button>
                </el-tooltip>
                <el-form-item prop="score4" style="margin-left: 90px">
                  <el-input v-model="form.score4" placeholder="请输入分数"></el-input>
                </el-form-item>
                <!--              <el-form-item>-->
                <!--                <el-button @click="submit" type="primary">提交</el-button>-->
                <!--              </el-form-item>-->
              </el-form>
              
              <h3>音频质量</h3>
              <el-form ref="form" label-width="70px" style="margin-top: 20px;" :inline="true"
                       :model="form"
                       :rules="rules">
                <el-tooltip class="item" effect="dark" content="Right Bottom 提示文字" placement="left-start">
                  <div slot="content">
                    90-100分：表现完美，音色悦耳具有辨识度，技巧发挥成熟自然，<br/>情感张力大，能打动人心；<br/><br/>80-89分：
                    表现良好，音色悦耳，技巧发挥成熟自然，<br/>有一定的情感表现；
                    <br/><br/>70-79分： 个别音音准、节奏把握不准确，气息稳定，共鸣较好，<br/>但部分技巧使用发挥不够成熟，情感表现较弱；<br/><br/>60-69分：
                    个别乐句音准、节奏把握不准确，音域也基本可以达到歌曲要求<br/>但整体的气息不够稳定，声乐技巧上的使用不够成熟，情感表现弱；
                    <br/><br/>59分以下： 有1/3的音准节奏问题，音域达不到歌曲要求；<br/>其他共鸣技巧等发挥也都比较糟糕，大白嗓严重；
                  </div>
                  <el-button>评分</el-button>
                </el-tooltip>
                <el-form-item prop="score5" style="margin-left: 90px">
                  <el-input v-model="form.score5" placeholder="请输入分数"></el-input>
                </el-form-item>
                <!--              <el-form-item>-->
                <!--                <el-button @click="submit" type="primary">提交</el-button>-->
                <!--              </el-form-item>-->
              </el-form>
              
              <el-button size="mini">情感标签是否正确</el-button>
              &nbsp&nbsp&nbsp
              &nbsp&nbsp&nbsp
              <el-radio-group v-model="radio" @input="dayin11" style="padding-left: 25px">
                <el-radio :label="1">是</el-radio>
                <el-radio :label="0">否</el-radio>
              </el-radio-group>
              &nbsp&nbsp&nbsp&nbsp&nbsp

              <el-select v-model="value" @change="dylog" :disabled="isable" placeholder="请选择" size="mini">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
              </el-select>
              <br>
              

              
              <el-button style="margin-left: 25vh" @click="submit" type="primary">提交</el-button>
              <br>
              <!--              <el-divider style="margin-top: 10px"></el-divider>-->
              

              

              

            </el-form>

          </div>
        </el-card>
      </el-col>

    </div>
  </div>
</template>

<script>

import APlayer from 'vue-aplayer'
import {
  getSongs,
  getASongRandom,
  createMarkedScore,
  createMarkedClip,
  createMarkedDimensionScore,
  updateMusicGenre, updateMusicHarmonyQuantity,
  createDimensionScore
} from "@/api/api";
import {user_id} from "@/store/getters";

function realFormatSecond(second) {
  var secondType = typeof second

  if (secondType === 'number' || secondType === 'string') {
    second = parseInt(second)

    var hours = Math.floor(second / 3600)
    second = second - hours * 3600
    var mimute = Math.floor(second / 60)
    second = second - mimute * 60

    return hours + ':' + ('0' + mimute).slice(-2) + ':' + ('0' + second).slice(-2)
  } else {
    return '0:00:00'
  }
}


export default {
  name: "User",
  components: {APlayer},
  props: {
    // 显示隐藏
    isShowAudioPlayer: {
      default: true,
    },
  },
  data() {
    return {
      Visible: true,
      radio: 1,
      ///radio1: -1,
      ///radio2: -1,
      ///radio3: -1,
      ///radio4: -1,
      ///radio5: -1,
      ///radio6: -1,
      ///radio7: -1,
      ///radio8: -1,
      ///radio9: -1,
      ///radio10: '',
      radio11: '',
      ismark: [],
      form: {
        score: '',
        score2: '', ///
        score3: '', ///
        score4: '', ///
        score5: '', ///
        
        clip_score: '',
        dimension_score: ''
      },
      // startTime: '',
      // endTime: '',
      audio: {
        currentTime: 0,
        maxTime: 0,
        playing: false,
        muted: false,
        speed: 1,
        // waiting: true,
        preload: 'auto'
      },
      sliderTime: 0,
      crules: {
        dimension_score: [
          {required: true, trigger: 'blur', message: '请输入维度分数'}
        ]
      },
      rules: {
        score: [
          {required: true, trigger: 'blur', message: '请输入分数'}
        ]
      },
      playIcon: require("../assets/play.png"),
      plozeIcon: require("../assets/ploze.png"),
      vulumnIcon: require("../assets/vulumn.png"),
      mutedIcon: require("../assets/muted3.png"),
      closeIcon: require("../assets/close.png"),
      leftIcon: require("../assets/leftwhite.png"),
      nextIcon: require("../assets/next.png"),
      box: undefined,
      play: false, // 播放状态，true为正在播放
      sliderValVolumn: 0.5, // 音量
      copySliderValVolumn: 0.5,
      isone: 1,
      start_time: -1,
      end_time: -1,
      bb: '00',
      cc: '00',
      dd: '00',
      ee: '00',
      ///clip1: '',
      ///clip2: '',
      ///clip3: '',
      ///clip4: '',
      ///clip5: '',
      ///clip6: '',
      ///clip7: '',
      ///clip8: '',
      ///clip9: '',
      clip10: '',
      ///type1: '音色与辨识度',
      ///type2: '音量与音域',
      ///type3: '音准、节奏',
      ///type4: '发音咬字',
      ///type5: '常规技巧',
      ///type6: '个性化技巧',
      ///type7: '戏剧性',
      ///type8: '叙事性',
      ///type9: '熟悉度',
      type10: '加权平均分',

      dimension_type: '维度1',///
      dimension_type2: '维度2',///
      dimension_type3: '维度3',///
      dimension_type4: '维度4',///
      dimension_type5: '维度5',///

      ///ishs: '',
      isable: true,
      isliupai: 1,
      new_genre: "",
      genre: "",
      type: -1,
      test: 1,
      sb: false,
      id: "",
      name: "点击下一首开始评价",
      singer: "",
      index: 0, // 当前播放的音乐索引
      playedMusic: [],
      options: [{
        value: '情感1',
        label: '情感1'
      }, {
        value: '情感2',
        label: '情感2'
      }, {
        value: '情感3',
        label: '情感3'
      }, {
        value: '情感4',
        label: '情感4'
      }],
      value: '',
      label: '',
      testData: [{
        date: '音色与辨识度',
        name: '歌手是否有明确的音色特点（如磁性、浑厚、清亮、纯净、温暖、丰满等）；\n' +
            '声音是否具有辨识度；',
      }, {

        date: '音量与音域',
        name: '音域范围；\n' +
            '动态范围（音量）；',
      }, {
        date: '音准、节奏',
        name: '音准、节奏把握是否准确',
      }, {
        date: '发音咬字',
        name: '发音咬字（吐字、归韵收音）是否清晰自然',
      }, {
        date: '常规技巧',
        name: '有效的气息管理：气息的平稳度、控制力强、自然的换气。\n' +
            '\n' +
            ' 共鸣（胸腔、头腔、鼻腔等）、声区转换平稳统一。\n',

      }, {
        date: '个性化技巧',
        name: '真假声转换及装饰音运用，滑音、颤音、跳音、转音、气泡声等技巧。',

      }, {
        date: '戏剧性',
        name: '段落、乐句的情绪对比；声音的穿透力、爆发力',

      }, {
        date: '叙事性',
        name: '\n' +
            '将语言中的语气感融入演唱技巧中，声音打动人心；\n',
      },
      ]
    }
  },
  mounted() {
    // this.getMusic()
    this.init();
    this.getAudioDuration()
  },
  beforeDestroy() {
    this.isShow = true
  },
  filters: {
    // 使用组件过滤器来动态改变按钮的显示
    // transPlayPause(value) {
    //   return value ? '暂停' : '播放'
    // },
    // 将整数转化成时分秒
    formatSecond(second = 0) {
      return realFormatSecond(second)
    }
  },
  methods: {
    init() {
      this.box = this.$refs["audio"];
      // this.box.src = require(`${this.list[this.index].src}`);
      this.box.src = require(`${this.src}`);
      console.log(this.box, "音频播放器DOM");
      const that = this;

      //  this.duration  =  this.formatTime(this.box.duration)
      // 绑定三个触发方法
      // 当时长有变化时触发，由"NaN"变为实际时长也算
      this.box.ondurationchange = function () {
        console.log("时长发生了变化");
        console.log(that.box.duration);
        // that.
        // that.duration  =  that.formatTime(that.box.duration)
        that.sliderMax = Math.floor(that.box.duration);
        that.updateTime();
      };
      // 当前数据可用是触发
      this.box.oncanplay = function () {
        console.log("已经可以播放了");
      };
      // 播放位置发送改变时触发。
      this.box.ontimeupdate = function () {
        console.log("播放位置发送了变动");
        that.updateTime();
      };
      // 音频播放完毕
      this.box.onended = function () {
        console.log("播放完毕，谢谢收听");
      };
      // 音频播放完毕
      this.box.onerror = function () {
        console.log("加载出错！");
      };
    },
    ///dayin1(val) {
    ///  console.log(val)
    ///  this.clip1 = val
    ///},
    ///dayin2(val) {
    ///  console.log(val)
    ///  this.clip2 = val
    ///},
    ///dayin3(val) {
    ///  console.log(val)
    ///  this.clip3 = val
    ///},
    ///dayin4(val) {
    ///  console.log(val)
    ///  this.clip4 = val
    ///},
    ///dayin5(val) {
    ///  console.log(val)
    ///  this.clip5 = val
    ///},
    ///dayin6(val) {
    ///  console.log(val)
    ///  this.clip6 = val
    ///},
    ///dayin7(val) {
    ///  console.log(val)
    ///  this.clip7 = val
    ///},
    ///dayin8(val) {
    ///  console.log(val)
    ///  this.clip8 = val
    ///},
    ///dayin9(val) {
    ///  console.log(val)
    ///  this.clip9 = val
    ///},
    ///dayin10(val) {
    ///  this.ishs = val
    ///  console.log(this.ishs)
    ///},
    dayin11(val) {
      console.log(val)
      this.isliupai = val
      if (this.isliupai === 0) {
        this.isable = false
      } else {
        this.isable = true
      }
    },
    dylog(setval) {
      if (this.isliupai === 0) {
        this.new_genre = setval
        console.log(this.new_genre)
      }
    },
    getSkillValue() {
      this.type = this.value
      console.log(this.value)
      // axios({
      //   methods: "POST",
      //   url:"#",
      //   data:{
      //     value:this.value
      //   }
      // })
    },
    getAudioDuration() {
      this.audioDuration = this.$refs.audioPlayer.duration;
      setInterval(() => {
        this.currentProgress = this.$refs.audioPlayer.currentTime;
      }, 1000);
    },
    chanyin() {
      this.type = '颤音'
      console.log(this.type)
    },
    start() {
      let aa = Math.floor(this.audio.currentTime)
      this.bb = Math.floor(aa / 60)
      this.cc = Math.floor(aa % 60)
      this.start_time = this.audio.currentTime
      if (this.bb >= 0 && this.bb < 10) {
        this.bb = '0' + this.bb
      }
      if (this.cc >= 0 && this.cc < 10) {
        this.cc = '0' + this.cc
      }
      console.log(this.bb + ':' + this.cc)
      // console.log(aa)
      console.log(this.start_time)
    },
    end() {
      let ff = Math.floor(this.audio.currentTime)
      this.dd = Math.floor(ff / 60)
      this.ee = Math.floor(ff % 60)
      this.end_time = this.audio.currentTime
      if (this.dd >= 0 && this.dd < 10) {
        this.dd = '0' + this.dd
      }
      if (this.ee >= 0 && this.ee < 10) {
        this.ee = '0' + this.ee
      }
    },
    inputpd() {
      if (this.start_time === -1) {
        this.$message({
          type: 'false',
          message: '未选择起始时间!'
        });
      } else if (this.end_time === -1) {
        this.$message({
          type: 'false',
          message: '未选择结束时间!'
        });
      } else {
        createMarkedClip({
          'user_id': sessionStorage.getItem('user_id'),
          'music_id': this.id,
          'start_time': this.start_time,
          'end_time': this.end_time,
        }).then(response => {
          // console.log(response.data)
          this.start_time = -1
          this.end_time = -1
          console.log(this.form.clip_score)
          console.log(this.start_time)
          this.$message({
            type: 'success',
            message: '提交成功!'
          });
        })
      }
    },
    newMarkedDimensionScore() {
      if (this.form.dimension_score === '') {
        this.form.dimension_score = -1
      }
      createMarkedDimensionScore({
        'user_id': sessionStorage.getItem('user_id'),
        'music_id': this.id,
        'dimension': this.type,
        'dimension_score': this.form.dimension_score,
      })
    },
    clipsubmit() {
      if (this.form.clip_score === '') {
        this.$message({
          type: 'false',
          message: '未输入局部分!'
        });
      } else if (this.start_time === -1) {
        this.$message({
          type: 'false',
          message: '未选择起始时间!'
        });
      } else if (this.end_time === -1) {
        this.$message({
          type: 'false',
          message: '未选择结束时间!'
        });
      } else if (this.type === -1) {
        this.$message({
          type: 'false',
          message: '未选择分类!'
        });
      } else {
        createMarkedClip({
          'user_id': sessionStorage.getItem('user_id'),
          'music_id': this.id,
          'clip_score': this.form.clip_score,
          'start_time': this.start_time,
          'end_time': this.end_time,
          'type': this.type
        }).then(response => {
          // console.log(response.data)
          this.form.clip_score = ''
          this.start_time = -1
          this.end_time = -1
          this.type = -1
          console.log(this.form.clip_score)
          console.log(this.start_time)
          this.$message({
            type: 'success',
            message: '提交成功!'
          });
        })
      }
    },

    async submit() {
      console.log('score', this.form.score);///
      console.log('score2:', this.form.score2);///
      console.log('score3:', this.form.score3);///
      console.log('score4:', this.form.score4);///
      console.log('score5:', this.form.score5);///
      if (this.form.score === '') {
        this.$message({
          type: 'false',
          message: '未输入分数!'
        });
      } else {
        if (this.form.score > 100 || this.form.score < 0) {
          this.$message({
            type: 'false',
            message: '分数在0-100之间!'
          });
        } else if (this.form.score2 === '' || this.form.score3 === '' || this.form.score4 === '' || this.form.score5 === '') {
          this.$message({
            type: 'false',
            message: '有维度未标注!'
          });
        } else {
          
          ///this.radio1 = ''
          ///this.radio2 = ''
          ///this.radio3 = ''
          ///this.radio4 = ''
          ///this.radio5 = ''
          ///this.radio6 = ''
          ///this.radio7 = ''
          ///this.radio8 = ''
          ///this.clip1 = ''
          ///this.clip2 = ''
          ///this.clip3 = ''
          ///this.clip4 = ''
          ///this.clip5 = ''
          ///this.clip6 = ''
          ///this.clip7 = ''
          ///this.clip8 = ''
          ///this.type = this.type9
          ///this.form.dimension_score = this.clip9
          ///this.radio9 = ''
          ///await this.newMarkedDimensionScore()
          ///this.clip9 = ''
          if (this.isliupai === 1) {
            this.new_genre = this.genre
          }
          await updateMusicGenre({'new_genre': this.new_genre, 'music_id': this.id})
          ///await updateMusicHarmonyQuantity({'music_id': this.id, 'new_harmony_quantity': this.ishs})
          ///this.radio10 = ''
          this.radio = 1
          this.isliupai = 1
          this.isable = true
          this.value = ''
          await createMarkedScore({
            'user_id': sessionStorage.getItem('user_id'),
            'music_id': this.id,
            'score': this.form.score
          }).then(response => {
            // console.log(response.data)
            this.$message({
              type: 'success',
              message: '提交成功!'
            });
          })
          ///
          await createDimensionScore({
            'user_id': sessionStorage.getItem('user_id'),
            'music_id': this.id,
            'dimension_score': this.form.score2,
            'dimension': this.dimension_type2
          }).then(response => {
            // console.log(response.data)
            this.$message({
              type: 'success',
              message: '提交成功!'
            });
          })
          ///

          await createDimensionScore({
            'user_id': sessionStorage.getItem('user_id'),
            'music_id': this.id,
            'dimension_score': this.form.score3,
            'dimension': this.dimension_type3
          }).then(response => {
            // console.log(response.data)
            this.$message({
              type: 'success',
              message: '提交成功!'
            });
          })
          ///

          await createDimensionScore({
            'user_id': sessionStorage.getItem('user_id'),
            'music_id': this.id,
            'dimension_score': this.form.score4,
            'dimension': this.dimension_type4
          }).then(response => {
            // console.log(response.data)
            this.$message({
              type: 'success',
              message: '提交成功!'
            });
          })
          ///

          await createDimensionScore({
            'user_id': sessionStorage.getItem('user_id'),
            'music_id': this.id,
            'dimension_score': this.form.score5,
            'dimension': this.dimension_type5
          }).then(response => {
            // console.log(response.data)
            this.$message({
              type: 'success',
              message: '提交成功!'
            });
          })
          ///
          
          this.form.score = ''
          this.form.score2 = ''
          this.form.score3 = ''
          this.form.score4 = ''
          this.form.score5 = ''
          this.ismark[this.index] = 1
          if (this.index === this.playedMusic.length) {
            // console.log("新歌")
            await getASongRandom({'user_id': sessionStorage.getItem('user_id')}).then(response => {
              if (response.data === "没有需要标注的歌曲") {
                this.sb = true
                this.$refs.audio.pause()
              } else {
                this.id = response.data.music_id
                this.name = response.data.music_name
                this.singer = response.data.singer
                this.genre = response.data.genre
                // console.log("1111111111111")
                this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav')
                // this.src = require(" "+response.data.src)
                this.$refs.audio.src = this.src;
                this.play = true;
                this.box.play();
                this.playedMusic.push({
                  'music_id': this.id,
                  'music_name': this.name,
                  'singer': this.singer,
                  'src': this.src,
                  'genre': this.genre
                })
                this.index++;
              }
            })
          } else {
            // console.log("旧歌")
            var music = this.playedMusic[this.index];
            // console.log(music)
            this.id = music.music_id;
            this.name = music.music_name;
            this.singer = music.singer;
            this.genre = music.genre;
            this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav')
            this.$refs.audio.src = this.src;
            this.play = true;
            this.box.play();
          }

        }
      }
    },
    onLoadedmetadata(res) {
      // console.log('loadedmetadata')
      // console.log(res)
      this.audio.waiting = false
      this.audio.maxTime = parseInt(res.target.duration)
    },
    changeCurrentTime(index) {
      this.$refs.audio.currentTime = parseInt(index / 100 * this.audio.maxTime)
    },
    onTimeupdate(res) {
      // console.log('timeupdate')
      // console.log(res)
      this.audio.currentTime = res.target.currentTime
      this.sliderTime = parseInt(this.audio.currentTime / this.audio.maxTime * 100)
    },

// 进度条格式化toolTip
    formatProcessToolTip(index = 0) {
      index = parseInt(this.audio.maxTime / 100 * index)
      return '进度条: ' + realFormatSecond(index)
    },
    changeVolumns() {
      // 静音切换
      if (this.sliderValVolumn > 0) {
        this.sliderValVolumn = 0;
      } else {
        this.sliderValVolumn = this.copySliderValVolumn;
      }
    },
    // 下一首
    musicNext1() {
      getASongRandom({'user_id': sessionStorage.getItem('user_id')}).then(response => {
        // console.log(user_id)
        if (response.data === "没有需要标注的歌曲") {
          this.sb = true
        } else {
          console.log(this.index)
          console.log(this.index)
          console.log(this.index)
          this.id = response.data.music_id
          this.name = response.data.music_name
          this.singer = response.data.singer
          this.genre = response.data.genre
          // console.log("1111111111111")
          this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav')
          // this.src = require(" "+response.data.src)
          this.$refs.audio.src = this.src;
          this.play = true;
          this.box.play();
          this.playedMusic.push({
            'music_id': this.id,
            'music_name': this.name,
            'singer': this.singer,
            'src': this.src,
            'genre': this.genre
          })
          this.index++;
        }
      })

      this.Visible = false
      this.ismark[this.index] = 0
    },

    musicNext() {
      this.ismark[0] = 1
      console.log(this.index)
      console.log(this.index)
      console.log(this.index)
      if (this.ismark[this.index] !== 1) {
        this.$message({
          type: 'false',
          message: '未提交整体分!'
        });
      } else {
        if (this.index === this.playedMusic.length) {
          // console.log("新歌")
          console.log(2323)
          console.log(this.index)
          console.log(this.playedMusic.length)
          console.log(this.index)
          console.log(this.playedMusic.length)
          getASongRandom({'user_id': sessionStorage.getItem('user_id')}).then(response => {
            if (response.data === "没有需要标注的歌曲") {
              this.sb = true
            } else {
              this.id = response.data.music_id
              this.name = response.data.music_name
              this.singer = response.data.singer
              this.genre = response.data.genre
              // console.log("1111111111111")
              this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav')
              // this.src = require(" "+response.data.src)
              this.$refs.audio.src = this.src;
              this.play = true;
              this.box.play();
              this.playedMusic.push({
                'music_id': this.id,
                'music_name': this.name,
                'singer': this.singer,
                'src': this.src,
                'genre': this.genre
              })
              this.index++;
            }
          })
        } else {
          // console.log("旧歌")
          this.index++
          var music = this.playedMusic[this.index];
          // console.log(music)
          this.id = music.music_id;
          this.name = music.music_name;
          this.singer = music.singer;
          this.genre = music.genre;
          this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav')
          this.$refs.audio.src = this.src;
          this.play = true;
          this.box.play();
        }
      }
    },
    //上一首
    musicPre() {
      // console.log('上一首')
      if (this.index === 0) {
        alert('没有上一首了')
      } else {
        this.index--;
        console.log(this.index)
        console.log(this.index)
        console.log(this.index)
        var music = this.playedMusic[this.index];
        console.log(music)
        this.id = music.music_id;
        this.name = music.music_name;
        this.singer = music.singer;
        this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav')
        this.$refs.audio.src = this.src;
        this.play = true;
        this.box.play();
      }

    },
    sbClose() {
      this.sb = false
    },
    musicPlay() {
      this.play = !this.play;
      console.log(this.play)
      if (this.play) {
        this.box.play();
      } else {
        this.box.pause();
      }
    },
    tableRowClassName({row, rowIndex}) {
      if (rowIndex === 0) {
        return 'warning-row';
      } else if (rowIndex === 1) {
        return 'warning-row';
      } else if (rowIndex === 2) {
        return 'warning-row';
      } else if (rowIndex === 3) {
        return 'success-row';
      } else if (rowIndex === 4) {
        return 'success-row';
      } else if (rowIndex === 5) {
        return 'success-row';
      } else if (rowIndex === 6) {
        return 'three-row';
      } else if (rowIndex === 7) {
        return 'three-row';
      }
      return '';
    },
    formatTooltip(val) {
      // 格式化毫秒数，由于组件提示为纯数字，所以这里需要将数字转化为我们所需要的的格式，string类型的。'03:45',
      const time = this.formatTime(val);
      return `${time.min}:${time.sec}`;
    },
    // 音量显示100%
    formatTooltipVolumn(val) {
      return val * 100 + "%";
    },
    spliderSelectVolumn() {
      this.box.volume = this.sliderValVolumn;
      // 备份音量
      this.copySliderValVolumn = this.sliderValVolumn;
    },
    updateTime() {
      const total = this.formatTime(this.box.duration);
      const current = this.formatTime(this.box.currentTime);
      this.duration = `${total.min}:${total.sec}`;
      this.currentTime = `${current.min}:${current.sec}`;
      // console.log(this.currentTime);
      // 值为xx.xxxxx 需要取整
      this.sliderVal = Math.floor(this.box.currentTime);
    },
    formatTime(time) {
      // 格式化毫秒，返回String型分秒对象
      if (!time) return {min: "00", sec: "00"};
      return {
        min: Math.floor(time / 60)
            .toString()
            .padStart(2, "0"),
        sec: Math.floor(time % 60)
            .toString()
            .padStart(2, "0"),
      };
    },
    closeAudioPlay() {
      this.isShowAudioPlayer = true;
    },
    spliderSelect() {
      // 滑块松动后触发。更新当前时长，
      // 时长发生变动会init里的方法进行更新数据
      this.box.currentTime = this.sliderVal;
    },

  },

}
</script>
<style>
>>> .el-dialog {
  display: flex;
  flex-direction: column;
  margin: 0 !important;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  /*height:600px;*/
  max-height: calc(100% - 200px);
  max-width: calc(100% - 30px);
}

>>> .el-dialog .el-dialog__body {
  flex: 1;
  overflow: auto;
}
</style>
<style lang="less" scoped>
.poppervulumn-class {
  min-width: 20px !important;
  padding: 12px 5px !important;
}

.login-container {
  width: 350px;
  border: 1px solid #eaeaea;
  margin: 180px auto;
  padding: 35px 35px 15px 35px;
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 0 25px #cac6c6;
  box-sizing: border-box;

  .login_title {
    text-align: center;
    margin-bottom: 40px;
    color: #505458;
  }

  .el-input {
    width: 198px;
  }
}
</style>
<style lang='scss'>
.poppervulumn-class {
  min-width: 20px !important;
  padding: 12px 5px !important;
}

.mydialog {
  top: 25%;
  left: 25%;
  height: 800px;
  width: 50%;
  //transform:translate(-50%,-50%);

}

//.el-dialog__body{
//  flex:1 !important;
//  overflow: auto !important;
//  background-color: #42b983 !important;
//}

.el-divider--horizontal {
  margin: 2vh 1vh;
  //background: 0 0;
  //border-top: 1px dashed #e8eaec;
  width: 70vh;
}

.audio-player {
  .audio-mock-player {
    position: center;
    width: 880px;
    padding: 50px;
    background: rgba(192, 192, 192, 0.8);
    border: 10px solid rgba(220, 220, 220, 1);
    border-radius: 80px;
    display: flex;
    align-items: center;

    .play-sty {
      margin: 0 16px;
      width: 52px;
      height: 52px;
    }

    .slider {
      display: inline-block;
      width: 460px;
      position: relative;
      top: 4px;
      margin-left: 10px;
    }

    .preicon {
      width: 32px;
      height: 32px;
    }

    .user {
      img {
        margin-right: 40px;
        width: 150px;
        height: 150px;
        border-radius: 50%;
      }
    }

    .closeicon {
      position: absolute;
      right: -10px;
      top: -10px;
      width: 20px;
      height: 20px;
    }

    .right-menu {
      margin-left: 40px;
      flex: 1;

      .bottom {
        display: flex;
        align-items: center;

        .progress {
          flex: 1;
        }

        .current {
          font-family: PingFangSC-Regular;
          font-size: 18px;
          color: #ffffff;
          text-align: left;
          font-weight: 400;
          margin-left: 12px;
        }

        .duration {
          opacity: 0.6;
          font-family: PingFangSC-Regular;
          font-size: 18px;
          color: #ffffff;
          text-align: left;
          font-weight: 400;
          margin-right: 16px;
        }

        .vulumn {
          position: relative;

          img {
            width: 18.5px;
            height: 15px;
          }

          .vulumn-progress {
            position: absolute;
            top: -73px;
            left: -12px;
          }
        }
      }

      .song-name {
        height: 25px;
        font-family: PingFangSC-Regular;
        font-size: 25px;
        color: #ffffff;
        text-align: left;
        font-weight: 400;
        margin-bottom: 15px;
      }
    }
  }
}
</style>
<style>
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}

.el-table .three-row {
  background: #EBF4FA;
}
</style>
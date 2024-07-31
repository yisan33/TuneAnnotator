<template>
  <div>
    <div class="audio-player" style="margin-top:0px; margin-left:100px">
      <!--      <button @click="musicPre">上一首</button>-->
      <!--      <button @click="musicNext">下一首</button>-->
      <!--      <span>歌曲名称：{{name}}</span>-->
      <br>
      <!--      <span>{{src}}</span>-->
      <audio ref="audio"
             @timeupdate="onTimeupdate"
             @loadedmetadata="onLoadedmetadata"
             controls="controls"
      >
        <source :src='require("@/assets/mp3/"+ name +".mp3")' type="audio/mp3">
      </audio>

      <div class="audio-mock-player" v-if="isShowAudioPlayer">
        <img :src="closeIcon" class="closeicon" @click="closeAudioPlay"/>
        <!-- 上一首 -->
        <img :src="leftIcon" class="preicon" @click="musicPre"/>
        <!-- "暂停" : "播放" -->
        <img @click="musicPlay" class="play-sty" :src="play ? plozeIcon : playIcon"/>
        <!-- 下一首 -->
        <!--            <img :src ="nextIcon" class="preicon" @click="musicPlay('next')" />-->
        <img :src="nextIcon" class="preicon" @click="musicNext()"/>

        <div class="right-menu" style="text-align: center;">
          <div class="song-name">{{ name }}
            <el-button @click="inputpd" type="primary" style="margin-left: 150px">提交片段</el-button>
          </div>
          <div class="song-name">{{ singer }}
            <el-button @click="start" type="primary">开始</el-button>
            <el-button @click="end" style="margin-left: 10px;" type="primary">结束
            </el-button>&nbsp;&nbsp;起始时间：{{ this.bb + ':' + this.cc }}&nbsp;结束时间：{{ this.dd + ':' + this.ee }}


          </div>

          <div class="bottom">
            <!--  播放进度条 -->

            <el-slider v-model="sliderTime" :format-tooltip="formatProcessToolTip" @change="changeCurrentTime"
                       class="slider">

            </el-slider>


            <span class="current">{{ audio.currentTime | formatSecond }}</span>
            <span class="duration">/{{ audio.maxTime | formatSecond }}</span>
            <div class="vulumn" @click="changeVolumns">
              <!-- <img :src="require('./asset/vulumn.png')" alt=""/> -->
              <!-- 有时候我们在对于一些hover定位元素，当离开时候就没了，这个时候可以使用ctrl+shift+c的快捷键来获取。 -->
              <el-popover
                  placement="top-start"
                  trigger="hover"
                  popper-class="poppervulumn-class"
              >
                <img
                    slot="reference"
                    :src="sliderValVolumn ? vulumnIcon : mutedIcon"
                    alt=""
                    style="width: 18.5px; height: 15px"
                />
              </el-popover>
            </div>
          </div>
        </div>
      </div>

      <el-form ref="form" label-width="70px" :inline="true" :model="form" :rules="rules"
               style="margin: 20px 120px">

        <h3>声音条件(人声表现)</h3>
        <!--        <el-radio-group v-model="radio" style="padding-left: 25px">-->
        <!--          <el-radio :label="3"  v-model="radio" value="颤音" >颤音</el-radio>-->
        <!--          <el-radio :label="6" value="2">高音</el-radio>-->
        <!--          <el-radio :label="9" value="3">延音</el-radio>-->
        <!--        </el-radio-group>-->
        <!--        <div style="margin-top: 5px" >-->
        <!--&lt;!&ndash;          <el-button @click="chanyin" type="primary">颤音</el-button>&ndash;&gt;-->
        <!--          &lt;!&ndash;          <el-button @click="end" style="margin-left: 15px;" type="primary">a音</el-button>&ndash;&gt;-->
        <!--          &lt;!&ndash;          <el-button @click="end" style="margin-left: 15px;" type="primary">b音</el-button>&ndash;&gt;-->
        <!--          &lt;!&ndash;          <el-button @click="end" style="margin-left: 15px;" type="primary">c音</el-button>&ndash;&gt;-->
        <!--          &lt;!&ndash;          <el-button @click="end" style="margin-left: 15px;" type="primary">d音</el-button>&ndash;&gt;-->
        <!--          <el-select v-model="value" placeholder="选择" style="padding-left: 20px" >-->
        <!--            <el-option-->
        <!--                v-for="item in options"-->
        <!--                :key="item.value"-->
        <!--                :label="item.label"-->
        <!--                :value="item.value" >-->
        <!--            </el-option>-->
        <!--          </el-select>-->
        <!--          <el-button @click="getSkillValue" type="primary">确认</el-button>-->
        <!--          起始时间：{{ this.bb + ':' +this.cc }}&nbsp;结束时间：{{this.dd + ':' +this.ee}}-->
        <!--        </div>-->
        <el-form ref="form" label-width="150px" style="margin-top: 10px" :inline="true" :model="form" :rules="crules">
          <el-form-item label="音量与音域" prop="dimension_score">
            <el-input v-model="clip1" style="width: 50px" size="mini"></el-input>
          </el-form-item>
          <el-form-item label="音色与辨识度" prop="dimension_score">
            <el-input v-model="clip2" style="width: 50px" size="mini"></el-input>
          </el-form-item>
          <el-form-item label="发音咬字" prop="dimension_score">
            <el-input v-model="clip3" style="width: 50px" size="mini"></el-input>
          </el-form-item>

        </el-form>

        <h3>声乐技术(技巧表现)</h3>
        <el-form ref="form" label-width="150px" style="margin-top: 10px" :inline="true" :model="form" :rules="crules">
          <el-form-item label="音准、节奏" prop="dimension_score">
            <el-input v-model="clip4" style="width: 50px" size="mini"></el-input>
          </el-form-item>
          <el-form-item label="常规技巧" prop="dimension_score">
            <el-input v-model="clip5" style="width: 50px" size="mini"></el-input>
          </el-form-item>
          <el-form-item label="个性化技巧" prop="dimension_score">
            <el-input v-model="clip6" style="width: 50px" size="mini"></el-input>
          </el-form-item>

        </el-form>

        <h3>情感表现</h3>
        <el-form ref="form" label-width="150px" style="margin-top: 10px" :inline="true" :model="form" :rules="crules">
          <el-form-item label="戏剧性" prop="dimension_score">
            <el-input v-model="clip7" style="width: 50px" size="mini"></el-input>
          </el-form-item>
          <el-form-item label="语气感" prop="dimension_score">
            <el-input v-model="clip8" style="width: 50px" size="mini"></el-input>
          </el-form-item>

        </el-form>


        <h3>综合分数</h3>
        <el-form ref="form" label-width="70px" style="margin-top: 10px" :inline="true" :model="form" :rules="rules">
          <el-form-item label="整体分" prop="score">
            <el-input v-model="form.score" placeholder="请输入分数"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button @click="submit" type="primary">提交</el-button>
          </el-form-item>
        </el-form>
      </el-form>
    </div>
  </div>
</template>

<script>

import APlayer from 'vue-aplayer'
import {getSongs, getASongRandom, createMarkedScore, createMarkedClip, createMarkedDimensionScore} from "@/api/api";
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
      radio: 'cy',
      radio1: 3,
      form: {
        score: '',
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
      // crules: {
      //   dimension_score: [
      //     {required: true, trigger: 'blur', message: '请输入维度分数'}
      //   ]
      // },
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
      ismark: 0,
      start_time: -1,
      end_time: -1,
      bb: '00',
      cc: '00',
      dd: '00',
      ee: '00',
      clip1: '',
      clip2: '',
      clip3: '',
      clip4: '',
      clip5: '',
      clip6: '',
      clip7: '',
      clip8: '',
      type1: '音量与音域',
      type2: '音色与辨识度',
      type3: '发音咬字',
      type4: '音准、节奏',
      type5: '常规技巧',
      type6: '个性化技巧',
      type7: '戏剧性',
      type8: '语气感',
      type: -1,
      test: 1,
      id: null,
      name: "请点击下一首开始评价歌曲",
      singer: "",
      index: -1, // 当前播放的音乐索引
      playedMusic: [],
      options: [{
        value: '颤音',
        label: '颤音'
      }, {
        value: '技巧2',
        label: '技巧2'
      }, {
        value: '技巧3',
        label: '技巧3'
      }, {
        value: '技巧4',
        label: '技巧4'
      }, {
        value: '技巧5',
        label: '技巧5'
      }],
      value: '',
      label: ''
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
    gettype() {

      // console.log(value);
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
    submit1() {
      this.type = '嗓音条件与音域'
      this.form.dimension_score = this.clip1
      console.log(this.type)
      console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
    },
    submit2() {
      this.type = '音色与辨识度'
      this.form.dimension_score = this.clip2
      this.newMarkedDimensionScore()
    },
    submit3() {
      this.type = this.type1
      this.form.dimension_score = this.clip1
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type2
      this.form.dimension_score = this.clip2
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type3
      this.form.dimension_score = this.clip3
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.$message({
        type: 'success',
        message: '提交成功!'
      });
    },
    submit4() {
      this.type = '音准节奏'
      this.form.dimension_score = this.clip4
      this.newMarkedDimensionScore()
    },
    submit5() {
      this.type = '技巧'
      this.form.dimension_score = this.clip5
      this.newMarkedDimensionScore()
    },
    submit6() {
      this.type = this.type4
      this.form.dimension_score = this.clip4
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type5
      this.form.dimension_score = this.clip5
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type6
      this.form.dimension_score = this.clip6
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.$message({
        type: 'success',
        message: '提交成功!'
      });
    },
    submit8() {
      this.type = this.type1
      this.form.dimension_score = this.clip1
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type2
      this.form.dimension_score = this.clip2
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type3
      this.form.dimension_score = this.clip3
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type4
      this.form.dimension_score = this.clip4
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type5
      this.form.dimension_score = this.clip5
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type6
      this.form.dimension_score = this.clip6
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type7
      this.form.dimension_score = this.clip7
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.type = this.type8
      this.form.dimension_score = this.clip8
      // console.log(this.type)
      // console.log(this.form.dimension_score)
      this.newMarkedDimensionScore()
      this.$message({
        type: 'success',
        message: '提交成功!'
      });
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
    submit() {
      if (this.form.score === '') {
        this.$message({
          type: 'false',
          message: '未输入分数!'
        });
      } else {
        this.type = this.type1
        this.form.dimension_score = this.clip1
        this.newMarkedDimensionScore()
        this.type = this.type2
        this.form.dimension_score = this.clip2
        this.newMarkedDimensionScore()
        this.type = this.type3
        this.form.dimension_score = this.clip3
        this.newMarkedDimensionScore()
        this.type = this.type4
        this.form.dimension_score = this.clip4
        this.newMarkedDimensionScore()
        this.type = this.type5
        this.form.dimension_score = this.clip5
        this.newMarkedDimensionScore()
        this.type = this.type6
        this.form.dimension_score = this.clip6
        this.newMarkedDimensionScore()
        this.type = this.type7
        this.form.dimension_score = this.clip7
        this.newMarkedDimensionScore()
        this.type = this.type8
        this.form.dimension_score = this.clip8
        this.newMarkedDimensionScore()
        createMarkedScore({
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
        this.ismark = 1
        this.form.score = ''
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
    musicNext() {
      // console.log("下一首")
      if (this.isone === 1) {
        this.index++;
        if (this.index === this.playedMusic.length) {
          // console.log("新歌")
          getASongRandom({'user_id': sessionStorage.getItem(user_id)}).then(response => {
            // console.log(response.data)
            this.id = response.data.music_id
            this.name = response.data.music_name
            this.singer = response.data.singer
            // console.log("1111111111111")
            this.src = require('@/assets/mp3/' + this.name + '.mp3')
            // this.src = require(" "+response.data.src)
            this.$refs.audio.src = this.src;
            this.play = false;
            this.playedMusic.push({
              'music_id': this.id,
              'music_name': this.name,
              'singer': this.singer,
              'src': this.src
            })
            // console.log(this.playedMusic)
            // console.log(this.index)
            // console.log(this.name)
          })
          this.isone = 0
          this.ismark = 0
        } else {
          // console.log("旧歌")
          var music = this.playedMusic[this.index];
          // console.log(music)
          this.id = music.music_id;
          this.name = music.music_name;
          this.singer = music.singer;
          this.src = require('@/assets/mp3/' + this.name + '.mp3')
          this.$refs.audio.src = this.src;
          this.play = false;
        }
      } else {
        if (this.ismark === 1) {
          this.index++;
          if (this.index === this.playedMusic.length) {
            // console.log("新歌")
            getASongRandom({'user_id': sessionStorage.getItem(user_id)}).then(response => {
              // console.log(response.data)
              this.id = response.data.music_id
              this.name = response.data.music_name
              this.singer = response.data.singer
              // console.log("1111111111111")
              this.src = require('@/assets/mp3/' + this.name + '.mp3')
              // this.src = require(" "+response.data.src)
              this.$refs.audio.src = this.src;
              this.play = false;
              this.playedMusic.push({
                'music_id': this.id,
                'music_name': this.name,
                'singer': this.singer,
                'src': this.src
              })
              // console.log(this.playedMusic)
              // console.log(this.index)
              // console.log(this.name)
            })
            this.isone = 0
            this.ismark = 0
          } else {
            // console.log("旧歌")
            var music = this.playedMusic[this.index];
            // console.log(music)
            this.id = music.music_id;
            this.name = music.music_name;
            this.singer = music.singer;
            this.src = require('@/assets/mp3/' + this.name + '.mp3')
            this.$refs.audio.src = this.src;
            this.play = false;
          }
        } else {
          this.$message({
            type: 'false',
            message: '未提交整体分!'
          });
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
        var music = this.playedMusic[this.index];
        console.log(music)
        this.id = music.music_id;
        this.name = music.music_name;
        this.singer = music.singer;
        this.src = require('@/assets/mp3/' + this.name + '.mp3')
        this.$refs.audio.src = this.src;
        this.play = false;
      }

    },
    musicPlay() {
      this.play = !this.play;
      if (this.play) {
        this.box.play();
      } else {
        this.box.pause();
      }
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

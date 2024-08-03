<template>
  <div>
    <!--<el-dialog-->
    <!--  title="修正技巧标注"-->
    <!--  :visible.sync="isAdjustDialogVisible"-->
    <!--  width="50%"-->
    <!--&gt;-->
    <!--  &lt;!&ndash; 音频播放器 &ndash;&gt;-->
    <!--  <div>-->
    <!--<div>开始时间: {{ adjustedRange[0] | formatSecond }}</div>-->
    <!--<div>结束时间: {{ adjustedRange[1] | formatSecond }}</div>-->
    <!-- <el-slider-->
    <!--  v-show="isSliderReady"-->
    <!--  v-model="adjustedRange"-->
    <!--  :min="adjustMin"-->
    <!--  :max="adjustMax"-->
    <!--  range>-->
    <!--</el-slider>-->
    <!--<div>开始时间: {{ adjustedRange[0] | formatSecond }}</div>-->
    <!--<div>结束时间: {{ adjustedRange[1] | formatSecond }}</div>-->
    <!--<div>直接显示 adjustedRange: {{ adjustedRange[0] }} - {{ adjustedRange[1] }}</div>-->
    <!--<div>过滤器处理后的时间: {{ adjustedRange[0] | formatSecond }} - {{ adjustedRange[1] | formatSecond }}</div>-->
    <!--  </div>-->
    <!--  <span slot="footer" class="dialog-footer">-->
    <!--    <el-button @click="isAdjustDialogVisible = false">取消</el-button>-->
    <!--    <el-button type="primary" @click="saveAdjustedRange">保存修改</el-button>-->
    <!--  </span>-->
    <!--</el-dialog>-->
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
        <el-col :span="24">
          <el-card class="box-card" style="margin-top: 2px;width: 100%">
            <span>歌曲：{{ name }}</span>&nbsp&nbsp<span>id：{{ id }}</span>&nbsp&nbsp<span>流派：{{ genre }}</span>
            <br>
            <div style="margin-top: 5px">
              <el-button @click="musicPre" type="primary">上一首</el-button>
              <el-button @click="musicPlay" type="primary">暂停/播放</el-button>
              <!--              <el-button @click="musicNext" type="primary">下一首</el-button>-->
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
            <!--<el-slider-->
            <!--  v-model="sliderTime"-->
            <!--  :format-tooltip="formatProcessToolTip"-->
            <!--  @change="changeCurrentTime"-->
            <!--  @mousedown="startDragging"-->
            <!--  @mouseup="stopDragging"-->
            <!--  class="slider" style="width: 100%;">-->
            <!--</el-slider>-->
            <div class="progress-bar" ref="progressBar">
              <el-slider
                  v-model="sliderTime"
                  :format-tooltip="formatProcessToolTip"
                  @change="changeCurrentTime"
                  class="slider" style="width: 100%;">
              </el-slider>
              <!-- 技巧开始和结束的红线 -->
              <div v-if="showRedLines" class="red-line"
                   :style="{left: startLinePosition}"
                   @mousedown="startDragging('start', $event)">
                <span class="time-text">{{ startLineTimeText }}</span>
              </div>
              <div v-if="showRedLines" class="red-line"
                   :style="{left: endLinePosition}"
                   @mousedown="startDragging('end', $event)">
                <span class="time-text">{{ endLineTimeText }}</span>
              </div>
            </div>
            <div class="technique-bar-container" v-for="technique in ['颤音', '滑音', '气泡音', '假声', '转音']"
                 :key="technique">
              <div class="technique-bar base-bar"></div>
              <div v-for="range in techniqueRanges" v-if="range.type === technique" :key="range.startPct"
                   class="technique-bar overlay-bar"
                   :style="{ left: range.startPct + '%', width: (range.endPct - range.startPct) + '%', backgroundColor: getTechniqueColor(technique) }"
                   @click="playAndMarkTechnique(range)">
                <el-tooltip class="item" effect="dark" :content="hengtiaoshijian(range)" placement="top">
                  <div style="width: 100%; height: 100%;"></div>
                </el-tooltip>
              </div>
            </div>
            <div style="margin-top: 1%">
              <span class="current">{{ audio.currentTime | formatSecond }}s</span>
              <span class="duration">/{{ audio.maxTime | formatSecond }}s</span>
              <el-button type="primary" size="small" @click="rewindOneSecond"
                         style="margin-left: 20%;width: 100px;height: 30px" class="dialog-box-center">后退1s
              </el-button>
              <el-button type="primary" size="small" @click="forwardOneSecond"
                         style="margin-left: 3%;width: 100px;height: 30px" class="dialog-box-center">前进1s
              </el-button>
              <el-button style="margin-left: 2%">播放速度</el-button>
              <el-select v-model="playbackSpeed" placeholder="请选择" style="width: 100px; margin-left: 10px;"
                         @change="changePlaybackSpeed">
                <el-option label="1x" value="1"></el-option>
                <el-option label="0.75x" value="0.75"></el-option>
                <el-option label="0.5x" value="0.5"></el-option>
                <el-option label="0.25x" value="0.25"></el-option>
              </el-select>
              <el-button type="primary" size="small" @click="updateTechnique" style="margin-left: 2%;">
                修改标注
              </el-button>
            </div>
          </el-card>
        </el-col>
      </div>
    </div>
    <div>
      <el-button type="primary" size="small" @click="chanyin"
                 style="margin-top: 4%;margin-left: 25%;width: 150px;height: 60px" class="technique-button 颤音"
                 :disabled="techniqueClicked && type !== '颤音'">颤音
      </el-button>
      <el-button type="primary" size="small" @click="huayin"
                 style="margin-top: 4%;margin-left: 6%;width: 150px;height: 60px" class="technique-button 滑音"
                 :disabled="techniqueClicked && type !== '滑音'">滑音
      </el-button>
      <el-button size="small" @click="remake" style="margin-top: 4%;margin-left: 10%;width: 150px;height: 60px"
                 class="technique-button dialog-box-center">重新标注
      </el-button>
      <el-button size="small" @click="mark()" style="margin-top: 4%;margin-left: 3%;width: 150px;height: 60px"
                 class="technique-button dialog-box-center" :disabled="techniqueClicked">查看已标注技巧
      </el-button>
      <br>
      <el-button type="primary" size="small" @click="qipaoyin"
                 style="margin-top: 5%;margin-left: 16%;width: 150px;height: 60px" class="technique-button 气泡音"
                 :disabled="techniqueClicked && type !== '气泡音'">气泡音
      </el-button>
      <el-button type="primary" size="small" @click="jiasheng"
                 style="margin-top: 5%;margin-left: 6%;width: 150px;height: 60px" class="technique-button 假声"
                 :disabled="techniqueClicked && type !== '假声'">假声
      </el-button>
      <el-button type="primary" size="small" @click="zhuanyin"
                 style="margin-top: 5%;margin-left: 6%;width: 150px;height: 60px" class="technique-button 转音"
                 :disabled="techniqueClicked && type !== '转音'">转音
      </el-button>
      <el-button size="small" @click="musicNext" style="margin-top: 5%;margin-left: 8%;width: 200px;height: 80px"
                 class="technique-button dialog-box-center" :disabled="techniqueClicked">下一首
      </el-button>
    </div>
    <el-dialog
        title="提示"
        :visible.sync="copy2Visible"
        width="50%"
        :before-close="listClose2">
      <el-table
          stripe
          height="65vh"
          :data="scoreclip"
          style="width: 100%"
      >
        <el-table-column
            prop="type"
            label="类型">
        </el-table-column>
        <el-table-column
            prop="start_time"
            label="开始时间">
        </el-table-column>
        <el-table-column
            prop="end_time"
            label="结束时间">
        </el-table-column>
        <el-table-column>
          <template slot-scope="scope">
            <!--            <el-button size="mini" @click="clipEdit(scope.row)">编辑</el-button>-->
            <el-button type="danger" size="mini" @click="clipDelete(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
  </div>
</template>
<script>

import APlayer from 'vue-aplayer'
import {
  getSongs,
  getASongRandom,
  createMarkedClip, getUserClips, deleteAMarkedClip, getAClipSongRandom, updateAMarkedClip,
} from "@/api/api";
import {user_id} from "@/store/getters";

function realFormatSecond(second) {
  console.log("Input second: ", second);
  var secondType = typeof second;
  if (secondType === 'number' || secondType === 'string') {
    second = parseFloat(second);

    var hours = Math.floor(second / 3600);
    second = second - hours * 3600;
    var minutes = Math.floor(second / 60);
    var sec = second % 60; // 获取秒数，包括小数

    // 格式化时间，保留小数点后三位
    return hours + ':' + ('0' + minutes).slice(-2) + ':' + sec.toFixed(3);
  } else {
    return '0:00:00.000';
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
      ismark: [],
      form: {
        score: '',
        clip_score: '',
        dimension_score: ''
      },
      // startTime: '',
      // endTime: '',
      toggleStartEnd: true,
      techniqueClicked: false,
      audioSource: '', // 歌曲的源文件路径
      editStartTime: 0, // 修正技巧的起始时间
      editEndTime: 0, // 修正技巧的结束时间
      startLinePosition: '0%',
      endLinePosition: '0%',
      audio: {
        currentTime: 0,
        maxTime: 0,
        playing: false,
        muted: false,
        speed: 1,
        // waiting: true,
        preload: 'auto'
      },
      scoreclip: [],
      clipData: {
        user_id: 0,
        music_id: 0,
      },
      techniqueMarkers: [],
      sliderTime: 0,
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

      playbackSpeed: 1,
      isDragging: false, //
      bb: '00',
      cc: '00',
      dd: '00',
      ee: '00',
      dragStartX: 0,
      isAdjustDialogVisible: false,
      adjustMin: 0,
      adjustMax: 0,
      adjustedRange: [0, 0],
      currentTechnique: null, // 当前选中的技巧片段
      showRedLines: false,
      draggingLine: null,
      audioClipStart: 0, // 技巧片段的开始时间
      audioClipEnd: 0, // 技巧片段的结束时间
      copy2Visible: false,
      currentClipId: null,
      ishs: '',
      isable: true,
      isliupai: 1,
      new_genre: "",
      genre: "",
      type: 'none',
      test: 1,
      sb: false,
      id: "",
      name: "点击下一首开始评价",
      singer: "",
      index: 0, // 当前播放的音乐索引
      playedMusic: [],
      value: '',
      label: '',
      isSliderReady: false, // 控制 el-slider 渲染的标志
    }
  },
  computed: {
    techniqueRanges() {
      if (!this.audio.maxTime) return [];

      return this.techniqueMarkers.map(marker => {
        return {
          type: marker.type,
          startPct: (marker.start_time / this.audio.maxTime) * 100,
          endPct: (marker.end_time / this.audio.maxTime) * 100,
          startTime: marker.start_time,
          endTime: marker.end_time,
          clipId: marker.clip_id // 确保包含 clip_id
        };
      });
    },
    startLinePosition() {
      // 计算开始红线的位置
      return this.calculateLinePosition(this.currentTechnique.startTime);
    },
    endLinePosition() {
      // 计算结束红线的位置
      return this.calculateLinePosition(this.currentTechnique.endTime);
    },
    startLineTimeText() {
      return this.formatTimeText(this.currentTechnique.startTime);
    },
    endLineTimeText() {
      return this.formatTimeText(this.currentTechnique.endTime);
    },
  },


  watch: {
    // 监听 adjustedRange 的变化
    adjustedRange(newValue) {
      if (newValue && Array.isArray(newValue) && newValue.length === 2) {
        console.log('Adjusted Range Updated:', newValue);
      } else {
        console.error('Invalid adjustedRange:', newValue);
      }
    },

    // 当主页面的 currentTime 改变时，更新弹窗中的进度条
    'audio.currentTime'(newValue) {
      // 仅在弹窗可见时进行同步
      if (this.isAdjustDialogVisible) {
        this.adjustedRange = [newValue, this.adjustedRange[1]];
      }
    }
  },


  mounted() {
    // this.getMusic()
    this.init();
    this.getAudioDuration()
    window.addEventListener('keydown', this.handleSpacebar);
  },
  // beforeDestroy() {
  //   // Remove keydown event listener
  //   window.removeEventListener('keydown', this.handleSpacebar);
  // },
  filters: {
    // 使用组件过滤器来动态改变按钮的显示
    // transPlayPause(value) {
    //   return value ? '暂停' : '播放'
    // },
    // 将整数转化成时分秒
    formatSecond(second = 0) {
      console.log("过滤器接收到的时间:", second);
      second = parseFloat(second);
      var wholeSeconds = Math.floor(second); // 获取整数秒
      var milliseconds = (second % 1).toFixed(3).substring(2); // 获取毫秒，保留三位小数
      return `${wholeSeconds.toString().padStart(2, '0')}.${milliseconds}`;
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
    openAdjustDialog() {
      if (this.currentClipId) {
        this.showAdjustDialog(this.currentClipId); // 假设您有一个方法来处理显示对话框
      } else {
        this.$message({
          type: 'warning',
          message: '请选择技巧片段'
        });
      }
    },
    getTechniqueColor(technique) {
      switch (technique) {
        case '颤音':
          return 'RoyalBlue';
        case '滑音':
          return 'DarkCyan';
        case '气泡音':
          return 'Violet';
        case '假声':
          return 'DarkGoldenrod';
        case '转音':
          return 'Indigo';
          // Add other cases as needed
        default:
          return 'white';
      }
    },

    addTechniqueMarker(newMarker) {
      this.techniqueMarkers.push(newMarker);
    },
    playTechnique(startTime, endTime) {
      // 设置音频播放器的当前时间为技巧的起始时间
      this.box.currentTime = startTime;
      // 开始播放
      this.box.play();

      const checkTime = () => {
        // 当前时间接近或超过结束时间时暂停播放
        if (this.box.currentTime >= endTime) {
          this.box.pause();
        } else {
          // 继续检查
          requestAnimationFrame(checkTime);
        }
      };

      // 开始检查
      checkTime();
    },
    formatTimeText(time) {
      if (!time && time !== 0) return '0.000';
      return time.toFixed(3);
    },
    // Method to delete a technique marker
    deleteTechniqueMarker(clipId) {
      this.techniqueMarkers = this.techniqueMarkers.filter(marker => marker.clip_id !== clipId);
    },

    // Example method to handle deletion from a UI action
    handleDelete(clipId) {
      // Call your API to delete the technique
      deleteAMarkedClip(clipId).then(() => {
        // On successful deletion, update the local state
        this.deleteTechniqueMarker(clipId);
      }).catch(error => {
        console.error('Error deleting technique:', error);
      });
    },


    showAdjustDialog(clipId) {
      const technique = this.techniqueMarkers.find(t => t.clip_id === clipId);
      if (!technique) {
        console.error("找不到对应的技巧标记");
        return;
      }
      console.log("技巧片段数据:", technique);
      // 设置当前技巧片段的歌手和歌曲名，以及开始和结束时间
      this.currentTechnique = {
        id: clipId,
        singer: this.singer,
        name: this.name,
        start_time: technique.start_time,
        end_time: technique.end_time
      };

      const startTime = isFinite(technique.start_time) ? technique.start_time : 0;
      const endTime = isFinite(technique.end_time) ? technique.end_time : 5;
      console.log("转换后的开始时间:", startTime, "转换后的结束时间:", endTime); // 调试信息
      // 使用经过验证的 startTime 和 endTime 初始化 adjustedRange
      this.isSliderReady = true; // 当一切准备就绪后，设置为 true 以渲染 slider
      this.$nextTick(() => {
        this.adjustedRange = [
          Math.max(0, startTime - 1), // 开始时间前1秒
          Math.min(this.audio.maxTime, endTime + 1) // 结束时间后1秒
        ];
      });
      console.log("wcy", this.adjustedRange)
      this.isAdjustDialogVisible = true;

    },

    saveAdjustedRange() {
      // 获取更新的时间范围
      const updatedStartTime = this.adjustedRange[0];
      const updatedEndTime = this.adjustedRange[1];

      // 创建请求体
      const requestBody = {
        clip_id: this.currentClipId,
        new_start_time: updatedStartTime,
        new_end_time: updatedEndTime
      };

      // 调用 API 方法进行更新
      updateAMarkedClip(requestBody)
          .then(response => {
            // 成功处理
            this.$message({
              type: 'success',
              message: '技巧标注已更新!'
            });
            this.isAdjustDialogVisible = false;

            // 找到并更新对应的技巧标记
            const index = this.techniqueMarkers.findIndex(marker => marker.clip_id === this.currentClipId);
            if (index !== -1) {
              this.techniqueMarkers[index].start_time = updatedStartTime;
              this.techniqueMarkers[index].end_time = updatedEndTime;
              // 重新计算百分比位置
              this.techniqueMarkers[index].startPct = (updatedStartTime / this.audio.maxTime) * 100;
              this.techniqueMarkers[index].endPct = (updatedEndTime / this.audio.maxTime) * 100;
            }

            // 如果需要，触发横条技巧显示的更新
            this.refreshTechniqueDisplay();
          })
          .catch(error => {
            // 错误处理
            console.error('更新失败:', error);
            this.$message({
              type: 'error',
              message: '更新失败!'
            });
          });
    },

    refreshTechniqueDisplay() {
      // 此方法中可以包含重新计算和渲染横条技巧显示的逻辑
      // 这可能包括强制组件重新渲染或调用特定的更新方法
    },


    mark() {
      this.clipData.music_id = this.id
      this.clipData.user_id = sessionStorage.getItem('user_id');
      getUserClips(this.clipData).then(response => {
        this.scoreclip = response.data
        console.log(this.scoreclip)

        console.log("Technique Markers:", this.techniqueMarkers);
        // console.log(response.data)
      })
      this.copy2Visible = true
    },
    listClose2() {
      // this.$refs.form.resetFields()
      this.copy2Visible = false
    },
    rewindOneSecond() {
      if (this.box.currentTime > 1) {
        this.box.currentTime -= 1;
      } else {
        this.box.currentTime = 0;
      }
    },

    forwardOneSecond() {
      if (this.box.currentTime < this.box.duration - 1) {
        this.box.currentTime += 1;
      } else {
        this.box.currentTime = this.box.duration;
      }
    },
    // When a new song is loaded
    loadNewSong(newSong) {
      this.audio.maxTime = newSong.duration;
      this.techniqueMarkers = []; // Clear old markers
      // ... Load the new song ...
    },

    clipDelete(clip_id) {
      this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteAMarkedClip(clip_id).then(response => {
          if (response.status === 200) {
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
            // 删除后更新技巧标记数组
            this.fetchAndUpdateTechniqueMarkers();
            if (this.currentTechnique && this.currentTechnique.id === clip_id) {
              this.currentTechnique = null;
              this.showRedLines = false;
            }
          }
        }).catch(error => {
          console.error('Error deleting technique:', error);
          this.$message({
            type: 'error',
            message: '删除失败!'
          });
        });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });

    },

    fetchAndUpdateTechniqueMarkers() {
      getUserClips(this.clipData).then(response => {
        this.scoreclip = response.data;
        this.techniqueMarkers = this.scoreclip.map(clip => ({
          type: clip.type,
          clip_id: clip.clip_id,
          start_time: clip.start_time,
          end_time: clip.end_time
        }));
        console.log("Updated techniqueMarkers:", this.techniqueMarkers);
      }).catch(error => {
        console.error('Error fetching technique markers:', error);
      });
    },
    changePlaybackSpeed() {
      this.box.playbackRate = this.playbackSpeed;
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
      if (!this.techniqueClicked) {
        this.type = '颤音';
        console.log(this.type);
        this.start();
        this.techniqueClicked = true;
      } else {
        this.end();
        this.techniqueClicked = false;
      }
    },
    huayin() {
      if (!this.techniqueClicked) {
        this.type = '滑音';
        console.log(this.type);
        this.start();
        this.techniqueClicked = true;
      } else {
        this.end();
        this.techniqueClicked = false;
      }
    },
    jiasheng() {
      if (!this.techniqueClicked) {
        this.type = '假声';
        console.log(this.type);
        this.start();
        this.techniqueClicked = true;
      } else {
        this.end();
        this.techniqueClicked = false;
      }
    },
    zhuanyin() {
      if (!this.techniqueClicked) {
        this.type = '转音';
        console.log(this.type);
        this.start();
        this.techniqueClicked = true;
      } else {
        this.end();
        this.techniqueClicked = false;
      }
    },
    qipaoyin() {
      if (!this.techniqueClicked) {
        this.type = '气泡音';
        // console.log(this.type);
        this.start();
        this.techniqueClicked = true;
      } else {
        this.end();
        this.techniqueClicked = false;
      }
    },
    start() {
      if (!this.techniqueClicked) {
        let aa = Math.floor(this.audio.currentTime);
        this.bb = Math.floor(aa / 60);
        this.cc = Math.floor(aa % 60);
        this.start_time = this.audio.currentTime;
        if (this.bb >= 0 && this.bb < 10) {
          this.bb = '0' + this.bb;
        }
        if (this.cc >= 0 && this.cc < 10) {
          this.cc = '0' + this.cc;
        }
        console.log("start");
        console.log(this.bb + ':' + this.cc);
        console.log(this.start_time);
        this.techniqueClicked = true;
      } else {
        this.end();
      }
    },
// 更新“修改标注”按钮的事件处理函数
    updateTechnique() {
      if (!this.currentClipId) {
        this.$message({
          type: 'warning',
          message: '请选择技巧片段'
        });
        return;
      }

      // 从 currentTechnique 获取更新后的时间
      const updatedStartTime = this.currentTechnique.startTime;
      const updatedEndTime = this.currentTechnique.endTime;

      // 检查时间范围是否有效
      if (updatedStartTime >= updatedEndTime) {
        this.$message({
          type: 'error',
          message: '错误: 技巧片段的起始时间必须小于结束时间'
        });
        return; // 阻止进一步操作
      }

      // 创建请求体
      const requestBody = {
        clip_id: this.currentClipId,
        new_start_time: updatedStartTime,
        new_end_time: updatedEndTime
      };

      // 调用 API 更新技巧标注
      updateAMarkedClip(requestBody).then(response => {
        // 处理成功的响应
        this.$message({
          type: 'success',
          message: '技巧标注已更新!'
        });

        // 更新本地技巧标记
        const index = this.techniqueMarkers.findIndex(marker => marker.clip_id === this.currentClipId);
        if (index !== -1) {
          this.techniqueMarkers[index].start_time = updatedStartTime;
          this.techniqueMarkers[index].end_time = updatedEndTime;
          this.techniqueMarkers[index].startPct = (updatedStartTime / this.audio.maxTime) * 100;
          this.techniqueMarkers[index].endPct = (updatedEndTime / this.audio.maxTime) * 100;
        }
      }).catch(error => {
        // 处理错误
        console.error('更新失败:', error);
        this.$message({
          type: 'error',
          message: '更新失败!'
        });
      });
    },


    end() {
      let ff = Math.floor(this.audio.currentTime);
      this.dd = Math.floor(ff / 60);
      this.ee = Math.floor(ff % 60);
      this.end_time = this.audio.currentTime;

      if (this.dd >= 0 && this.dd < 10) {
        this.dd = '0' + this.dd;
      }
      if (this.ee >= 0 && this.ee < 10) {
        this.ee = '0' + this.ee;
      }

      // 检查时间范围是否有效
      if (this.start_time >= this.end_time) {
        this.$message({
          type: 'error',
          message: '错误: 技巧片段的起始时间必须小于结束时间'
        });
        return; // 阻止进一步操作
      }

      // 创建新标记
      const formattedStartTime = realFormatSecond(this.start_time);
      const formattedEndTime = realFormatSecond(this.end_time);
      const newMarker = {
        type: this.type,
        start_time: this.start_time,
        end_time: this.end_time,
        formattedStartTime: formattedStartTime,
        formattedEndTime: formattedEndTime,
        startPct: (this.start_time / this.audio.maxTime) * 100,
        endPct: (this.end_time / this.audio.maxTime) * 100,
      };

      console.log("New marker: ", newMarker); // 调试信息
      this.techniqueMarkers.push(newMarker);

      // 提交新标记到后端
      createMarkedClip({
        'user_id': sessionStorage.getItem('user_id'),
        'music_id': this.id,
        'start_time': this.start_time,
        'end_time': this.end_time,
        'type': this.type
      }).then(response => {
        this.start_time = -1;
        this.end_time = -1;
        this.type = 'none';
        this.$message({
          type: 'success',
          message: '提交成功!'
        });
        // 更新技巧标记
        this.getclip();
      });

      // 重置技巧点击状态
      this.techniqueClicked = false;
    },


    remake() {
      // 重置起始和结束时间
      this.start_time = -1;
      this.end_time = -1;
      this.type = 'none'

      // 重置时间显示
      this.bb = '00';
      this.cc = '00';
      this.dd = '00';
      this.ee = '00';

      // 解除技巧按钮的禁用状态
      this.techniqueClicked = false;
      console.log(this.start_time)
      // 可以在这里添加任何其他需要重置的状态
    },
    onLoadedmetadata(res) {
      // console.log('loadedmetadata')
      // console.log(res)
      this.audio.waiting = false
      this.audio.maxTime = parseInt(res.target.duration)
    },
    changeCurrentTime(index) {
      const newTime = (index / 100) * this.audio.maxTime;
      this.$refs.audio.currentTime = newTime;
    },
    onTimeupdate(res) {
      if (!this.isDragging) {
        this.audio.currentTime = res.target.currentTime;
        this.sliderTime = parseInt(this.audio.currentTime / this.audio.maxTime * 100);
      }
    },

    formatProcessToolTip(index = 0) {
      // 计算当前进度条对应的精确时间（秒），保持小数点后三位
      const timeInSeconds = (this.audio.maxTime / 100 * index).toFixed(3);

      // 返回格式化的时间字符串
      return `进度条: ${timeInSeconds} 秒`;
    },

    hengtiaoshijian(range) {
      const startTime = range.startTime.toFixed(3);
      const endTime = range.endTime.toFixed(3);
      return `时间范围: ${startTime} - ${endTime} 秒`;
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
      getAClipSongRandom({'user_id': sessionStorage.getItem('user_id')}).then(response => {
        if (response.data === "本次标注结束") {
          this.sb = true;
          this.box.pause();
        } else {
          // 设置歌曲信息
          this.id = response.data.music_id;
          this.name = response.data.music_name;
          this.singer = response.data.singer;
          this.genre = response.data.genre;
          this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav');
          this.$refs.audio.src = this.src;
          this.play = true;
          this.box.play();
          this.playedMusic.push({
            'music_id': this.id,
            'music_name': this.name,
            'singer': this.singer,
            'src': this.src,
            'genre': this.genre
          });
          this.index++;

          // 重置播放速度
          this.playbackSpeed = 1;
          this.changePlaybackSpeed();

          // 加载已标注的技巧片段
          this.getTechniqueMarkersForSong(this.id); // 新添加的代码行
        }
      });

      this.Visible = false;
      this.ismark[this.index] = 0;
    },

    async musicNext() {
      // 重置技巧标记
      this.resetTechniqueState();

      // 检查是否需要加载新歌
      if (this.index === this.playedMusic.length) {
        try {
          // 等待异步操作完成
          let response = await getAClipSongRandom({'user_id': sessionStorage.getItem('user_id')});
          if (response.data === "本次标注结束") {
            this.sb = true;
          } else {
            this.loadSongData(response.data);
            this.index++;
          }
        } catch (error) {
          console.error('Error fetching new song:', error);
        }
      } else {
        // 加载已有歌曲
        this.loadSongFromPlayedMusic(this.index);
        this.index++;
      }

      // 更新播放速度
      this.playbackSpeed = 1;
      this.changePlaybackSpeed();
    },


    loadSongData(songData) {
      this.id = songData.music_id;
      this.name = songData.music_name;
      this.singer = songData.singer;
      this.genre = songData.genre;
      this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav');
      this.$refs.audio.src = this.src;
      this.play = true;
      this.box.play();
      this.playedMusic.push(songData);

      // 获取新歌曲的技巧标记
      this.getTechniqueMarkersForSong(this.id);
    },

    loadSongFromPlayedMusic(index) {
      let music = this.playedMusic[index];
      this.id = music.music_id;
      this.name = music.music_name;
      this.singer = music.singer;
      this.genre = music.genre;
      this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav');
      this.$refs.audio.src = this.src;
      this.play = true;
      this.box.play();

      // 异步获取旧歌曲的技巧标记
      this.getTechniqueMarkersForSong(this.id).then(() => {
        // 这里可以添加一些在技巧标记加载完成后的逻辑
      }).catch(error => {
        console.error('Error loading technique markers for previous song:', error);
      });
    },

    resetTechniqueState() {
      this.techniqueMarkers = [];
      this.currentTechnique = null;
      this.showRedLines = false;
    },

    //上一首
    musicPre() {
      // 检查是否有上一首歌
      if (this.index === 0) {
        alert('没有上一首了');
      } else {
        this.index--;
        this.loadSongFromPlayedMusic(this.index);
      }
    },

    async getTechniqueMarkersForSong(musicId) {
      try {
        let response = await getUserClips({music_id: musicId, user_id: sessionStorage.getItem('user_id')});
        this.techniqueMarkers = response.data.map(clip => ({
          type: clip.type,
          clip_id: clip.clip_id,
          start_time: clip.start_time,
          end_time: clip.end_time,
          startPct: (clip.start_time / this.audio.maxTime) * 100,
          endPct: (clip.end_time / this.audio.maxTime) * 100
        }));
        this.showRedLines = false;
        this.currentTechnique = null;
      } catch (error) {
        console.error('Error fetching technique markers:', error);
      }
    },
    sbClose() {
      this.sb = false
    },
    jumpToTechnique(startTime, endTime, clipId) {
      console.log('Clip ID:', clipId);
      // 设置音频播放器的当前时间为技巧的起始时间

      // 开始播放
      this.box.play();
      this.box.currentTime = startTime;
      // 在技巧的结束时间暂停播放
      const checkEndTime = () => {
        if (this.box.currentTime >= endTime) {
          this.box.pause();
          // 以下代码用于处理暂停后的操作，例如弹出对话框等
          // this.showAdjustDialog(clipId);
        } else {
          requestAnimationFrame(checkEndTime); // 继续检查
        }
      };

      checkEndTime();
      console.log('Playing technique from', startTime, 'to', endTime);

      // 记录当前技巧的 clipId，用于后续的“修改标注”操作
      console.log(clipId)
      this.currentTechnique = {
        id: clipId,
        startTime: startTime,
        endTime: endTime
      };
      this.currentClipId = clipId;
    },

    startDragging(lineType, event) {
      // 防止默认事件和事件冒泡
      event.preventDefault();

      // 设置当前拖动的线类型和初始鼠标位置
      this.draggingLine = lineType;
      this.dragStartX = event.clientX;

      // 添加鼠标移动和鼠标放开的事件监听器
      document.addEventListener('mousemove', this.dragging);
      document.addEventListener('mouseup', this.stopDragging);
    },
    dragging(event) {
      if (!this.draggingLine) return;

      // 计算鼠标移动的距离
      const dx = event.clientX - this.dragStartX;
      // 更新鼠标开始位置
      this.dragStartX = event.clientX;

      // 根据拖动的线更新技巧时间
      if (this.draggingLine === 'start') {
        // 计算新的开始时间
        let newStartTime = this.updateTimeByDrag(this.currentTechnique.startTime, dx);
        // 确保开始时间不超过结束时间
        newStartTime = Math.min(newStartTime, this.currentTechnique.endTime);
        this.currentTechnique.startTime = newStartTime;
        // 更新红线的位置
        this.startLinePosition = this.calculateLinePosition(newStartTime);
      } else if (this.draggingLine === 'end') {
        // 计算新的结束时间
        let newEndTime = this.updateTimeByDrag(this.currentTechnique.endTime, dx);
        // 确保结束时间不小于开始时间
        newEndTime = Math.max(newEndTime, this.currentTechnique.startTime);
        this.currentTechnique.endTime = newEndTime;
        // 更新红线的位置
        this.endLinePosition = this.calculateLinePosition(newEndTime);
      }
    },


    stopDragging() {
      // 停止拖动，移除事件监听器
      this.draggingLine = null;
      document.removeEventListener('mousemove', this.dragging);
      document.removeEventListener('mouseup', this.stopDragging);
      this.updateTechniqueDisplay(this.currentTechnique.id, this.currentTechnique.startTime, this.currentTechnique.endTime);
    },
    updateTimeByDrag(time, dx) {
      // 确保 progressBar 已经被渲染且可访问
      if (!this.$refs.progressBar) {
        console.error("Progress bar not found");
        return time; // 或者返回一个合理的默认值
      }

      const progressBarWidth = this.$refs.progressBar.offsetWidth;

      // 根据拖动距离和进度条的宽度计算新的时间
      let newTime = time + (dx / progressBarWidth) * this.audio.maxTime;

      // 保证新的时间值在有效范围内
      newTime = Math.max(0, Math.min(newTime, this.audio.maxTime));

      return newTime;
    },


    getclip() {
      this.clipData.music_id = this.id;
      this.clipData.user_id = sessionStorage.getItem('user_id');
      getUserClips(this.clipData).then(response => {
        this.scoreclip = response.data;
        console.log(this.scoreclip);
        this.techniqueMarkers = this.scoreclip.map(clip => ({
          type: clip.type,
          clip_id: clip.clip_id,
          start_time: clip.start_time,
          end_time: clip.end_time,
        }));
        console.log("Updated techniqueMarkers:", this.techniqueMarkers);
      });
    },
    handleSpacebar(event) {
      console.log('Key pressed:', event.code);
      if (event.code === 'Space') {
        event.preventDefault(); // Prevent the default action to avoid scrolling
        console.log('Spacebar pressed, toggling play/pause');
        this.musicPlay(); // Toggle play/pause
      }
    },

    musicPlay() {
      this.play = !this.play;
      console.log(this.play)
      if (this.play) {
        this.box.play();
      } else {
        this.box.pause();
      }
      console.log('Play status:', this.play); // Debugging log
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
    playAndMarkTechnique(range) {
      // 当当前技巧未被设置或者当前横条技巧与正在播放的技巧不同时，更新当前技巧
      if (!this.currentTechnique || this.currentTechnique.clipId !== range.clipId) {
        this.showRedLines = true;
        this.startLinePosition = range.startPct + '%';
        this.endLinePosition = range.endPct + '%';
        this.currentTechnique = Object.assign({}, range);
        this.currentClipId = range.clipId;
      }

      // 播放当前技巧的音频段落
      this.playTechnique(this.currentTechnique.startTime, this.currentTechnique.endTime);
    },


    calculateLinePosition(time) {
      // 将时间转换为百分比位置
      const positionPct = (time / this.audio.maxTime) * 100;
      return positionPct + '%';
    },
    updateTechniqueDisplay(clipId, newStartTime, newEndTime) {
      // 查找并更新对应的技巧标记
      const index = this.techniqueMarkers.findIndex(marker => marker.clip_id === clipId);
      if (index !== -1) {
        this.techniqueMarkers[index].start_time = newStartTime;
        this.techniqueMarkers[index].end_time = newEndTime;
        // 重新计算百分比位置
        this.techniqueMarkers[index].startPct = (newStartTime / this.audio.maxTime) * 100;
        this.techniqueMarkers[index].endPct = (newEndTime / this.audio.maxTime) * 100;
      }
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

<style scoped>
/* Example CSS for responsive buttons */
.button-responsive {
  width: 10vw; /* width as a percentage of the viewport width */
  height: 5vw; /* height as a percentage of the viewport width */
  min-width: 50px; /* minimum width to ensure usability */
  min-height: 25px; /* minimum height to ensure usability */
  font-size: 1.5vw; /* font size scales with viewport width */
  padding: 1vw; /* padding scales with viewport width */
  margin: 1vw; /* margin scales with viewport width */
}

/* Adjustments for smaller screens to prevent buttons from becoming too small */
@media (max-width: 600px) {
  .button-responsive {
    width: 20vw;
    height: 10vw;
    font-size: 3vw;
  }
}
</style>
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

.technique-bars {
  position: relative;
  height: 5px;
  margin-top: 5px;
}

.technique-button {
  border: 2px solid #ADD8E6; /* 默认浅蓝色边框 */
  margin: 5px; /* 保持按钮间距 */
  border-radius: 5px; /* 轻微的圆角 */
  color: black; /* 文字颜色 */
  font-weight: bold; /* 字体加粗 */
}

.technique-button:disabled {
  opacity: 0.5; /* 使颜色变暗 */
  cursor: not-allowed; /* 更改鼠标指针样式 */
}

/* 特定技巧类型的按钮颜色 */
.technique-button.颤音 {
  background-color: RoyalBlue;
  color: white;
}

.technique-button.滑音 {
  background-color: DarkCyan;
  color: white;
}

.technique-button.气泡音 {
  background-color: Violet;
  color: white;
}

/* 文字颜色改为黑色以提高可读性 */
.technique-button.假声 {
  background-color: DarkGoldenrod;
  color: white;
}

.technique-button.转音 {
  background-color: Indigo;
  color: white;
}

.technique-button.颤音:disabled {
  background-color: #6699CC;
}

/* 淡化颜色 */
.technique-button.滑音:disabled {
  background-color: #669999;
}

.technique-button.气泡音:disabled {
  background-color: #CC99CC;
}

.technique-button.假声:disabled {
  background-color: #CC9966;
}

.technique-button.转音:disabled {
  background-color: #666699;
}

.technique-bar {
  position: absolute;
  height: 100%;
  bottom: 0;
}

.overlay-bar {
  position: absolute;
  height: 100%;
  bottom: 0;
}

.technique-bar-container {
  position: relative;
  height: 10px;
  margin-top: 10px;
  margin-bottom: 15px;
}

.base-bar {
  background-color: lightgrey;
  width: 100%;
  height: 100%;
}

.technique-bar.颤音 {
  background-color: RoyalBlue;
}

.technique-bar.滑音 {
  background-color: DarkCyan;
}

.technique-bar.气泡音 {
  background-color: Violet;
}

.technique-bar.假声 {
  background-color: DarkGoldenrod;
}

// ... styles for other techniques

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

.time-text {
  position: absolute;
  bottom: 100%; /* 将文本放置在红线的上方 */
  left: 50%;
  transform: translateX(-50%);
  background-color: #fff;
  padding: 2px 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
  font-size: 12px;
  white-space: nowrap;
}

.red-line {
  position: absolute;
  bottom: 0;
  width: 2px;
  height: 100%;
  background-color: red;
  cursor: pointer;
}

.progress-bar {
  position: relative;
  /* 其他样式 */
}

//.el-dialog__body{
//  flex:1 !important;
//  overflow: auto !important;
//  background-color: #42b983 !important;
//}
//.technique-button {
//    border: 2px solid #ADD8E6; /* 浅蓝色边框 */
//    margin: 5px; /* 保持按钮间距 */
//    border-radius: 5px; /* 轻微的圆角 */
//}
.el-divider--horizontal {
  margin: 2vh 1vh;
  //background: 0 0;
  //border-top: 1px dashed #e8eaec;
  width: 70vh;
}

.dashed-divider {
  border-right: 2px dashed #ccc; /* 设置虚线的颜色和样式 */
  height: 100%; /* 设置虚线的高度，根据需要调整 */
  margin-right: 10px; /* 设置虚线与右侧按钮的间距 */
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
      width: 100%;
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
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
        <el-button size="small" @click="musicNext1" center width="50%"
                   style="margin-top: -30px;margin-left: 40%;width: 150px;height: 50px" class="highlight-button btn-9">开始评价
        </el-button>
        <br><br><br><br>
      </el-dialog>

      <el-dialog
          class="mydialog"
          :before-close="sbClose">
        <el-button type="primary" size="small" center width="50%"
                   style="margin-top: -30px;margin-left: 40%;width: 150px;height: 50px" class="dialog-box-center">标注结束
        </el-button>
      </el-dialog>


    </div>
    <div class="audio-player" style="margin-top:10px; margin-left:10px">
      <div style="margin-top: 20px">
        <el-col :span="10">
          <el-card class="box-card" style="margin-top: 2px;width: 95%">
            <span style="font-size: 18px; color: #026b9f;">
              进度：{{ marked_count }} / {{ marked_count + unmarked_count }}
            </span>&nbsp&nbsp
            <span style="margin-left: 12px; font-size: 18px; color: #026b9f;">
              歌曲：{{ name }}
            </span>&nbsp&nbsp
            <!-- <span style="margin-left: 10px; font-size: 18px; color: #026b9f;"> -->
            <!--   歌手：{{ singer }} -->
            <!-- </span>&nbsp&nbsp -->
            <span style="margin-left: 12px; font-size: 18px; color: #026b9f;" >情感：{{ genre }}
            </span>
            
            <div>
              <el-button @click="musicPre_v2"  class="highlight-button btn-9" style="margin-top: 30px;">上一首</el-button>
              <el-button @click="musicPlay"  class="highlight-button btn-9b" style="margin-top: 30px; margin-left: 30px;">暂停/播放</el-button>
              <el-button @click="musicNext" class="highlight-button btn-9" style="margin-top: 30px; margin-left: 30px;">下一首</el-button>
            </div>
  
            <div style="margin-top: 20px">
              <audio ref="audio"
                     @timeupdate="onTimeupdate"
                     @loadedmetadata="onLoadedmetadata"
                     @seeking="onSeeking"
                     @seeked="onSeeked"
                     controls="controls"
                     style="width: 500px; height: 30px; border-radius: 5px; margin-top: 10px"
              >
                <source :src='require("@/assets/mp3/" + singer + "-" + name + "_(Vocals)" + ".wav")' type="audio/wav">
              </audio>
            </div>
            <div style="margin-top: 1vh">
            </div>
          </el-card>

          <el-card class="box-card" style="margin-top: 20px;width: 95%" v-show="hasPlayedOnce">
            <span style="font-size: 18px; color: #026b9f;">------------------------人声轨--------------------------</span>
            
            <div>
              <el-button class="highlight-button-b btn-9c" style="margin-top: 30px;">上一首</el-button>
              <el-button @click="musicPlay_vocal"  class="highlight-button btn-9b" style="margin-top: 30px; margin-left: 30px;">暂停/播放</el-button>
              <el-button class="highlight-button-b btn-9c" style="margin-top: 30px; margin-left: 30px;">下一首</el-button>
            </div>
  
            <div style="margin-top: 20px">
              <audio ref="audio_vocal"
                     @timeupdate="onTimeupdate_vacal"
                     @loadedmetadata="onLoadedmetadata_vocal"
                     controls="controls"
                     style="width: 500px; height: 30px; border-radius: 5px; margin-top: 10px"
              >
                <source :src='require("@/assets/mp3/" + singer + "-" + name + "_(Vocals)" + ".wav")' type="audio/wav">
              </audio>
            </div>
            
            <div style="margin-top: 1vh">


            </div>
          </el-card>

          <el-card class="box-card" style="margin-top: 20px;width: 95%" v-show="hasPlayedOnce">
            <span style="font-size: 18px; color: #026b9f;">------------------------伴奏轨--------------------------</span>            <br>
            <div style="margin-top: 5px">
              <el-button class="highlight-button-b btn-9c" style="margin-top: 30px;">上一首</el-button>
              <el-button @click="musicPlay_instrumental"  class="highlight-button btn-9b" style="margin-top: 30px; margin-left: 30px;">暂停/播放</el-button>
              <el-button class="highlight-button-b btn-9c" style="margin-top: 30px; margin-left: 30px;">下一首</el-button>
            </div>
  
            <div style="margin-top: 20px">
              <!--      <span>{{src}}</span>-->
              <audio ref="audio_instrumental"
                     @timeupdate="onTimeupdate_instrumental"
                     @loadedmetadata="onLoadedmetadata_instrumental"
                     controls="controls"
                     style="width: 500px; height: 30px; border-radius: 5px; margin-top: 10px"
              >
                /// <source :src='require("@/assets/mp3/" + singer + "-" + name + "_(Vocals)" + ".wav")' type="audio/wav">
              </audio>
            </div>
            <div style="margin-top: 1vh"></div>
          </el-card>
          

          
        </el-col>
      </div>
      <el-col :span="14">
        <el-card class="box-card-a" style="margin-left:40px; width: 800px !important; height: 700px;">
          <div class="demo1-video" style="margin-left: 30px;  width: 900px;height: 710px">

            <el-form ref="form" label-width="70px" :inline="true" :model="form" :rules="rules"
                     style="margin: 5px 10px">

              <!-- /// <h3>整体质量</h3>-->
              <el-form ref="form" label-width="70px" style="margin-top: 20px;" :inline="true"
                       :model="form"
                       :rules="rules">
                
                
                <div class="form-container">
                  <el-tooltip placement="left" effect="customized">
                    <div slot="content" style="font-size: 15px; width: 800px; max-width: 300px;">
                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;一首歌曲带给人的整体感受，营造的整体氛围，具有的艺术表现力以及可听性。

                      <br/><br/>打分细则：
                      <br/><br/>90-100分：
                      带给人的整体听感极好，营造的整体氛围以及艺术表现力极强，使听者愿意反复聆听并分享给他人；（技术完善，无瑕疵，有感染力）
                      <br/><br/>80-89分：
                      带给人的整体听感较好，营造的整体氛围以及艺术表现力较强，使听者愿意反复聆听；（技术完善，无瑕疵；85以上需要有一定的独特性）
                      <br/><br/>70-79分： 
                      带给人的整体听感一般，营造的整体氛围以及艺术表现力一般，可听可不听；(有瑕疵70~74；无瑕疵但不动听75~79)
                      <br/><br/>60-69分：
                      带给人的整体听感较差，缺乏整体氛围以及艺术表现力，不想再听；（缺陷比较多）
                      <br/><br/>59分以下： 
                      带给人的整体听感很差，音乐不知所云，不能忍受；（乱弹琴没法听）
                    </div>
                    <el-button class="highlight-button button-5">整体评价</el-button>

                  </el-tooltip>
                  <div class="form-control">
                    <input 
                      type="text" 
                      v-model="form.score" 
                      :aria-valid="isScoreValid1"
                      placeholder="请输入分数" 
                      @input="validateScore1" 
                      required
                    />
                  </div>
                  
                </div>
                
              </el-form>
              
              <!-- /// <h3>演唱</h3>-->
              <el-form ref="form" label-width="70px" style="margin-top: 50px;" :inline="true"
                       :model="form"
                       :rules="rules">
                
                <div class="form-container">
                  <el-tooltip placement="left" effect="customized">
                    <div slot="content" style="font-size: 15px; width: 800px; max-width: 300px;">
                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;演唱是歌手通过对声音的运用，将歌曲中蕴含的内容及情感生动地传达给听众。评价演唱的主要子维度为人声表现和技巧表现。
                      <br/>
                     （1）人声表现：旨在考察演唱者在一首歌曲中所展现出来的先天声音条件，这被认为是演唱表现的最基础条件。
                      声乐研究者广泛认为演唱者的先天条件在一定程度上决定了其演唱的上限。
                      <br/>（2）技巧表现：旨在考察演唱者在经过声乐技能训练后所展现出来的各种演唱技巧。
                      这些技巧的训练可以提高演唱者对声音的美化以及对歌曲的驾驭能力，使许多先天嗓音不理想的演唱者能够通过这一维度的加强，实现演唱水平的大幅提升。

                      <br/><br/>打分细则：
                      <br/><br/>90-100分：表现完美，音色悦耳具有辨识度，技巧发挥成熟自然，有感染力；<br/><br/>80-89分：
                      表现良好，音色悦耳，技巧发挥成熟自然；
                      <br/><br/>70-79分： 个别音音准、节奏把握不准确，气息稳定，共鸣较好，但部分技巧使用发挥不够成熟；<br/><br/>60-69分：
                      个别乐句音准、节奏把握不准确，气息不够稳定，共鸣一般，整体技巧运用不成熟；
                      <br/><br/>59分以下： 有1/3以上的音准、节奏问题，气息不稳定，共鸣很少，声乐技巧运用较差，大白嗓严重
                      
                    </div>
                  <el-button class="highlight-button button-5">演唱</el-button>
                  </el-tooltip>
                  
                  <div class="form-control">
                    <input 
                      type="text" 
                      v-model="form.score2" 
                      :aria-valid="isScoreValid2"
                      :disabled="!isInputUnlocked"
                      placeholder="请输入分数" 
                      @input="validateScore2" 
                      required
                    />
                  </div>
                  
                </div>
                
              </el-form>
              
              <!-- /// <h3>旋律</h3>-->
              <el-form ref="form" label-width="70px" style="margin-top: 50px;" :inline="true"
                       :model="form"
                       :rules="rules">
                
                <div class="form-container">
                  
                  <el-tooltip placement="left" effect="customized">
                    <div slot="content" style="font-size: 15px; width: 800px; max-width: 300px;">
                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;旋律是音乐的主要线索，它可以反映音乐结构，表达音乐情感，传达音乐主题。评价一个旋律的主要子维度暂定为：流畅性、易记性及独特性。
                      <br/>（1） 流畅性：具有流畅性的旋律通常呈波浪形的曲线，级进多于跳进，声区间连接顺畅，没有过多的装饰音，旋律通常保持在原调及其关系调内，较少使用不协和音程；
                      <br/>（2）易记性：旨在考察旋律是否具有明显的记忆点；
                      <br/>（3）独特性：旨在考察旋律是否在设计上有一些独到之处，能够区别于其他歌曲的旋律； 

                      <br/><br/>打分细则：
                      <br/><br/>90-100分：
                      旋律流畅，极具美感，具有较强的易记性或独特性，有感染力；《虚幻与现实》《梦里什么都有》
                      <br/><br/>80-89分：
                      旋律流畅，具有美感，具有一定的易记性或独特性；《我们的时光》
                      <br/><br/>70-79分： 
                      旋律流畅，略有美感，易记性较差，不具有独特性；
                      <br/><br/>60-69分：
                      有一定流畅性，不具有美感，不具有易记性和独特性，所听即所得；
                      <br/><br/>59分以下： 
                      缺乏流畅性，缺乏美感，不具有易记性和独特性，所听即所得；如《阻止你哭泣》《我想找对象》
                    </div>
                  <el-button class="highlight-button button-5">旋律</el-button>
                  </el-tooltip>
                  <div class="form-control">
                    <input 
                      type="text" 
                      v-model="form.score3" 
                      :aria-valid="isScoreValid3"
                      :disabled="!isInputUnlocked" 
                      placeholder="请输入分数" 
                      @input="validateScore3" 
                      required
                    />
                  </div>
                  
                </div>

              </el-form>
                
              
              <!-- /// <h3>编曲</h3> -->
              <el-form ref="form" label-width="70px" style="margin-top: 50px;" :inline="true"
                       :model="form"
                       :rules="rules">
                
                <div class="form-container">
                  <el-tooltip placement="left" effect="customized">
                    <div slot="content" style="font-size: 15px; width: 800px; max-width: 300px;">
                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;编曲是指对音乐作品中各种乐器、声音元素和音符进行有序安排和组合的过程。编曲的质量取决于其能否巧妙地运用不同乐器与声音元素，以创造出丰富、平衡、富有表现力与层次感的音乐体验。评价编曲的子维度暂定为：层次感、平衡性、创新性。
                      <br/>（1）协调性：旨在考察和声与旋律是否搭配协调；各乐器是否搭配合理，不会相互掩盖或失衡； 
                      <br/>（2）层次感：旨在考察编曲是否巧妙地运用不同声音元素，给音乐不同阶段带来一定的深度和动态变化，避免单调； 
                      <br/>（3）创新性：旨在考察和声是否能够避免套路性的进行，具有新颖独特性，能给歌曲带来新鲜感和惊喜；配器是否运用不常见的乐器与音色搭配；

                      <br/><br/>打分细则：
                      <br/><br/>90-100分：
                      协调性很好，具有层次感，有较强创新性，有感染力；《虚幻与现实》《浓缩蓝鲸》
                      <br/><br/>80-89分：
                      协调性较好，具有层次感，有一定创新性；《黑白色》《冷玻璃》
                      <br/><br/>70-79分：
                      满足基本协调性，略有层次感，不具有创新性；《月老掉线》《爱如火》
                      <br/><br/>60-69分：
                      满足基本协调性，单调，不具有层次感，不具有创新性；《倒霉的一天》《姑娘别哭泣》
                      <br/><br/>59分以下：
                      不协调，缺乏层次感，缺乏创新性
                    </div>
                  <el-button class="highlight-button button-5">编曲</el-button>
                  </el-tooltip>
                  <div class="form-control">
                    <input 
                      type="text" 
                      v-model="form.score4" 
                      :aria-valid="isScoreValid4"
                      :disabled="!isInputUnlocked" 
                      placeholder="请输入分数" 
                      @input="validateScore4" 
                      required
                    />
                  </div>
                  
                </div>
              </el-form>
              
              <!-- /// <h3>音频质量</h3> -->
              <el-form ref="form" label-width="70px" style="margin-top: 50px;" :inline="true"
                       :model="form"
                       :rules="rules">
                
                <div class="form-container">
                  <el-tooltip placement="left" effect="customized">
                    <div slot="content" style="font-size: 15px; width: 800px; max-width: 300px;">
                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;音频质量维度涉及到音乐作品的录音和混音质量。本研究将评估音频质量的子维度暂定为：清晰度、立体感、动态范围。
                      <br/>（1）清晰度：旨在考察声音是否干净、明亮，是否能清楚听到音频元素；
                      <br/>（2）立体感：旨在考察音频是否具有良好的空间感，是否有层次，左右声道的定位是否合理；
                      <br/>（3）动态范围：旨在考察音频的动态是否丰富，是否保留了声音的起伏，而没有过度压缩；

                      <br/><br/>打分细则：
                      <br/><br/>90-100分：
                      清晰度很好，具有丰富的立体感，动态范围适度；《女儿国》
                      <br/><br/>80-89分：
                      清晰度较好，具有一定立体感，动态范围适度；
                      <br/><br/>70-79分：
                      满足基本清晰度，立体感较差，动态范围较为适度；
                      <br/><br/>60-69分：
                      满足基本清晰度，立体感差，动态范围不适度；《姑娘别哭泣》
                      <br/><br/>59分以下：
                      清晰度差，立体感差，没有动态范围；《我想找对象》
                    </div>
                  <el-button class="highlight-button button-5">音频质量</el-button>
                  </el-tooltip>
                  <div class="form-control">
                    <input 
                      type="text" 
                      v-model="form.score5" 
                      :aria-valid="isScoreValid5"
                      :disabled="!isInputUnlocked" 
                      placeholder="请输入分数" 
                      @input="validateScore5" 
                      required
                    />
                  </div>
                  
                </div>
              </el-form>
              
              <!-- 
              <el-button class="highlight-button button-5" style="width: 25%; margin-top: 50px">情感标签是否正确</el-button>
              
              &nbsp&nbsp&nbsp
              &nbsp&nbsp&nbsp
              <el-radio-group v-model="radio" @input="dayin11" class="custom-radio-group" style="padding-left: 25px;">
                <el-radio :label="1">是</el-radio>
                <el-radio :label="0">否</el-radio>
              </el-radio-group>
              &nbsp&nbsp&nbsp&nbsp&nbsp

              <el-select v-model="value" @change="dylog" :disabled="isable" placeholder="请选择" size="mini" class="custom-select">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                    class="custom-option">
                </el-option>
              </el-select>
              <br>
              -->
              

              
              <br>
              <el-button class="highlight-button btn-13" style="margin-left: 25vh" @click="submit">提交</el-button>
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
  createDimensionScore,
  findSongofVocalVersion,
  findSongofInstrumentalVersion,
  createMusicEmotion
} from "@/api/api";
import {user_id} from "@/store/getters";
import CustomInput from './CustomInput.vue';


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

  components: {
    CustomInput
  },
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
      
      radio11: '',
      ismark: [],
      isScoreValid1: 'false',
      isScoreValid2: 'false',
      isScoreValid3: 'false',
      isScoreValid4: 'false',
      isScoreValid5: 'false',
      form: {
        score: '',
        score2: '', ///
        score3: '', ///
        score4: '', ///
        score5: '', ///
        
        clip_score: '',
        dimension_score: ''
      },

      isInputUnlocked: false, /// 输入框初始是锁定的
      hasPlayedOnce: false,   /// 标记歌曲是否播放完一遍
      lastValidTime: 0,        /// 保存上一次的有效播放时间，用于阻止拖动进度条
      hasShownWarning: false, /// 用于控制弹窗提示只出现一次
      hasShownPlayCompleted: false,

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

      audio_vocal: {
        currentTime: 0,
        maxTime: 0,
        playing: false,
        muted: false,
        speed: 1,
        // waiting: true,
        preload: 'auto'
      }, ///

      audio_instrumental: {
        currentTime: 0,
        maxTime: 0,
        playing: false,
        muted: false,
        speed: 1,
        // waiting: true,
        preload: 'auto'
      }, ///

      sliderTime: 0,
      sliderTime_vocal: 0, ///
      sliderTime_instrumental: 0, ///
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
      box_vocal: undefined, ///
      box_instrumental: undefined, ///

      play: false, // 播放状态，true为正在播放
      play_vocal: false, ///
      play_instrumental: false, ///

      sliderValVolumn: 0.5, // 音量
      copySliderValVolumn: 0.5,
      isone: 1,
      start_time: -1,
      end_time: -1,
      bb: '00',
      cc: '00',
      dd: '00',
      ee: '00',
      
      clip10: '',
      
      type10: '加权平均分',

      dimension_type: '维度1',///
      dimension_type2: '演唱',///
      dimension_type3: '旋律',///
      dimension_type4: '编曲',///
      dimension_type5: '音频质量',///

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
      ///
      marked_count: "",
      unmarked_count: "",
      ///
      index: 0, // 当前播放的音乐索引
      playedMusic: [],
      playedMusic_vocal: [], ///
      playedMusic_instrumental: [], ///
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

      this.box_vocal = this.$refs["audio_vocal"];
      this.box_instrumental = this.$refs["audio_instrumental"];

      // this.box.src = require(`${this.list[this.index].src}`);
      this.box.src = require(`${this.src}`);
      this.box_vocal.src_vocal = require(`${this.src_vocal}`); ///
      this.box_instrumental.src_instrumental = require(`${this.src_instrumental}`); ///
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

      this.box_vocal.onTimeupdate_vacal = function () {
        console.log("播放位置发送了变动");
        that.updateTime();
      }; ///

      this.box_instrumental.onTimeupdate_instrumental = function () {
        console.log("播放位置发送了变动");
        that.updateTime();
      }; ///


      // 音频播放完毕
      this.box.onended = function () {
        console.log("播放完毕，谢谢收听");
      };
      // 音频播放完毕
      this.box.onerror = function () {
        console.log("加载出错！");
      };
    },
    validateScore1() {
      const ScoreValue1 = this.form.score;
      if (/^(?:[1-9]?[0-9]|100)$/.test(ScoreValue1)) {
        this.isScoreValid1 = 'true';
      } else {
        this.isScoreValid1 = 'false';
      }
    },
    validateScore2() {
      const ScoreValue2 = this.form.score2;
      if (/^(?:[1-9]?[0-9]|100)$/.test(ScoreValue2)) {
        this.isScoreValid2 = 'true';
      } else {
        this.isScoreValid2 = 'false';
      }
    },
    validateScore3() {
      const ScoreValue3 = this.form.score3;
      if (/^(?:[1-9]?[0-9]|100)$/.test(ScoreValue3)) {
        this.isScoreValid3 = 'true';
      } else {
        this.isScoreValid3 = 'false';
      }
    },
    validateScore4() {
      const ScoreValue4 = this.form.score4;
      if (/^(?:[1-9]?[0-9]|100)$/.test(ScoreValue4)) {
        this.isScoreValid4 = 'true';
      } else {
        this.isScoreValid4 = 'false';
      }
    },
    validateScore5() {
      const ScoreValue5 = this.form.score5;
      if (/^(?:[1-9]?[0-9]|100)$/.test(ScoreValue5)) {
        this.isScoreValid5 = 'true';
      } else {
        this.isScoreValid5 = 'false';
      }
    },

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
        if (this.form.score > 100 || this.form.score < 0 ||
          this.form.score2 > 100 || this.form.score2 < 0 ||
          this.form.score3 > 100 || this.form.score3 < 0 ||
          this.form.score4 > 100 || this.form.score4 < 0 ||
          this.form.score5 > 100 || this.form.score5 < 0) {
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
          
          if (this.isliupai === 1) {
            this.new_genre = this.genre
          }
          ///await updateMusicGenre({'new_genre': this.new_genre, 'music_id': this.id})
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
            // this.$message({
              // type: 'success',
              // message: '提交成功!'
            // });
          })
          ///

          await createDimensionScore({
            'user_id': sessionStorage.getItem('user_id'),
            'music_id': this.id,
            'dimension_score': this.form.score3,
            'dimension': this.dimension_type3
          }).then(response => {
            // console.log(response.data)
            // this.$message({
              // type: 'success',
              // message: '提交成功!'
            // });
          })
          ///

          await createDimensionScore({
            'user_id': sessionStorage.getItem('user_id'),
            'music_id': this.id,
            'dimension_score': this.form.score4,
            'dimension': this.dimension_type4
          }).then(response => {
            // console.log(response.data)
            // this.$message({
              // type: 'success',
              // message: '提交成功!'
            // });
          })
          ///

          await createDimensionScore({
            'user_id': sessionStorage.getItem('user_id'),
            'music_id': this.id,
            'dimension_score': this.form.score5,
            'dimension': this.dimension_type5
          }).then(response => {
            // console.log(response.data)
            // this.$message({
              // type: 'success',
              // message: '提交成功!'
            // });
          })

          await createMusicEmotion({
            'user_id': sessionStorage.getItem('user_id'),
            'music_id': this.id,
            'emotion': this.new_genre
          }).then(response => {
            // console.log(response.data)
            // this.$message({
              // type: 'success',
              // message: '提交成功!'
            // });
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
                this.$router.push({ name: 'EndPage' })
              } else {
                this.id = response.data.music_id
                this.name = response.data.music_name
                this.singer = response.data.singer
                this.genre = response.data.genre
                ///
                this.marked_count = response.data.marked_count
                this.unmarked_count = response.data.unmarked_count

                // console.log("1111111111111")
                this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '.mp3')
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

                findSongofVocalVersion({'song_name': this.name, 'singer_name': this.singer}).then(response => {

                  this.src_vocal = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav')
                  console.log(this.src_vocal) ///
                  this.$refs.audio_vocal.src = this.src_vocal;
                  this.play_vocal = false;
                  this.playedMusic_vocal.push({
                    'music_id': this.id,
                    'music_name': this.name,
                    'singer': this.singer,
                    'src': this.src_vocal,
                    'genre': this.genre
                  })
                  
                });

                findSongofInstrumentalVersion({'song_name': this.name, 'singer_name': this.singer}).then(response => {

                  this.src_instrumental = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Instrumental)' + '.wav')
                  console.log(this.src_instrumental) ///
                  this.$refs.audio_instrumental.src = this.src_instrumental;
                  this.play_instrumental = false;
                  this.playedMusic_instrumental.push({
                    'music_id': this.id,
                    'music_name': this.name,
                    'singer': this.singer,
                    'src': this.src_instrumental,
                    'genre': this.genre
                  })
                  
                });

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
      this.isScoreValid1 = 'false';
      this.isScoreValid2 = 'false';
      this.isScoreValid3 = 'false';
      this.isScoreValid4 = 'false';
      this.isScoreValid5 = 'false';

      this.hasPlayedOnce = false;
      this.isInputUnlocked = false;
      
    },
    onLoadedmetadata(res) {
      // console.log('loadedmetadata')
      // console.log(res)
      this.audio.waiting = false
      this.audio.maxTime = parseInt(res.target.duration)
    },

    onLoadedmetadata_vocal(res) {
      // console.log('loadedmetadata')
      // console.log(res)
      this.audio_vocal.waiting = false
      this.audio_vocal.maxTime = parseInt(res.target.duration)
    }, ///

    onLoadedmetadata_instrumental(res) {
      // console.log('loadedmetadata')
      // console.log(res)
      this.audio_instrumental.waiting = false
      this.audio_instrumental.maxTime = parseInt(res.target.duration)
    }, ///

    changeCurrentTime(index) {
      this.$refs.audio.currentTime = parseInt(index / 100 * this.audio.maxTime)
    },
    onTimeupdate(res) {
      // console.log('timeupdate')
      // console.log(res)
      this.audio.currentTime = res.target.currentTime
      this.sliderTime = parseInt(this.audio.currentTime / this.audio.maxTime * 100)  

      ///新增对于进度条的控制,只有听完第一遍才能解锁输入框、拖动进度条
      if (this.audio.currentTime >= this.audio.maxTime) {// 检查歌曲是否播放到结尾
        this.isInputUnlocked = true;
        this.hasPlayedOnce = true;
        if (!this.hasShownPlayCompleted) {
          this.$message({
          type: 'success',
          message: '维度标注功能已解锁',
          duration: 5000
        });
        }
        this.hasShownPlayCompleted = true;        
      }
      ///
    },

    onTimeupdate_vacal(res) {
      // console.log('timeupdate')
      // console.log(res)
      this.audio_vocal.currentTime = res.target.currentTime
      this.sliderTime_vocal = parseInt(this.audio_vocal.currentTime / this.audio_vocal.maxTime * 100)
    },

    onTimeupdate_instrumental(res) {
      // console.log('timeupdate')
      // console.log(res)
      this.audio_instrumental.currentTime = res.target.currentTime
      this.sliderTime_instrumental = parseInt(this.audio_instrumental.currentTime / this.audio_instrumental.maxTime * 100)
    },

    ///新增对于进度条的控制,只有听完第一遍才能解锁输入框、拖动进度条
    onSeeking() {
      const audio = this.$refs.audio;
      const tempTime = this.lastValidTime
      // 如果还没有播放完一次，则阻止拖动
      if (!this.hasPlayedOnce) {
        // audio.play()
        if (!this.hasShownWarning) {
          this.$message({
          type: 'warning',
          message: '请先完整听完一遍'
        });
        this.hasShownWarning = true; // 显示提示后立即设置标志
        }
      }
    },
    onSeeked() {
      const audio = this.$refs.audio;
      // 如果还没有播放完一次，再次阻止用户确认拖动的位置
      if (!this.hasPlayedOnce) {
        // audio.currentTime = 0; // 恢复到之前的位置
        audio.load(); // 直接重新播放
        audio.play();
        this.hasShownWarning = false;
      }
    },
    ///

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
          this.$router.push({ name: 'EndPage' })
        } else {
          ///
          
          console.log(this.index)
          console.log(this.index)
          console.log(this.index)
          this.id = response.data.music_id
          this.name = response.data.music_name
          this.singer = response.data.singer
          this.genre = response.data.genre
          ///
          this.marked_count = response.data.marked_count
          this.unmarked_count = response.data.unmarked_count

          // console.log("1111111111111")
          console.log(this.name, this.id, this.genre) ///
          console.log(response.data.src) ///
          this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '.mp3')
          console.log(this.src) ///
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

          findSongofVocalVersion({'song_name': this.name, 'singer_name': this.singer}).then(response => {

            this.src_vocal = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav')
            console.log(this.src_vocal) ///
            this.$refs.audio_vocal.src = this.src_vocal;
            this.play_vocal = false;
            this.playedMusic_vocal.push({
              'music_id': this.id,
              'music_name': this.name,
              'singer': this.singer,
              'src': this.src_vocal,
              'genre': this.genre
            })
            
          });

          findSongofInstrumentalVersion({'song_name': this.name, 'singer_name': this.singer}).then(response => {

            this.src_instrumental = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Instrumental)' + '.wav')
            console.log(this.src_instrumental) ///
            this.$refs.audio_instrumental.src = this.src_instrumental;
            this.play_instrumental = false;
            this.playedMusic_instrumental.push({
              'music_id': this.id,
              'music_name': this.name,
              'singer': this.singer,
              'src': this.src_instrumental,
              'genre': this.genre
            })
            
          });
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

    musicPre_v2() {
      this.$message({
          type: 'warning',
          message: '上一首已标注，无法返回'
        });
    },

    musicPre() {
      // console.log('上一首')
      if (this.index === 0) {
        this.$message({
          type: 'warning',
          message: '没有上一首了'
        });
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

    musicPlay_vocal() {
      this.play_vocal = !this.play_vocal;
      console.log(this.play_vocal)
      if (this.play_vocal) {
        this.box_vocal.play();
      } else {
        this.box_vocal.pause();
      }
    }, ///
    
    musicPlay_instrumental() {
      this.play_instrumental = !this.play_instrumental;
      console.log(this.play_instrumental)
      if (this.play_instrumental) {
        this.box_instrumental.play();
      } else {
        this.box_instrumental.pause();
      }
    }, ///

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

///
<style>
.el-form {
  line-height: 60px; /* 根据需要调整行高 */
}
</style>
///

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

.mydialog .el-dialog {
  border-radius: 10px;
  background-color: #f0f4f7; /* 更改为对话框内容区域的背景颜色 */
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

///
<style scoped>
.highlight-button {
  font-size: 20px; /* 字体大小 */
  font-weight: bold; /* 字体加粗 */
  padding: 10px 20px; /* 内边距 */
  border: 2px solid #2c6fdb; /* 边框颜色 */
  transition: all 0.3s ease; /* 动画效果 */
  background-color: #ffffff; /* 背景颜色 */
  color: #2c6fdb; /* 字体颜色 */
}

.highlight-button:hover {
  border-color: #1a4d9b; /* 悬停时边框颜色 */
  color: #1a4d9b; /* 悬停时字体颜色 */
  background-color: #f0f0f0; /* 悬停时背景颜色 */
  transform: scale(1.17); /* 悬停时放大效果 */
}
</style>
///

<style>
.highlight-button-b {
  font-size: 20px; /* 字体大小 */
  font-weight: bold; /* 字体加粗 */
  padding: 10px 20px; /* 内边距 */
  border: 2px solid #2c6fdb; /* 边框颜色 */
  transition: all 0.3s ease; /* 动画效果 */
  background-color: #ffffff; /* 背景颜色 */
  /* color: #2c6fdb; */ 
  width: 130px;
  height: 40px;
  /* color: #fff; */
  border-radius: 5px; /* 圆角 */
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
  box-shadow: inset 2px 2px 2px 0px rgba(255,255,255,.5),
              7px 7px 20px 0px rgba(0,0,0,.1),
              4px 4px 5px 0px rgba(0,0,0,.1);
  outline: none;
}

</style>

<style scoped>
.highlight-button {
  width: 130px;
  height: 40px;
  color: #fff;
  border-radius: 5px; /* 圆角 */
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
  box-shadow: inset 2px 2px 2px 0px rgba(255,255,255,.5),
              7px 7px 20px 0px rgba(0,0,0,.1),
              4px 4px 5px 0px rgba(0,0,0,.1);
  outline: none;
}

/* 5 */
.button-5 {
  width: 130px;
  height: 40px;
  line-height: 42px;
  padding: 0;
  border: none;
  background: rgb(240, 240, 240); /* 灰白色背景 */
  background: linear-gradient(0deg, rgba(240, 240, 240, 1) 0%, rgba(220, 220, 220, 1) 100%);
  color: #2d467b;
}
.button-5:hover {
  /* color: #5591dc; */
  color: #026b9f;
  background: transparent;
   box-shadow:none;
}
.button-5:before,
.button-5:after{
  content:'';
  position:absolute;
  top:0;
  right:0;
  height:2px;
  width:0;
  /* background: #5591dc; */
  background: #026b9f;
  box-shadow:
   -1px -1px 5px 0px #fff,
   7px 7px 20px 0px #0003,
   4px 4px 5px 0px #0002;
  transition:400ms ease all;
}
.button-5:after{
  right:inherit;
  top:inherit;
  left:0;
  bottom:0;
}
.button-5:hover:before,
.button-5:hover:after{
  width:100%;
  transition:800ms ease all;
}

/* 6 */
.button-6 {
  background: rgb(247,150,192);
  background: radial-gradient(circle, rgba(247,150,192,1) 0%, rgba(118,174,241,1) 100%);
  line-height: 42px;
  padding: 0;
  border: none;
}
.button-6 span {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}
.button-6:before,
.button-6:after {
  position: absolute;
  content: "";
  height: 0%;
  width: 1px;
 box-shadow:
   -1px -1px 20px 0px rgba(255,255,255,1),
   -4px -4px 5px 0px rgba(255,255,255,1),
   7px 7px 20px 0px rgba(0,0,0,.4),
   4px 4px 5px 0px rgba(0,0,0,.3);
}
.button-6:before {
  right: 0;
  top: 0;
  transition: all 500ms ease;
}
.button-6:after {
  left: 0;
  bottom: 0;
  transition: all 500ms ease;
}
.button-6:hover{
  background: transparent;
  color: #76aef1;
  box-shadow: none;
}
.button-6:hover:before {
  transition: all 500ms ease;
  height: 100%;
}
.button-6:hover:after {
  transition: all 500ms ease;
  height: 100%;
}
.button-6 span:before,
.button-6 span:after {
  position: absolute;
  content: "";
  box-shadow:
   -1px -1px 20px 0px rgba(255,255,255,1),
   -4px -4px 5px 0px rgba(255,255,255,1),
   7px 7px 20px 0px rgba(0,0,0,.4),
   4px 4px 5px 0px rgba(0,0,0,.3);
}
.button-6 span:before {
  left: 0;
  top: 0;
  width: 0%;
  height: .5px;
  transition: all 500ms ease;
}
.button-6 span:after {
  right: 0;
  bottom: 0;
  width: 0%;
  height: .5px;
  transition: all 500ms ease;
}
.button-6 span:hover:before {
  width: 100%;
}
.button-6 span:hover:after {
  width: 100%;
}

/* 9 */
.btn-9 {
  border: none;
  transition: all 0.3s ease;
  overflow: hidden;
  /* background-color: #15559a; */
  background-color: #026b9f;
  /* color: #e8d8bb; */
}
.btn-9:after {
  position: absolute;
  content: " ";
  z-index: -1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
   background-color: #1fd1f9;
background-image: linear-gradient(315deg, #1fd1f9 0%, #3b5bdb 74%);
  transition: all 0.3s ease;
}
.btn-9:hover {
  background: transparent;
  box-shadow:  4px 4px 6px 0 rgba(255,255,255,.5),
              -4px -4px 6px 0 rgba(116, 125, 136, .2), 
    inset -4px -4px 6px 0 rgba(255,255,255,.5),
    inset 4px 4px 6px 0 rgba(116, 125, 136, .3);
  color: #fff;
}
.btn-9:hover:after {
  -webkit-transform: scale(2) rotate(180deg);
  transform: scale(2) rotate(180deg);
  box-shadow:  4px 4px 6px 0 rgba(255,255,255,.5),
              -4px -4px 6px 0 rgba(116, 125, 136, .2), 
    inset -4px -4px 6px 0 rgba(255,255,255,.5),
    inset 4px 4px 6px 0 rgba(116, 125, 136, .3);
}

/* 9 */
.btn-9b {
  border: none;
  transition: all 0.3s ease;
  overflow: hidden;
  /* background-color: #f29a76; */
  /* background-color: #f38235; */
  /* background-color: #FFC0CB; */
  background-color: #81D8D0;
}
.btn-9b:after {
  position: absolute;
  content: " ";
  z-index: -1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
   background-color: #1fd1f9;
background-image: linear-gradient(315deg, #ffc9c9 0%, #ff6b6b 74%);
  transition: all 0.3s ease;
}
.btn-9b:hover {
  background: transparent;
  box-shadow:  4px 4px 6px 0 rgba(255,255,255,.5),
              -4px -4px 6px 0 rgba(116, 125, 136, .2), 
    inset -4px -4px 6px 0 rgba(255,255,255,.5),
    inset 4px 4px 6px 0 rgba(116, 125, 136, .3);
  color: #fff;
}
.btn-9b:hover:after {
  -webkit-transform: scale(2) rotate(180deg);
  transform: scale(2) rotate(180deg);
  box-shadow:  4px 4px 6px 0 rgba(255,255,255,.5),
              -4px -4px 6px 0 rgba(116, 125, 136, .2), 
    inset -4px -4px 6px 0 rgba(255,255,255,.5),
    inset 4px 4px 6px 0 rgba(116, 125, 136, .3);
}

/* 9 */
.btn-9c {
  border: none;
  /* transition: all 0.3s ease; */
  /* overflow: hidden; */
  /* background-color: #15559a; */
  background-color: #f0f0f0;
  color: #1a4d9b;
  
}


/* 13 */
.btn-13 {
  /* background-color: #89d8d3; */
  background-color: #077349;
  /* background-image: linear-gradient(315deg, #89d8d3 0%, #03c8a8 74%); */
  background-image: linear-gradient(315deg, #81D8D0 0%, #89d8d3 74%);
  border: none;
  z-index: 1;
}
.btn-13:after {
  position: absolute;
  content: "";
  width: 100%;
  height: 0;
  bottom: 0;
  left: 0;
  z-index: -1;
  border-radius: 5px;
  background-color: #4dccc6;
  background-image: linear-gradient(315deg, #4dccc6 0%, #96e4df 74%);
  box-shadow:
   -7px -7px 20px 0px #fff9,
   -4px -4px 5px 0px #fff9,
   7px 7px 20px 0px #0002,
   4px 4px 5px 0px #0001;
  transition: all 0.3s ease;
}
.btn-13:hover {
  color: #fff;
}
.btn-13:hover:after {
  top: 0;
  height: 100%;
}
.btn-13:active {
  top: 2px;
}


</style>

<style>
/* tooltip body */
.el-tooltip__popper.is-customized {
  background: #026b9f;
  /* background: rgba(2, 107, 159, 0.8); */
  transform: translateX(-20px);
  color: #e8d8bb; /* 文字颜色 */
}

/* tooltip arrow body */
.el-tooltip__popper.is-customized .popper__arrow {
  border-left-color: #026b9f;
}

/* tooltip arrow border */
.el-tooltip__popper.is-customized .popper__arrow::after {
  border-left-color: #026b9f;
}

</style>

<style scoped>
.box-card-a {
  background-color: #f0f4f7; /* 修改背景颜色 */
  color: #333; /* Adjust text color for better readability on the background image */
  
  
}
</style>

<style scoped>
.box-card {
  background-color: #f0f4f7; /* 修改背景颜色 */
  color: #333; /* 调整文本颜色以提高背景上的可读性 */
  display: flex;
  flex-direction: column;
  align-items: center; /* 垂直方向居中 */
  justify-content: center; /* 水平方向居中 */
  text-align: center; /* 文本水平居中 */
}

.box-card span {
  font-size: 18px;
  color: #026b9f;
  margin-bottom: 10px; /* 增加文本之间的间距 */
}

.box-card .button-group {
  display: flex;
  justify-content: center;
  margin-top: 30px;
}

.box-card .button-group el-button {
  margin: 0 15px;
}

.box-card audio {
  width: 500px;
  height: 30px;
  border-radius: 5px;
  margin-top: 20px;
}
</style>

<style scoped>

.form-container {
  display: flex;
  align-items: center;
}

.form-control {
  flex: 1;
  margin-right: 10px;
  margin-left: 200px;
}

input {
  font-size: inherit;
  width: 30%;  /* 修改输入框宽度 */
  height: 30px; /* 修改输入框高度 */
  color: #000; /* 修改字体颜色 */
  margin-left: 50px;
  outline: none;
  display: block;
  font-weight: 400;
  line-height: 1.6;
  padding: 3px 3px 3px 10px;
  border-radius: 10px;
  border: 2px solid #8c8c8c;
  background-color: transparent;
  transition: border-color 0.2s ease-in-out;
  background-repeat: no-repeat;
  background-position: right 2% center;
  background-size: 1.5rem 1.5rem; /* 修改图片大小 */
}

input:focus {
  border-color: #de4437;
}

input[aria-valid="false"] {
  /* border-color: #f6c1b7; */
  border-color: #026b9f;
  /* background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxMicgaGVpZ2h0PScxMicgZmlsbD0nbm9uZScgc3Ryb2tlPScjZGU0NDM3JyB2aWV3Qm94PScwIDAgMTIgMTInPjxjaXJjbGUgY3g9JzYnIGN5PSc2JyByPSc0LjUnLz48cGF0aCBzdHJva2UtbGluZWpvaW49J3JvdW5kJyBkPSdNNS44IDMuNmguNEw2IDYuNXonLz48Y2lyY2xlIGN4PSc2JyBjeT0nOC4yJyByPScuNicgZmlsbD0nI2RlNDQzNycgc3Ryb2tlPSdub25lJy8+PC9zdmc+'); */
  background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxMicgaGVpZ2h0PScxMicgZmlsbD0nbm9uZScgc3Ryb2tlPScjMDI2YjlmJyB2aWV3Qm94PScwIDAgMTIgMTInPjxjaXJjbGUgY3g9JzYnIGN5PSc2JyByPSc0LjUnLz48cGF0aCBzdHJva2UtbGluZWpvaW49J3JvdW5kJyBkPSdNNS44IDMuNmguNEw2IDYuNXonLz48Y2lyY2xlIGN4PSc2JyBjeT0nOC4yJyByPScuNicgZmlsbD0nIzAyNmI5Zicgc3Ryb2tlPSdub25lJy8+PC9zdmc+');

}

input[aria-valid="true"] {
  /* border-color: #077349; */
  border-color: #81D8D0;
  /* background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPSc4JyBoZWlnaHQ9JzgnIHZpZXdCb3g9JzAgMCA4IDgnPjxwYXRoIGZpbGw9JyMzN0M2MjUnIGQ9J00yLjMgNi43M0wuNiA0LjUzYy0uNC0xLjA0LjQ2LTEuNCAxLjEtLjhsMS4xIDEuNCAzLjQtMy44Yy42LS42MyAxLjYtLjI3IDEuMi43bC00IDQuNmMtLjQzLjUtLjguNC0xLjEuMXonLz48L3N2Zz4='); */
  background-image: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPSc4JyBoZWlnaHQ9JzgnIHZpZXdCb3g9JzAgMCA4IDgnPjxwYXRoIGZpbGw9JyM4MUQ4RDAnIGQ9J00yLjMgNi43M0wuNiA0LjUzYy0uNC0xLjA0LjQ2LTEuNCAxLjEtLjhsMS4xIDEuNCAzLjQtMy44Yy42LS42MyAxLjYtLjI3IDEuMi43bC00IDQuNmMtLjQzLjUtLjguNC0xLjEuMXonLz48L3N2Zz4=');

}

</style>

<style scoped>
audio::-webkit-media-controls-panel {
    background-color: #ecf5fc; /* 更改播放条的背景颜色 */
}
</style>

<style>
.custom-radio-group .el-radio__inner {
  width: 16px; /* 自定义按钮宽度 */
  height: 16px; /* 自定义按钮高度 */
}

.custom-radio-group .el-radio__inner::after {
  width: 6px; /* 自定义选中状态下的圆点大小 */
  height: 6px; /* 自定义选中状态下的圆点大小 */
}

.custom-radio-group .el-radio__input.is-checked .el-radio__inner {
  border-color: #026b9f; /* 自定义边框颜色 */
  background-color: #026b9f; /* 自定义背景颜色 */
}

.custom-radio-group .el-radio__input.is-checked+.el-radio__label {
  color: #026b9f; /* 自定义选中后的文字颜色 */
}


</style>

<style>
/* 自定义 el-select 样式 */
.custom-select .el-input__inner {
  /* background-color: #026b9f;*/
  color: #026b9f;
  border-color: #026b9f !important;
  transition: background-color 0.3s ease, color 0.3s ease;
}

</style>

<style scoped>

/* 自定义 el-option 样式 */
.custom-option {
  /* background-color: #026b9f; */
  /* color: #e8d8bb; */
  transition: background-color 0.3s ease, color 0.3s ease;
}

.custom-option:hover {
  /* background-color: #034d75;
  color: #ffffff; */
  background-color: #026b9f;
  color: #e8d8bb;
}

/* 添加选项的悬停动画效果 */
.custom-option {
  position: relative;
  overflow: hidden;
}

.custom-option::before {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.1);
  transition: left 0.3s ease;
}

.custom-option:hover::before {
  left: 0;
}
</style>

<style>


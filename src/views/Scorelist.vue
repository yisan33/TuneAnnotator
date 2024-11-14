<template>
  <!--  <div style="margin-top: 40px">-->
  <div class="manage">

    <el-dialog
        title="提示"
        :visible.sync="dialogVisible"
        width="50%"
        :before-close="handleClose">
      <el-form ref="form" :rules="rules" :inline="true" :model="form" label-width="80px">
        <el-form-item label="整体分数" prop="score">
          <el-input placeholder="请输入整体分数" v-model="form.score"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
          <el-button @click="cancel">取 消</el-button>
          <el-button type="primary" @click="submit(dataa)">确 定</el-button>
      </span>
    </el-dialog>


    <el-dialog
        title="提示"
        :visible.sync="sb1Visible"
        width="50%"
        :before-close="sb1Close">
      <el-form ref="form" :rules="rules" :inline="true" :model="form" label-width="80px">
        <el-form-item label="流派" prop="genre">
          <el-select v-model="value" @change="dylog" placeholder="请选择">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
          <el-button @click="sb1cancel">取 消</el-button>
          <el-button type="primary" @click="sb1submit">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog
        title="提示：（1表示多，0表示不多）"
        :visible.sync="sb2Visible"
        width="50%"
        :before-close="sb2Close">
      <el-form ref="form" :rules="rules" :inline="true" :model="form" label-width="80px">
        和声是否多：
        <el-radio-group v-model="radio" @input="dayin" style="padding-left: 25px">

          <el-radio :label="1">是</el-radio>
          <el-radio :label="0">否</el-radio>
        </el-radio-group>
      </el-form>
      <span slot="footer" class="dialog-footer">
          <el-button @click="sb2cancel">取 消</el-button>
          <el-button type="primary" @click="sb2submit">确 定</el-button>
      </span>
    </el-dialog>


    <!--    <el-dialog-->
    <!--        title="提示"-->
    <!--        :visible.sync="clipVisible"-->
    <!--        width="50%"-->
    <!--        :before-close="clipClose">-->
    <!--      <el-form ref="fclip" :rules="rclips" :inline="true" :model="fclip" label-width="80px">-->
    <!--        <el-form-item label="开始时间" prop="new_start_time">-->
    <!--          <el-input placeholder="请输入开始时间" v-model="fclip.start_time"></el-input>-->
    <!--        </el-form-item>-->
    <!--        <el-form-item label="结束时间" prop="new_end_time">-->
    <!--          <el-input placeholder="请输入结束时间" v-model="fclip.end_time"></el-input>-->
    <!--        </el-form-item>-->

    <!--      </el-form>-->
    <!--      <span slot="footer" class="dialog-footer">-->
    <!--          <el-button @click="cancel">取 消</el-button>-->
    <!--          <el-button type="primary" @click="subclip(clipp)">确 定</el-button>-->
    <!--      </span>-->
    <!--    </el-dialog>-->

    
    
    <el-dialog
        title="提示：（只可以输入1~5之间的数）"
        :visible.sync="dimensionVisible"
        width="50%"
        :before-close="dimensionClose">
      <el-form ref="fclip" :rules="rclips" :inline="true" :model="fclip" label-width="80px">
        <!--        <el-form-item label="种类" prop="new_start_time">-->
        <!--          <el-input placeholder="请输入种类" v-model="fclip.start_time"></el-input>-->
        <!--        </el-form-item>-->
        <el-form-item label="分数" prop="new_dimension_score">
          <el-input placeholder="请输入分数" v-model="fclip.dimension_score"></el-input>
        </el-form-item>

      </el-form>
      <span slot="footer" class="dialog-footer">
          <el-button @click="cancel1">取 消</el-button>
          <el-button type="primary" @click="subdimension(clipp)">确 定</el-button>
      </span>
    </el-dialog>
    
    
    <el-dialog
        title="提示：（维度修改）"
        :visible.sync="dimensionVisible"
        width="50%"
        :before-close="dimensionClose">
      <el-form ref="form2" :rules="rules2" :inline="true" :model="form2" label-width="80px">

        <el-form-item label="分数" prop="dimension_score">
          <el-input placeholder="请输入分数" v-model="form2.dimension_score"></el-input>
        </el-form-item>

      </el-form>
      <span slot="footer" class="dialog-footer">
          <el-button @click="cancel1">取 消</el-button>
          <el-button type="primary" @click="subdimension(clipp)">确 定</el-button>
      </span>
    </el-dialog>
    

    <el-dialog
        title="维度评价列表"
        :visible.sync="copy3Visible"
        width="50%"
        :before-close="listClose3">
      <!--      <audio src="../assets/mp3/星辰大海.mp3" controls>111</audio>-->
      <audio ref="audio"
             controls="controls">
        <source :src='require("@/assets/mp3/" + this.singer + "-" + this.name + "_(Vocals)" + ".wav")' type="audio/wav">
        <!--                <source :src='require("@/assets/mp3/"+ name +".wav")' type="audio/wav">-->
      </audio>

      <el-table
          stripe
          height="65vh"
          :data="scoredimension"
          style="width: 100%"
      >
        <el-table-column
            prop="dimension"
            label="分类">
        </el-table-column>
        <el-table-column
            prop="dimension_score"
            label="分数">
        </el-table-column>
        <el-table-column>
          <template slot-scope="scope">
            <el-button size="mini" @click="dimensionEdit(scope.row)">编辑</el-button>
            <el-button type="primary" @click="getclip">技巧</el-button>
            <!--            <el-button size="mini" @click="getclip">技巧</el-button>-->
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>

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
            prop="start_time"
            label="开始时间">
        </el-table-column>
        <el-table-column
            prop="end_time"
            label="结束时间">
        </el-table-column>
        <el-table-column>
          <template slot-scope="scope">
            <el-button size="mini" @click="clipEdit(scope.row)">编辑</el-button>
            <el-button type="danger" size="mini" @click="clipDelete(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>

    <div class="manage-header">
      <!--      <el-button @click="handleAdd" type="primary">-->
      <!--        + 新增-->
      <!--      </el-button>-->

      <el-form :inline="true" :model="userForm">
        <el-form-item>
          <el-input placeholder="请输入音乐名" v-model="userForm.musicname"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">查询</el-button>
        </el-form-item>
      </el-form>

    </div>


    <div class="common-tabel">
      <el-table
          stripe
          height="65vh"
          :data="tableData"
          style="width: 100%">
        <el-table-column label="序号" type="index" width="180" align="center">
          <template slot-scope="scope">
            {{ (pageData.current_page - 1) * pageData.page_size + scope.$index + 1 }}
          </template>
        </el-table-column>
        <el-table-column
            prop="music_name"
            label="音乐">
        </el-table-column>
        <!--        <el-table-column-->
        <!--            prop="singer"-->
        <!--            label="歌手">-->
        <!--        </el-table-column>-->
        <!--        <el-table-column-->
        <!--            prop="score"-->
        <!--            label="整体分数">-->
        <!--        </el-table-column>-->
        <el-table-column
            prop="mark_time"
            label="评价时间">
        </el-table-column>
        <!--        <el-table-column>-->
        <!--          <template slot-scope="scope">-->
        <!--            <el-button @click="list2(scope.row)" type="primary" size="mini">片段列表</el-button>-->
        <!--          </template>-->
        <!--        </el-table-column>-->
        <el-table-column>
          <template slot-scope="scope">
            <el-button @click="list(scope.row)" type="primary" size="mini">维度评价</el-button>
          </template>
        </el-table-column>
        <el-table-column>
          <template slot-scope="scope">
            <!--            <el-button size="mini" @click="handleEdit(scope.row)">编辑</el-button>-->
            <el-button type="danger" size="mini" @click="handleDelete(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="pager">
        <el-pagination
            layout="prev, pager, next"
            :total="total"
            @current-change="handlePage">
        </el-pagination>

      </div>


    </div>
  </div>
  <!--  </div>-->
</template>

<script>
import {
  getUserPageScores,
  getUserScoresNumber,
  deleteAMarkedScore,
  updateAMarkedScore,
  getUserMusicClips,
  deleteAMarkedClip,
  updateAMarkedClip,
  getMarkedScoresByQuery,
  getUserMusicDimensionscore,
  updateAMarkedDimensionscore,
  getASongID,
  updateMusicGenre,
  updateMusicHarmonyQuantity

} from '@/api/api'

export default {
  data() {
    return {
      userid: '',
      user_id: '',
      radio: '',
      singer: '',
      value: '',
      ishs: '0',
      isable: true,
      isliupai: 1,
      new_genre: "",
      genre: "",
      name: "点击下一首开始评价",
      box: undefined,
      play: false, // 播放状态，true为正在播放
      dialogVisible: false,
      clipVisible: false,
      dimensionVisible: false,
      sb1Visible: false,
      sb2Visible: false,
      dataa: {
        new_score: '',
        score_id: '',
      },
      liupai: {
        music_id: '',
        new_genre: '',
      },
      clipp: {
        clip_id: '',
        new_dimension_score: '',
        new_type: '',
        new_start_time: '',
        new_end_time: '',
      },
      form: {
        // music_name: '',
        // singer: '',
        score: '',
        // mark_time: '',
      },
      ///
      form2: {
        dimension_score: '',
      },
      ///
      fclip: {
        type: '',
        start_time: '',
        end_time: '',
        dimension_score: '',
      },
      id: "",
      music_id: "",
      clipid: 0,
      dimensionid: 0,
      dimension: '',
      rclips: {
        type: [
          {required: true, message: '请输入分类名'}
        ],
        new_start_time: [
          {required: true, message: '请输入起始时间'}
        ],
        new_end_time: [
          {required: true, message: '请输入结束时间'}
        ],
        new_clip_score: [
          {required: true, message: '请输入分数'}
        ],
      },
      ///
      rules2: {
        dimension_score: [
          { required: true, message: '请输入分数'}
        ],
      },
      ///
      rules: {
        score: [
          {required: true, message: '请输入分数'}
        ],
      },
      copyVisible: false,
      copy2Visible: false,
      copy3Visible: false,
      tableData: [],
      scoreclip: [],
      scoredimension: [],
      modalType: 0,  //0表示新增的弹窗，1表示编辑
      clipType: 0,  //0表示新增的弹窗，1表示编辑
      dimensionType: 0,
      total: 0, //当前的总条数
      pageData: {
        user_id: 0,
        current_page: 1,
        page_size: 10
      },
      clipData: {
        user_id: 0,
        music_id: 0,
      },
      userForm: {
        musicname: ''
      },
      options: [{
        value: '抒情流行',
        label: '抒情流行'
      }, {
        value: 'R&B',
        label: 'R&B'
      }, {
        value: '摇滚',
        label: '摇滚'
      }, {
        value: '民谣',
        label: '民谣'
      }],
      scoreList: '',
    }
  },
  created() {
    window.addEventListener('keydown', this.handkeyCode, true)//开启监听键盘按下事件
  },
  mounted() {
    function getuserid() {

    }

    getuserid()
    {
      this.user_id = this.$route.params.user_id
      this.userid = sessionStorage.getItem('user_id');
      this.pageData.user_id = this.userid
      this.clipData.user_id = this.userid
      // console.log(this.userid)
      // console.log(this.clipData.user_id)
    }
    this.getList()
    // this.getclip()
    this.init();
  },
  methods: {
    init() {
      this.box = this.$refs["audio"];
      this.box.src = require(`${this.src}`);
    },
    // 提交评价表单
    dylog(setval) {
      this.new_genre = setval
      console.log(this.new_genre)
    },
    dayin(val) {
      this.ishs = val
      console.log(this.ishs)
    },
    submit() {
      //后续对表单数据的处理
      let new_score = this.form.score
      if (new_score > 100 || new_score < 0) {
        this.$message({
          type: 'false',
          message: '分数在0~100之间!'
        });
      } else {
        updateAMarkedScore({'new_score': new_score, 'score_id': this.id}).then(response => {
          if (response.status === 200) {
            this.$message({
              type: 'success',
              message: '修改成功!'
            });
            this.getdimension()
          }
        })
        // 清空表单的数据
        this.$refs.form.resetFields()
        // 关闭弹窗
        this.dialogVisible = false
      }
    },
    subclip() {
      let new_start_time = this.fclip.start_time
      let new_end_time = this.fclip.end_time
      // console.log(new_type)
      // console.log(new_start_time)
      // console.log(new_end_time)
      updateAMarkedClip({
        'clip_id': this.clipid,
        'new_start_time': new_start_time,
        'new_end_time': new_end_time,
      }).then(response => {
        if (response.status === 200) {
          this.$message({
            type: 'success',
            message: '修改成功!'
          });
          this.getclip()
        }
      })
      // 清空表单的数据
      this.$refs.fclip.resetFields()
      // 关闭弹窗
      this.clipVisible = false
    },
    ///
    /*
    subdimension() {
      let new_dimension_score = this.fclip.dimension_score
      console.log(new_dimension_score)
      if (new_dimension_score === '1' || new_dimension_score === '2' || new_dimension_score === '3' || new_dimension_score === '4' || new_dimension_score === '5' || new_dimension_score === 1 || new_dimension_score === 2 || new_dimension_score === 3 || new_dimension_score === 4 || new_dimension_score === 5) {
        updateAMarkedDimensionscore({
          'dimension_score_id': this.dimensionid,
          'new_dimension_score': new_dimension_score,
        }).then(response => {
          if (response.status === 200) {
            this.$message({
              type: 'success',
              message: '修改成功!'
            });
            this.getdimension()
          }
        })
        // 清空表单的数据
        this.$refs.fclip.resetFields()
        // 关闭弹窗
        this.dimensionVisible = false
      } else {
        this.$message({
          type: 'false',
          message: '分数在1~5之间!'
        });
      }
    },
    */
    ///
    subdimension() {
      let new_dimension_score = Number(this.form2.dimension_score)
      console.log(new_dimension_score)
      console.log(this.dimensionid)
      if (new_dimension_score >= 0 && new_dimension_score <= 100 && Number.isInteger(new_dimension_score)) {
        updateAMarkedDimensionscore({
          'dimension_score_id': this.dimensionid,
          'new_dimension_score': new_dimension_score,
        }).then(response => {
          if (response.status === 200) {
            this.$message({
              type: 'success',
              message: '修改成功!'
            });
            this.getdimension()
          }
        })
        // 清空表单的数据
        this.$refs.form2.resetFields()
        // 关闭弹窗
        this.dimensionVisible = false
      } else {
        this.$message({
          type: 'false',
          message: '请保持分数在0~100之间！'
        });
      }
    },
    ///
    getList() {
      // 获取的列表的数据
      getUserScoresNumber(this.pageData).then(response => {
        // console.log(response.data)
        this.total = response.data || 0
      })
      getUserPageScores(this.pageData).then(response => {
        this.tableData = response.data
        // console.log(this.tableData)
      })
    },
    getclip() {
      console.log("技巧")
      getUserMusicClips(this.clipData).then(response => {
        this.scoreclip = response.data
        console.log(this.scoreclip)
        // console.log(response.data)
      })
    },
    getdimension() {
      getUserMusicDimensionscore(this.clipData).then(response => {
        this.scoredimension = response.data
        console.log(this.scoredimension)
      })
    },
    onLoadedmetadata(res) {
      // console.log('loadedmetadata')
      // console.log(res)
      this.audio.waiting = false
      this.audio.maxTime = parseInt(res.target.duration)
    },
    onTimeupdate(res) {
      // console.log('timeupdate')
      // console.log(res)
      this.audio.currentTime = res.target.currentTime
      this.sliderTime = parseInt(this.audio.currentTime / this.audio.maxTime * 100)
    },
    clearData() {
      //清除编辑窗体的缓存数据
      this.form.id = 0;
      this.form.score = '';
      this.dialogVisible = false;
    },
    // clearclip() {
    //   //清除编辑窗体的缓存数据
    //   this.form.id = 0;
    //   this.form.score = '';
    //   this.dialogVisible = false;
    // },

    list(row) {
      this.clipData.music_id = row.music_id
      this.music_id = row.music_id
      this.getdimension()
      getASongID({'music_id': row.music_id}).then(response => {
        var song = response.data[0]
        console.log(song)
        this.name = song.music_name
        this.singer = song.singer
        this.src = require('@/assets/mp3/' + this.singer + '-' + this.name + '_(Vocals)' + '.wav')
        this.$refs.audio.src = this.src;
        this.$refs.audio.play()
      })

      this.copy3Visible = true
    },
    sb1submit() {
      updateMusicGenre({'new_genre': this.new_genre, 'music_id': this.music_id}).then(response => {
        if (response.status === 200) {
          this.$message({
            type: 'success',
            message: '修改成功!'
          });
          this.getdimension()
        }
      })
      this.value = ''
      this.sb1Visible = false
      // this.copy3Visible = false
    },
    sb2submit() {
      console.log(this.ishs)
      updateMusicHarmonyQuantity({'music_id': this.music_id, 'new_harmony_quantity': this.ishs}).then(response => {
        if (response.status === 200) {
          this.$message({
            type: 'success',
            message: '修改成功!'
          });
          this.getdimension()
        }
      })
      this.radio = ''
      this.sb2Visible = false
    },
    list2(row) {
      this.clipData.music_id = row.music_id
      this.getclip()
      this.copy2Visible = true
    },
    dimensionClose() {
      // this.$refs.form.resetFields()
      this.dimensionVisible = false
    },
    handleClose() {
      this.$refs.form.resetFields()
      this.dialogVisible = false
    },
    sb1Close() {
      this.$refs.form.resetFields()
      this.sb1Visible = false
      this.getdimension()
    },
    sb2Close() {
      this.$refs.form.resetFields()
      this.sb2Visible = false
      this.radio = ''
      this.getdimension()
    },
    clipClose() {
      this.$refs.fclip.resetFields()
      this.clipVisible = false
    },
    listClose() {
      // this.$refs.form.resetFields()
      this.copyVisible = false
    },
    listClose2() {
      // this.$refs.form.resetFields()
      this.copy2Visible = false
    },
    listClose3() {
      // this.$refs.form.resetFields()
      this.copy3Visible = false
      this.$refs.audio.pause()
    },
    cancel() {
      this.handleClose()
    },
    sb1cancel() {
      this.sb1Close()
    },
    sb2cancel() {
      this.sb2Close()
    },
    cancel1() {
      this.dimensionClose()
    },
    handleEdit(row) {
      this.clearData();
      this.modalType = 1
      this.dialogVisible = true
      console.log(row)
      if (row) {
        //编辑
        this.title = '编辑窗体';
        this.id = row.score_id;
        this.form.score = row.score;
      }
      // 注意需要对当前行数据进行深拷贝，否则会出错
      // this.form = JSON.parse(JSON.stringify(row))
    },
    clipEdit(row) {
      // this.clearData();
      this.clipType = 1
      this.clipVisible = true
      console.log(row)
      if (row) {
        //编辑
        this.title = '编辑窗体';
        this.clipid = row.clip_id;
        // console.log(this.id)
        this.fclip.start_time = row.start_time;
        this.fclip.end_time = row.end_time;
      }
      // 注意需要对当前行数据进行深拷贝，否则会出错
      // this.form = JSON.parse(JSON.stringify(row))
    },
    dimensionEdit(row) {
      console.log(row)
      console.log(1223453)
      this.dimension = row.dimension
      // console.log(this.dimension)
      if (this.dimension === "整体分数") {
        this.clearData();
        this.modalType = 1
        this.dialogVisible = true
        console.log(row)
        console.log(145689)
        if (row) {
          //编辑
          this.title = '编辑窗体';
          this.id = row.score_id;
          console.log(this.id)
          this.form.score = row.score;
        }
      ///
      //} else if (this.dimension === "旋律") {
      //  this.clearData();
      //  this.modalType = 1
      //  this.dialogVisible = true
      //  if (row) {
      //    //编辑
      //    this.title = '编辑窗体';
      //    this.id = row.score_id;
      //    console.log(this.id)
      //    this.form.score = row.score;
      //  }
      ///
      } else if (this.dimension === "流派") {
        console.log(row)
        console.log(145689)
        this.sb1Visible = true
        this.liupai.new_genre = row.genre
      } else if (this.dimension === "和声是否多") {
        this.sb2Visible = true
      } else {
        this.dimensionType = 1
        this.dimensionVisible = true
        if (row) {
          //编辑
          this.title = '编辑窗体';
          this.dimensionid = row.dimension_score_id;
          /// this.fclip.dimension_score = row.dimension_score;
          this.form2.dimension_score = row.dimension_score;
        }
      }
      // 注意需要对当前行数据进行深拷贝，否则会出错
      // this.form = JSON.parse(JSON.stringify(row))
    },
    handkeyCode(e) {
      console.log(e); // 打印出按键后的信息
      if (e.keyCode === 13) {
        getMarkedScoresByQuery({'query': this.userForm.musicname}).then(response => {
          this.tableData = response.data
          console.log(this.tableData)
        })
      }
    },
    ///
    /*
    handleDelete(score_id) {
      console.log(score_id)
      this.$confirm('此操作将永 久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        callback: (action) => {
          if (action === 'confirm') {
            deleteAMarkedScore(score_id).then(response => {
              if (response.status === 200) {
                this.$message({
                  type: 'success',
                  message: '删除成功!'
                });
                this.getList()
              }
            })
          } else {
            this.$message({
              type: 'info',
              message: '已取消删除'
            });
          }
        }
      });
    },
    */
    /// 删除评分记录时,新增将四个维度分一并删除
    handleDelete(row) {
      console.log(row)
      console.log(row.score_id)
      console.log(row.dimension_score_0_id)
      console.log(row.dimension_score_1_id)
      console.log(row.dimension_score_2_id)
      console.log(row.dimension_score_3_id)
      this.$confirm('此操作将删除该歌曲所有评分记录,是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        callback: (action) => {
          if (action === 'confirm') {
            deleteAMarkedScore( {
              score_id: row.score_id, 
              dimension_score_0_id: row.dimension_score_0_id, 
              dimension_score_1_id: row.dimension_score_1_id, 
              dimension_score_2_id: row.dimension_score_2_id, 
              dimension_score_3_id: row.dimension_score_3_id}).then(response => {
              if (response.status === 200) {
                this.$message({
                  type: 'success',
                  message: '删除成功!'
                });
                this.getList()
              }
            })
          } else {
            this.$message({
              type: 'info',
              message: '已取消删除'
            });
          }
        }
      });
    },
    ///
    clipDelete(clip_id) {
      console.log(clip_id)
      this.$confirm('此操作将永 久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        callback: (action) => {
          if (action === 'confirm') {
            deleteAMarkedClip(clip_id).then(response => {
              if (response.status === 200) {
                this.$message({
                  type: 'success',
                  message: '删除成功!'
                });
                this.getclip()
              }
            })
          } else {
            this.$message({
              type: 'info',
              message: '已取消删除'
            });
          }
        }
      });
    },
    dimensionDelete(dimension_score_id) {
      console.log(dimension_score_id)
      this.$confirm('此操作将永 久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        callback: (action) => {
          if (action === 'confirm') {
            deleteAMarkedClip(dimension_score_id).then(response => {
              if (response.status === 200) {
                this.$message({
                  type: 'success',
                  message: '删除成功!'
                });
                this.getdimension()
              }
            })
          } else {
            this.$message({
              type: 'info',
              message: '已取消删除'
            });
          }
        }
      });
    },

    // 选择页码的回调函数
    handlePage(val) {
      // console.log(val, 'val')
      this.pageData.current_page = val
      this.getList()
    },
    // // 列表的查询
    onSubmit() {
      ///
      //console.log(row)
      console.log(333)
      const user_id = this.userid;
      console.log(user_id)
      ///
      // this.getList()
      //if (!this.userForm.musicname) {
      //  this.$message.error('请输入音乐名');
      //  return;
      //}
      getMarkedScoresByQuery({'query': this.userForm.musicname, 'user_id': user_id}).then(response => {
        this.tableData = response.data
        console.log(this.tableData)
      })
    },
  }
}
</script>

<style lang="less" scoped>
.manage {
  padding-top: 25px;
  height: 90%;

  .manage-header {
    padding-top: 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .common-tabel {
    position: relative;
    height: calc(100% - 62px);

    .pager {
      position: absolute;
      bottom: 0;
      right: 20px;
    }
  }
}
</style>
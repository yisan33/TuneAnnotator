<template>


    <div class="header-container">
      <div class="header">
        <img class="logo1" src="../assets/images/school.png">
        <div class="font" ></div>
        <img class="logo2" src="../assets/images/school2.png">
        </div>
<!--    <div class="l-content">-->
<!--      <el-button @click="handMenu" icon="el-icon-menu" size="mini"></el-button>-->
<!--      <span class="text">首页</span>-->
<!--    </div>-->
    <div class="r-content">
      <el-dropdown @command="handleClick">
        <span class="el-dropdown-link">
          <img class="user" src="../assets/images/xitured.jpg" alt="">
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="cancel" >退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>


</template>

<script>
import { mapState } from 'vuex'
import Cookie from 'js-cookie'
export default {
  name: "CommonHeader",
  methods: {
        handleMenu() {
            this.$store.commit('collapseMenu')
        },
        handleClick(command) {
            if (command === 'cancel') {
                console.log('登出')
                // 登录拦截取消
                sessionStorage.removeItem('user_id')
                sessionStorage.removeItem('user_name')
                // 清除cookie中的token
                Cookie.remove('token')
                // 清除cookie中的menu
                Cookie.remove('menu')
                // 跳转到登录页
                this.$router.push('/login')
            }
        }
    },
  computed: {
        ...mapState({
            tags: state => state.tab.tabsList
        })
    }
}
</script>

<style lang="less" scoped>
.header-container {
  background-color: #333;
  height: 50px;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  .text {
    color: #fff;
    font-size: 14px;
    margin-left: 10px;
  }
  .r-content {
    .user {
      width: 50px;
      height: 50px;
      border-radius: 50%;
    }
  }
}
.header{
      //background: black;
      //height: 80px;
      position: relative;
  }

  .logo1{
      float: left;
      margin-top: 10px;
      margin-left: 25px;
      margin-right: 20px;
      height: 60px;
  }
  .logo2{
      float: left;
      margin-top: 10px;
      margin-left: 20px;
      height: 60px;
  }
  .font{
    float:left;
    margin-top: 15px;
    width: 1px;
    height: 50px;
    background: white;
  }
  .font1{
    height: auto;
    font-size: 35px;
    //position: absolute;
    padding-left: 200px;
    left:44%;
    font-family:KaiTi;
    color: white;
    padding-top: 18px;
  }
</style>
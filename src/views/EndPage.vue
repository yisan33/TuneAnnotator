<template>
  <div class="login-background">
    <div class="background-image"></div>
    <el-form ref="form" label-width="70px" class="login-container" :model="form">
      <h3 class="login_title">标注完成，关闭页面即可</h3>
    </el-form>
  </div>
</template>

<script>
import CustomInput from './CustomInput.vue'
import Mock from 'mockjs'
import Cookie from 'js-cookie'
// import { getMenu } from '../api'
import {getMarkedScoresByQuery, login} from "@/api/api";
import axios from "axios";
export default {
  components: {
    CustomInput
  },
  data() {
    return {
      form: {
        user_name: '',
        user_password: ''
      }
    }
  },

  methods: {
    submit() {
          login({'user_name': this.form.user_name, 'user_password': this.form.user_password}).then(response => {
            if (response.data.loginstatus === 1) {
              // token信息存入cookie用于不同页面间的通信
              Cookie.set('token', response.data.token)
              sessionStorage.setItem('user_name', response.data.user_name)
              sessionStorage.setItem('user_id', response.data.user_id)
              this.$router.push({path:'/page2', params:{user_name:response.data.user_name}})
            } else {
              this.$message.error(response.data.message);
            }
          }).catch((error) => {
            alert(error.response.data)
          })
    },
    // 监听回车键执行事件
    keyDown (e) {
      // 回车则执行登录方法 enter键的ASCII是13
      if (e.keyCode === 13) {
        this.submit() // 需要执行的方法方法
      }
    }
  },
  // 绑定监听事件
  mounted () {
    window.addEventListener('keydown', this.keyDown)
  },
  // 销毁事件
  destroyed () {
    window.removeEventListener('keydown', this.keyDown, false)
  }

}
</script>

<style lang="less" scoped>
.login-background {
  background: url('@/assets/images/login1.jpg') no-repeat center center fixed;
  background-size: cover;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden; /* 确保子元素不会溢出父容器 */
}
.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/images/login1.jpg');
  background-size: cover;
  background-position: center;
  filter: blur(10px); /* 设置模糊效果 */
  z-index: -1; /* 确保背景图片在其他元素下方 */
}
.login-container {
    width: 400px;
    border: 1px solid #eaeaea;
    margin: 180px auto;
    padding: 35px 35px 5px 35px;
    background-color: rgba(255, 255, 255, 0.7);
    border-radius: 15px;
    box-shadow: 0 0 25px #cac6c6;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    backdrop-filter: blur(5px); /* 对背景进行模糊处理 */
    

    .login_title {
        text-align: center;
        margin-bottom: 35px;
        color: #505458;
        font-size: 25px;
    }
}
.register-prompt {
  font-size: 13px;
  margin-top: 20px;
  text-align: center;
  opacity: 0.8;
}
.register-prompt a {
  font-size: 13px;
  color: #2c6fdb;
  text-decoration: none;
}
</style>
<template>
  <div class="login-background">
    <div class="background-image"></div>

    <el-form ref="form" label-width="70px" :inline="true" class="login-container" :model="form" :rules="rules">
      <h3 class="login_title">系统注册</h3>
      <custom-input v-model="form.user_name" placeholder="请输入账号" icon="ri-user-3-line"></custom-input>
      <custom-input v-model="form.password1" placeholder="请输入密码" type="password" icon="ri-lock-2-line"></custom-input>
      <custom-input v-model="form.password2" placeholder="请再次输入密码" type="password" icon="ri-lock-2-line"></custom-input>
      <el-button @click="tologin" type="primary">注册</el-button><br>
    </el-form>
  
  </div>
</template>

<script>
import CustomInput from './CustomInput.vue'
import Mock from 'mockjs'
import Cookie from 'js-cookie'
import {register} from "@/api/api";
import {getMenu} from '../api'
import axios from "axios";

export default {
  components: {
    CustomInput
  },
  data() {
    return {
      form: {
        user_name: '',
        user_phone: '',
        password1: '',
        password2: ''
      },
      rules: {
        user_name: [
          {required: true, trigger: 'blur', message: '请输入用户名'}
        ],
        password1: [
          {required: true, trigger: 'blur', message: '请输入密码'}
        ],
        password2: [
          {required: true, trigger: 'blur', message: '请再次输入密码'}
        ],
        user_phone: [
          {required: true, trigger: 'blur', message: '请输入手机号'}
        ],
      }
    }
  },
  methods: {
    tologin() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          getMenu(this.form).then(({data}) => {
            console.log(data)
            console.log(this.form.password1)
            if (this.form.password1 !== this.form.password2) {
              this.$message({
                type: 'info',
                message: '两次密码不一致!'
              });
            } else {
              this.form['user_password'] = this.form.password1
              register(this.form).then(response => {
                console.log(response.data)
              }).catch((error) => {
                alert(error.response.data)
              })
              this.$message({
                type: 'success',
                message: '注册成功!'
              });
              this.$router.push('/login')
            }
          })
        } else {
          this.$message({
            type: 'info',
            message: '请完整输入!'
          });
        }
      })
    }
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

.login-container {
  width: 350px;
  border: 1px solid #eaeaea;
  margin: 180px auto;
  padding: 35px 35px 15px 35px;
  background-color: rgba(255, 255, 255, 0.7);
  border-radius: 15px;
  box-shadow: 0 0 25px #cac6c6;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  backdrop-filter: blur(5px); /* 对背景进行模糊处理 */

  .login_title {
    text-align: center;
    margin-bottom: 40px;
    color: #505458;
    font-size: 25px
  }

  .el-input {
    width: 198px;
  }
}
</style>
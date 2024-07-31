<template>

  <el-form ref="form" label-width="70px" :inline="true" class="login-container" :model="form" :rules="rules">
    <h3 class="login_title">系统登录</h3>
    <el-form-item label="用户名" prop="user_name">
      <el-input v-model="form.user_name" placeholder="请输入账号"></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="user_password">
      <el-input type="password" v-model="form.user_password" placeholder="请输入密码"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button @click="submit" style="margin-left: 105px;margin-top: 10px;" type="primary">登录</el-button>
      <el-button @click="toregist" style="margin-left: 105px;margin-top: 10px;">注册</el-button>
    </el-form-item>
  </el-form>

</template>

<script>
import Mock from 'mockjs'
import Cookie from 'js-cookie'
// import { getMenu } from '../api'
import {getMarkedScoresByQuery, login} from "@/api/api";
import axios from "axios";
export default {
  data() {
    return {
      form: {
        user_name: '',
        user_password: ''
      },
      rules: {
        user_name: [
          {required: true, trigger: 'blur', message: '请输入用户名'}
        ],
        user_password: [
          {required: true, trigger: 'blur', message: '请输入密码'}
        ]
      }
    }
  },

  methods: {
        // 登录
    
    submit() {
          login({'user_name': this.form.user_name, 'user_password': this.form.user_password}).then(response => {
            // console.log(response.data)
            if (response.data.loginstatus === 1) {
              // console.log(response.data.user_name)
              // token信息存入cookie用于不同页面间的通信
              Cookie.set('token', response.data.token)
              sessionStorage.setItem('user_name', response.data.user_name)
              sessionStorage.setItem('user_id', response.data.user_id)
              // 跳转到首页
              this.$router.push({path:'/home',name:'home',params:{user_name:response.data.user_name}})
            } else {
              this.$message.error(response.data.message);
            }
          }).catch((error) => {
            alert(error.response.data)
          })
    },
    
    /*
    submit() {
        let uname = this.form.user_name
        let upass = this.form.user_password
        if(uname === 'wcy'){
          if(upass === 'wcy'){
                         Cookie.set('token', uname)
               sessionStorage.setItem('user_name', uname)
               // 跳转到首页
               this.$router.push({path:'/home',name:'home'})
          }
        }
    },
    */

    toregist() {
      const token = Mock.Random.guid()
      Cookie.set('token', token)
      this.$router.push('/register')
      Cookie.remove('token')
    }
  }
}
</script>

<style lang="less" scoped>
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
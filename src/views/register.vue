<template>

  <el-form ref="form" label-width="70px" :inline="true" class="login-container" :model="form" :rules="rules">
    <h3 class="login_title">系统注册</h3>
    <el-form-item label="用户名" prop="user_name">
      <el-input v-model="form.user_name" placeholder="请输入账号"></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password1">
      <el-input type="password" v-model="form.password1" placeholder="请输入密码"></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password2">
      <el-input type="password" v-model="form.password2" placeholder="请再次输入密码"></el-input>
    </el-form-item>
    <el-form-item label="手机号" prop="user_phone">
      <el-input type="phone" v-model="form.user_phone" placeholder="请输入手机号"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button @click="tologin" style="margin-left: 105px;margin-top: 10px;" type="primary">注册</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import Mock from 'mockjs'
import Cookie from 'js-cookie'
import {register} from "@/api/api";
import {getMenu} from '../api'
import axios from "axios";

export default {
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
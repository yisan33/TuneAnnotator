import http from '../utils/request'



export const getData = () => {
    return http.get('/home/getData')
}

export const getUser = (params) => {
    return http.get('/user/getUser', params)
}

export const addUser = (data) => {
    return http.post('/user/add', data)
}

export const editUser = (data) => {
    return http.post('/user/edit', data)
}

export const delUser = (data) => {
    return http.post('/user/del', data)
 }

 export const getMenu = (data) => {
    return http.post('/permission/getMenu', data)
 }

 export const getScore = (params) => {
    return http.get('/user/del', params)
 }

 import Vue from 'vue'
import Axios from 'axios'

const axiosInstance = Axios.create({
    withCredentials: true
})

// 通过拦截器处理csrf问题，这里的正则和匹配下标可能需要根据实际情况小改动
axiosInstance.interceptors.request.use((config) => {
    config.headers['X-Requested-With'] = 'XMLHttpRequest'
    const regex = /.*csrftoken=([^;.]*).*$/
    config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]
    return config
})

axiosInstance.interceptors.response.use(
    response => {
        return response
    },
    error => {
        return Promise.reject(error)
    }
)

Vue.prototype.axios = axiosInstance

export default axiosInstance

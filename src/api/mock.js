import Mock from 'mockjs'

import homeApi from './mockServeData/home'
import user from './mockServeData/musiclist'
import permission from './mockServeData/permission'
Mock.mock('/api/home/getData', homeApi.getStatisticalData)

Mock.mock('/api/user/add',user.createUser)
Mock.mock('/api/user/edit',user.updateUser)
Mock.mock('/api/user/del',user.deleteUser)
Mock.mock(/api\/user\/getUser/,user.getUserList)
Mock.mock(/api\/permission\/getMenu/, 'post', permission.getMenu)
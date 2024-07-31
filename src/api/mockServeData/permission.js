import Mock from 'mockjs'
export default {
  getMenu: config => {
    const { username, password } = JSON.parse(config.body)
    // 先判断用户是否存在
    // 判断账号和密码是否对应
    if (username === 'admin' && password === 'admin') {
      return {
        code: 20000,
        data: {
          token: Mock.Random.guid(),
          message: '获取成功'
        }
      }
    }  else {
      return {
        code: -999,
        data: {
          message: '密码错误'
        }
      }
    }

  }
}
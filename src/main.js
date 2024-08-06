import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './router'
import store from './store'
import stores from './store/stores'
import Video from 'video.js'

import 'video.js/dist/video-js.css'
import './api/mock'
import Cookie from "js-cookie"

import 'remixicon/fonts/remixicon.css'

// import '../static/font/iconfont.css'
// import '../static/css/style.css'
import Aplayer from 'vue-aplayer'
// import './js/jquery'
// import './js/index99'
Vue.prototype.$video = Video  // 在vue的原生里添加了Video这个标签，增强了vue的功能性




Vue.config.productionTip = false

Vue.use(ElementUI);
Vue.use(Aplayer);

new Vue({
  router,
  store,
  stores,
  render: h => h(App),
}).$mount('#app')

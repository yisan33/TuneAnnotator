import Vue from 'vue'
import VueRouter from "vue-router";
import Home from '../views/Home'
import User from '../views/User'
import Main from '../views/Main'
import Scorelist from '../views/Scorelist'
import PageOne from '../views/PageOne'
import PageTwo from '../views/PageTwo'
import Login from '../views/Login'
import register from '../views/register'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Main,
    redirect: '/home',
    children: [
      { path: 'home',name:'home', component: Home, meta:{requireAuth: true} },
      { path: 'user', component: User, meta:{requireAuth: true} },
      { path: 'scorelist', component: Scorelist, meta:{requireAuth: true} },
      { path: 'user', component: User, meta:{requireAuth: true} },
      { path: 'page1', component: PageOne, meta:{requireAuth: true} },
      { path: 'page2', component: PageTwo, meta:{requireAuth: true} },
    ],
    meta: {
      requireAuth: true
    }
  },
  {
    path: '/register',
    name: 'register',
    component: register
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },


]

const router = new VueRouter({
  routes // (缩写) 相当于 routes: routes
})

router.beforeEach((to, from, next) => {
  if(to.meta.requireAuth){
    if(sessionStorage.user_id){
      next();
    }else{
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    }
  }else{
    next();
  }
})

export default router

import Vue from 'vue'
import Router from 'vue-router'
import store from '../store.js'
import Index from '../components/Index.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
//import  from '../components/SignUp.vue'


Vue.use(Router)

let router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: '/',
      component: Index,
      // meta: { 
      //   requiresAuth: true
      // }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
  ]
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login') 
  } else {
    next() 
  }
})

export default router
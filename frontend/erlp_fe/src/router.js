import { createRouter, createWebHashHistory } from 'vue-router'
import App                                    from './App.vue'

import Login                                  from './components/Login.vue'
import SignUp                                 from './components/SignUp.vue'
import Home                                   from './components/Home.vue'
import Account                                from './components/Account.vue'
import Create                                 from './components/Create.vue'
import Delete                                 from './components/Delete.vue'
import Update                                 from './components/Update.vue'
import View                                   from './components/View.vue'


const routes = [
  {
    path: '/',
    name: 'root',
    component: App
  },
  {
    path: '/user/login',
    name: "login",
    component: Login
  },
  {
    path: '/user/signUp',
    name: "signUp",
    component: SignUp
  },
  {
    path: '/user/home',
    name: "home",
    component: Home
  },
  {
    path: '/user/account',
    name: "account",
    component: Account
  },
  {
    path: '/user/create',
    name: "create",
    component: Create
  },
  {
    path: '/user/delete',
    name: "delete",
    component: Delete
  },
  {
    path: '/user/update',
    name: "update",
    component: Update
  },
  {
    path: '/user/view',
    name: "view",
    component: View
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

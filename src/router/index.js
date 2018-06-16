import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Index from '@/Views/Index'
import SignIn from '@/Views/SignIn'
import SignUp from '@/Views/SignUp'
import ActionRecord from '@/Views/ActionRecord'
import IPFS from "@/Views/IPFS"
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/SignUp',
      name: 'SignUp',
      component: SignUp
    },
    {
      path: '/SignIn',
      name: 'SignIn',
      component: SignIn
    },
    {
      path: '/ActionRecord',
      name: 'ActionRecord',
      component: ActionRecord
    },
    {
      path: '/IPFS',
      name: 'IPFS',
      component: IPFS
    }
  ]
})

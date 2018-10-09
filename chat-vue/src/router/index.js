import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'

import Room from '@/components/rooms/Room'
import Dialog from '@/components/rooms/Dialog'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'room',
            component: Room
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/dialog/:id',
            name: 'dialog',
            component: Dialog
        },
    ]
})

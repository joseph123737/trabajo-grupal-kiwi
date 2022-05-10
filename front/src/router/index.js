import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/varcode',
    name: 'Var-Code',
    component: () => import('@/pages/varcode/VarCodePage.vue'),
  },
  {
    path: '/qrcode',
    name: 'QrCode',
    component: () => import('@/pages/qr/QrPageLecture.vue'),
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router

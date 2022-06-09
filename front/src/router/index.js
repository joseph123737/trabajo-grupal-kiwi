import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: '/:line',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/selectLine',
    name: 'SelectLine',
    component: () => import('@/pages/selectLine/SelectLinePage.vue'),
  },
  {
    path: '/',
    name: 'BarCode',
    component: () => import('@/pages/barcode/BarCodePage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

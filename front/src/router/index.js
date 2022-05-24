import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/barcode',
    name: 'BarCode',
    component: () => import('@/pages/barcode/BarCodePage.vue'),
  },
  {
    path: '/qrcode',
    name: 'QrCode',
    component: () => import('@/pages/qr/QrPageLecture.vue'),
  },
  {
    path: '/loading',
    name: 'Loading',
    component: () => import('@/pages/components/LoadingScreen.vue'),
  },
  
]

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;

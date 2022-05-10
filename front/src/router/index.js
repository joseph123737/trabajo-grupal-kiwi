import { createRouter, createWebHistory } from "vue-router";

const routes = [
	{
		path: "/",
		name: "Home",
		component: () => import("@/pages/home/HomePage.vue"),
	},
	{
		path: "/barcode",
		name: "Bar-Code",
		component: () => import("@/pages/barcode/BarCodePage.vue"),
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;

import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/Home.vue"
import LoginView from "../views/Login.vue"
import SignupView from "../views/Signup.vue"

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
	{
	    path: "/",
	    name: "home",
	    component: HomeView,
	},
	{
	    path: "/login",
	    name: "Login",
	    component: LoginView
	},
	{
	    path: "/signup",
	    name: "Signup",
	    component: SignupView
	}
    ],
});

export default router;

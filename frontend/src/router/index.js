import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/Home.vue"
import LoginView from "../views/Login.vue"
import SignupView from "../views/Signup.vue"

import MyBlogsView from "../views/my/Blogs.vue"
import CreateBlog from "../views/my/CreateBlog.vue"
import EditBlog from "../views/my/EditBlog.vue"

import auth from "../logic/auth"

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
	},
	{
	    path: "/my/blogs",
	    name: "My Blogs",
	    component: MyBlogsView
	},
	{
	    path: "/my/blogs/create",
	    name: "Create Blog",
	    component: CreateBlog
	},
	{
	    path: "/my/blogs/:id/edit",
	    name: "Edit Blog",
	    component: EditBlog
	}
    ],
});

router.beforeEach (async (to) => {
    const authenticated = auth.is_user_loggedin ()

    if (to.path.includes ("/my") && !authenticated)
	return "/login"

    if ((to.path.includes ("/login") || to.path.includes ("/signup")) && authenticated)
	return "/"
})

export default router;

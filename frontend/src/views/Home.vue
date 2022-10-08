<template>
    <!-- <h1>Look at this cool Home page!</h1>
	 <p>Earn money creating blogs, writing posts and books!</p>
	 <ul v-if="!is_user_loggedin">
	 <li>
	 <router-link to="/login">Login</router-link>
	 </li>
	 <li>
	 <router-link to="/signup">Signup</router-link>
	 </li>
	 </ul>
	 <ul v-else>
	 <li>
	 <router-link to="/my/blogs">My Blogs</router-link>
	 </li>
	 </ul> -->
</template>

<script>
 import auth from "../logic/auth"

 export default {
     name: "Home",
     computed: {
	 is_user_loggedin () {
	     return auth.is_user_loggedin ()
	 }
     }
 }
</script>

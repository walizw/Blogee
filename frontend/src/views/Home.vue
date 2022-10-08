<template>
    <section class="section banner overflow-hidden">
	<div class="container">
            <div class="row">
		<div class="col-lg-9 col-md-11 mx-auto text-center position-relative">
		    <h1 class="text-dark mb-0">
			{{$t ("lain quote")}}
		    </h1>
		    <WaveIcon />
		</div>
            </div>
	</div>
    </section>
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

 import WaveIcon from "../components/icons/WaveIcon.vue"

 export default {
     name: "Home",
     components: {
	 WaveIcon
     },
     computed: {
	 is_user_loggedin () {
	     return auth.is_user_loggedin ()
	 }
     }
 }
</script>

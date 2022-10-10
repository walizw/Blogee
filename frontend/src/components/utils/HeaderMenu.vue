<template>
    <ul class="navbar-nav mx-auto">
	<li :class="`nav-item` + ($route.path == elm.url ? ' active' : '')"
	    :key="elm.id" v-for="elm in menu">
	    <router-link class="nav-link" :to="elm.url"
			 v-if="!('requiresAuth' in elm) || 'requiresAuth' in elm && elm.requiresAuth && loggedin || 'requiresAuth' in elm && !elm.requiresAuth && !loggedin">
		{{elm.name}}
	    </router-link>
	</li>
    </ul>
</template>

<script>
 import auth from "@/logic/auth"

 export default {
     name: "HeaderMenu",
     props: {
	 menu: Array
     },
     computed: {
	 loggedin () {
	     return auth.is_user_loggedin ()
	 }
     }
 }
</script>

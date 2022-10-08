<template>
    <ul class="navbar-nav mx-auto">
	<li class="nav-item" :key="elm.id" v-for="elm in menu">
	    <router-link class="nav-link" :to="elm.url">
		{{elm.name}}
	    </router-link>
	</li>
    </ul>
</template>

<script>
 export default {
     name: "HeaderMenu",
     props: {
	 menu: Array
     }
 }
</script>

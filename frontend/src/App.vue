<template>
    <Header />
    <RouterView :user_id="user_id" />
</template>

<script>
 import auth from "./logic/auth"

 import Header from "./components/Header.vue"

 export default {
     name: "App",
     components: {
	 Header
     },
     data () {
	 return {
	     user_id: -1
	 }
     },
     created () {
	 this.user_id = auth.get_user_id ()
     }
 }
</script>

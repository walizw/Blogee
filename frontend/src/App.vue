<template>
  <RouterView :user_id="user_id" />
</template>

<script>
 import auth from "./logic/auth"

 export default {
     name: "App",
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

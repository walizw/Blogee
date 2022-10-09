<template>
    
</template>

<script>
 import auth from "../../logic/auth"

 export default {
     name: "Logout",
     created () {
	 auth.logout ()
	 this.$router.go ("/login")
     }
 }
</script>

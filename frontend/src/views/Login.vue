<template>
    <h1>Log Into your Blogee account!</h1>
    <form @submit="submit">
	<div>
	    <label>Username: </label>
	    <input v-model="username" type="text" placeholder="Username"/>
	</div>
	<div>
	    <label>Password: </label>
	    <input v-model="password" type="password" placeholder="Password" />
	</div>
	<input type="submit" value="Log In!"/>
    </form>
    <p v-if="error">{{error}}</p>
</template>

<script>
 import auth from "../logic/auth"

 export default {
     name: "Login",
     data () {
	 return {
	     username: "",
	     password: "",
	     error: null
	 }
     },
     methods: {
	 async submit (e) {
	     this.error = null
	     e.preventDefault ()

	     let response = await auth.login_user (this.username, this.password)
	     if (response)
	     {
		 if (response.success)
		     this.$router.go ("/")
		 
		 if (response.error)
		     this.error = response.error
	     }
	 }
     }
 }
</script>

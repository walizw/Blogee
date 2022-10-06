<template>
    <h1>Signup</h1>
    <form @submit="submit">
	<div>
	    <label>Username: </label>
	    <input type="text" placeholder="Username" v-model="username" />
	</div>
	<div>
	    <label>Email: </label>
	    <input type="email" v-model="email" placeholder="Email address" />
	</div>
	<div>
	    <label>Password: </label>
	    <input type="password" v-model="password1" placeholder="Password" />
	</div>
	<div>
	    <label>Repeat Your Password: </label>
	    <input type="password" v-model="password2" placeholder="Repeat your password" />
	</div>
	<input type="Submit" value="Sign Up!"/>
    </form>
    <p v-if="error">{{error}}</p>
</template>

<script>
 import auth from "../logic/auth"

 export default {
     name: "Signup",
     data () {
	 return {
	     username: "",
	     email: "",
	     password1: "",
	     password2: "",
	     error: ""
	 }
     },
     methods: {
	 async submit (e) {
	     e.preventDefault ()

	     if (this.password1 != this.password2)
	     {
		 this.error = "The entered passwords don't match"
		 return
	     }

	     let response = await auth.register_user (this.username,
						      this.email,
						      this.password1)

	     if (response) {
		 if (response.success)
		     this.$router.push ("/login")

		 if (response.error)
		     this.error = response.error
	     }
	 }
     }
 }
</script>

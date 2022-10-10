<template>
    <PageHeader />

    <section>
	<div class="container">
            <div class="row justify-content-center">
		<div class="col-lg-10">
		    <div class="content">
			<h3>{{$t ("Create an account in Blogee")}}</h3>

			<div class="alert alert-danger" role="alert"
			     v-if="error">
			    <h4 class="alert-heading">
				{{$t ("There's been an error")}}
			    </h4>
			    <p>{{$t ("signup_error_msg")}}</p>
			</div>

			<form @submit="submit">
			    <div class="mb-3">
				<label for="username">{{$t ("Username")}}:</label>
				<input v-model="username" type="text" class="form-control" />
			    </div>
			    <div class="mb-3">
				<label for="email">{{$t ("Email")}}:</label>
				<input v-model="email" type="email" class="form-control" />
			    </div>
			    <div class="row">
				<div class="col">
				    <div class="mb-3">
					<label for="password">{{$t ("Password")}}:</label>
					<input v-model="password1" type="password" class="form-control" />
				    </div>
				</div>
				<div class="col">
				    <div class="mb-3">
					<label for="password1">{{$t ("Repeat your password")}}:</label>
					<input v-model="password2" type="password" class="form-control" />
				    </div>
				</div>
			    </div>

			    <button class="btn btn-primary" type="submit">
				{{$t ("Signup")}}
			    </button>
			</form>
		    </div>
		</div>
            </div>
	</div>
    </section>
</template>

<script>
 import auth from "../logic/auth"

 import PageHeader from "../components/utils/PageHeader.vue"

 export default {
     name: "Signup",
     components: {
	 PageHeader
     },
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

<template>
    <PageHeader />

    <section>
	<div class="container">
            <div class="row justify-content-center">

		<div class="col-lg-10">
		    <div class="content">
			<h3>{{$t ("Login to your Blogee Account")}}</h3>

			<div class="alert alert-danger" role="alert"
			     v-if="error">
			    <h4 class="alert-heading">
				{{$t ("There's been an error")}}
			    </h4>
			    <p>{{$t ("login_error_msg")}}</p>
			</div>

			<form @submit="submit">
			    <div class="mb-3">
				<label for="username">{{$t ("Username")}}:</label>
				<input v-model="username" type="text"
				       class="form-control" />
			    </div>
			    <div class="mb-3">
				<label for="password">{{$t ("Password")}}:</label>
				<input v-model="password" type="password"
						class="form-control" />
			    </div>

			    <button type="submit" class="btn btn-primary">
				{{$t ("Login")}}
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

 import PageHeader from "@/components/utils/PageHeader.vue"

 export default {
     name: "Login",
     components: {
	 PageHeader
     },
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

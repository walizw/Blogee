<template>
    <h1>Create your blog</h1>

    <form @submit="submit">
	<div>
	    <label>Name: </label>
	    <input type="text" placeholder="name" v-model="name" />
	</div>

	<div>
	    <label>About: </label>
	    <textarea cols="30" v-model="about" rows="10"></textarea>
	</div>

	<div>
	    <label>Header Image: </label>
	    <input type="file" ref="header_img" @change="changed_file" />
	</div>

	<input type="submit" value="Create!"/>
    </form>
    <p v-if="error">{{error}}</p>
</template>

<script>
 import blogs from "../../logic/blogs"

 export default {
     name: "CreateBlog",
     data () {
	 return {
	     name: "",
	     about: "",
	     header_img: "",
	     error: ""
	 }
     },
     methods: {
	 changed_file () {
	     this.header_img = this.$refs.header_img.files [0]
	 },
	 async submit (e) {
	     e.preventDefault ()

	     let form_data = new FormData ()
	     form_data.append ("name", this.name)
	     form_data.append ("about", this.about)
	     form_data.append ("header_img", this.header_img)
	     
	     let response = await blogs.create_blog (form_data)

	     if (response)
	     {
		 if (response.success)
		     this.$router.push ("/my/blogs")

		 this.error = response.error
	     }
	 }
     }
 }
</script>

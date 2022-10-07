<template>
    <h1>Edit blog</h1>
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

	<input type="submit" value="Update!"/>
    </form>
    <p v-if="success">Blog Updated Successfully!</p>
    <p v-if="error">{{error}}</p>
</template>

<script>
 import blogs from "../../logic/blogs"

 export default {
     name: "EditBlog",
     data () {
	 return {
	     name: "",
	     about: "",
	     header_img: "",
	     error: "",
	     success: false
	 }
     },
     async created () {
	 let blog_data = await blogs.get_blog (this.$route.params.id)

	 if (blog_data.error)
	 {
	     this.error = blog_data.error
	     return
	 }

	 this.name = blog_data.name
	 this.about = blog_data.about
     },
     methods: {
	 changed_file () {
	     this.header_img = this.$refs.header_img.files [0] // Only one file
	 },
	 async submit (e) {
	     e.preventDefault ()

	     this.success = false
	     this.error = ""

	     let form_data = new FormData ()
	     form_data.append ("name", this.name)
	     form_data.append ("about", this.about)
	     form_data.append ("header_img", this.header_img)

	     let response = await blogs.update_blog (this.$route.params.id, form_data)

	     if (response)
	     {
		 if (response.success)
		 {
		     this.success = true
		     return
		 }

		 if (response.error)
		     this.error = response.error
	     }
	 }
     }
 }
</script>

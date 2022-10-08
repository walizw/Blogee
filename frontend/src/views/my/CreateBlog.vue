<template>
    <h1>Create your blog</h1>

    <form @submit="submit">
	<div>
	    <label>Name: </label>
	    <input type="text" placeholder="name" v-model="name"
		   required/>
	</div>

	<div>
	    <label>About: </label>
	    <textarea cols="30" v-model="about" rows="10"
		      required></textarea>
	</div>

	<div>
	    <label>Icon: </label>
	    <input type="file" ref="icon" @change="changed_file" />
	</div>

	<div>
	    <label>Header Image: </label>
	    <input type="file" ref="header_img" @change="changed_file" />
	</div>

	<div>
	    <label>Language: </label>
	    <select v-model="language" required>
		<option value="en">English</option>
		<option value="es">Spanish</option>
		<option value="fr">French</option>
		<option value="it">Italian</option>
		<option value="jp">Japanese</option>
		<option value="kr">Korean</option>
		<option value="zh">Chinese</option>
		<option value="de">Deutsch</option>
	    </select>
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
	     icon_img: "",
	     header_img: "",
	     language: "",
	     error: ""
	 }
     },
     methods: {
	 changed_file () {
	     if (this.$refs.header_img.files)
		 this.header_img = this.$refs.header_img.files [0]

	     if (this.$refs.icon.files)
		 this.icon_img = this.$refs.icon.files [0]
	 },
	 async submit (e) {
	     e.preventDefault ()

	     let form_data = new FormData ()
	     form_data.append ("name", this.name)
	     form_data.append ("about", this.about)
	     form_data.append ("icon", this.icon_img)
	     form_data.append ("header_img", this.header_img)
	     form_data.append ("lang", this.language)
	     
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

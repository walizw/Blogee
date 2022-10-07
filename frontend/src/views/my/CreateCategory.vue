<template>
    <h1>Create category</h1>

    <form @submit="submit">
	<div>
	    <label>Name: </label>
	    <input type="text" placeholder="Name" v-model="name" required />
	</div>

	<div>
	    <label>Topic: </label>
	    <select v-model="parent" required>
		<option value="0">Health & Fitness</option>
		<option value="1">Lifestyle</option>
		<option value="2">News</option>
		<option value="3">Sports</option>
		<option value="4">Technology</option>
		<option value="5">Political</option>
		<option value="6">DIY</option>
		<option value="7">Videogames</option>
		<option value="8">History</option>
		<option value="9">Arts</option>
	    </select>
	</div>

	<div>
	    <label>About: </label>
	    <textarea cols="30" rows="10" v-model="about"></textarea>
	</div>

	<div>
	    <label>Icon: </label>
	    <input type="file" @change="changed_file" ref="icon" required />
	</div>

	<input type="submit" value="Create!"/>
    </form>
    <p v-if="error">{{error}}</p>
</template>

<script>
 import blogs from "../../logic/blogs"

 export default {
     name: "CategoryCreate",
     data () {
	 return {
	     name: "",
	     parent: -1,
	     about: "",
	     icon_img: "",
	     error: ""
	 }
     },
     methods: {
	 changed_file () {
	     this.icon_img = this.$refs.icon.files [0]
	 },
	 async submit (e) {
	     e.preventDefault ()

	     let blog_id = this.$route.params.id

	     let form_data = new FormData ()
	     form_data.append ("name", this.name)
	     form_data.append ("blog", blog_id)
	     form_data.append ("parent_id", this.parent)
	     form_data.append ("about", this.about)
	     form_data.append ("icon", this.icon_img)

	     let response = await blogs.create_blog_category (blog_id, form_data)

	     if (response) {
		 if (response.success)
		     this.$router.push ("/my/blogs")

		 this.error = response.error
	     }
	 }
     }
 }
</script>

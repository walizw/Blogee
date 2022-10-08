<template>
    <h1>New Post</h1>

    <form @submit="submit">
	<div>
	    <label>Name: </label>
	    <input v-model="name" type="text" placeholder="Name"
		   required/>
	</div>

	<div>
	    <label>Content: </label>
	    <textarea cols="30" v-model="content" rows="10"
		      required></textarea>
	</div>

	<div>
	    <label>Thumbnail: </label>
	    <input type="file" @change="changed_file" ref="thumb"
		   required/>
	</div>

	<div>
	    <label>Draft: </label>
	    <input type="checkbox" v-model="draft" />
	</div>

	<div>
	    <label>Tags: </label>
	    <input type="text" placeholder="Tags (separated by a comma ',')"
		   v-model="tags" />
	</div>

	<div>
	    <label>Category: </label>
	    <select v-model="category" required>
		<option :key="cat.id" v-for="cat in categories"
			:value="cat.id">
		    {{cat.name}}
		</option>
	    </select>
	</div>

	<div>
	    <input type="submit" value="Create!" />
	</div>
    </form>

    <p v-if="error">{{error}}</p>
</template>

<script>
 import blogs from "../../logic/blogs"
 import posts from "../../logic/posts"

 export default {
     name: "NewPost",
     data () {
	 return {
	     name: "",
	     content: "",
	     thumb: "",
	     draft: false,
	     tags: "",
	     category: -1,
	     categories: [],
	     error: ""
	 }
     },
     methods: {
	 changed_file () {
	     this.thumb = this.$refs.thumb.files [0]
	 },
	 async submit (e) {
	     e.preventDefault ()

	     this.error = ""

	     let form_data = new FormData ()
	     form_data.append ("name", this.name)
	     form_data.append ("blog", this.$route.params.id)
	     form_data.append ("content", this.content)
	     form_data.append ("thumbnail", this.thumb)
	     form_data.append ("tags", this.tags)
	     form_data.append ("category", this.category)

	     let response = await posts.post_create (form_data)

	     if (response) {
		 if (response.success)
		     this.$router.push ("/my/blogs")

		 this.error = response.error
	     }
	 }
     },
     async created () {
	 this.categories = await blogs.get_blog_categories (this.$route.params.id)
     }
 }
</script>

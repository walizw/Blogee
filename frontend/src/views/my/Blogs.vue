<template>
    <h1>My Blogs</h1>
    <ul>
	<li>
	    <router-link to="/my/blogs/create">
		Create Blog
	    </router-link>
	</li>
    </ul>
    <div v-if="blogs.length === 0">
	You have no blogs! Create one :D
    </div>
    <div v-else>
	<div :key="blog.id" v-for="blog in blogs">
	    <p>
		{{blog.name}} --
		<router-link :to="`/my/blogs/${blog.id}/edit`">Edit</router-link> --
		<router-link :to="`/my/blogs/${blog.id}/delete`">Delete</router-link>
	    </p>
	    <p>
		Categories: --
		<router-link :to="`/my/blogs/${blog.id}/cat_create`">Create</router-link>
	    </p>
	    <p v-if="blog.categories && blog.categories.length === 0">
		This blog has no categories, you can create some or use the
		default ones.
	    </p>
	    <ul v-else>
		<li :key="cat.id" v-for="cat in blog.categories">
		    {{cat.name}} --
		    <router-link :to="`/my/category/${cat.id}/edit`">Edit</router-link> --
		    <router-link :to="`/my/category/${cat.id}/delete`">Delete</router-link>
		</li>
	    </ul>
	</div>
    </div>
</template>

<script>
 import auth from "../../logic/auth"
 import blogs from "../../logic/blogs"

 export default {
     name: "Blogs",
     data () {
	 return {
	     blogs: []
	 }
     },
     async created () {
	 this.blogs = await blogs.get_user_blogs (auth.get_user_id ())

	 for (let i = 0; i < this.blogs.length; i++) {
	     let categories = await blogs.get_blog_categories (this.blogs[i].id)
	     this.blogs [i].categories = categories
	 }
     }
 }
</script>

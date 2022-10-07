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
	<p :key="blog.id" v-for="blog in blogs">
	    {{blog.name}} --
	    <router-link :to="`/my/blogs/${blog.id}/edit`">Edit</router-link> --
	    <router-link :to="`/my/blogs/${blog.id}/delete`">Delete</router-link>
	</p>
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
     }
 }
</script>

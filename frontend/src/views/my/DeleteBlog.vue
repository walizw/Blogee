<template>
    <p v-if="error">{{error}}</p>
</template>

<script>
 import blogs from "../../logic/blogs"

 export default {
     name: "DeleteBlog",
     data () {
	 return {
	     error: ""
	 }
     },
     async created () {
	 let response = await blogs.delete_blog (this.$route.params.id)

	 if (response) {
	     if (response.success)
		 this.$router.push ("/my/blogs")

	     this.error = response.error
	 }
     }
 }
</script>

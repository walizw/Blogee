<template>
    <p v-if="error">{{error}}</p>
</template>

<script>
 import category from "../../logic/category"

 export default {
     name: "DeleteCategory",
     data () {
	 return {
	     error: ""
	 }
     },
     async created () {
	 let response = await category.delete_category (this.$route.params.id)

	 if (response) {
	     if (response.success)
		 // TODO: Go to this category's blog page
		 this.$router.push ("/my/blogs")

	     this.error = response.error
	 }
     }
 }
</script>

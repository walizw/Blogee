<template>
    <PageHeader />
    <div class="container">
	<div class="row g-4 justify-content-center text-center mb-4">
	    <h3>Blogs</h3>
	    <CategoryBox size="4" link="/my/blogs/create"
			 icon="ti-new-section" title="Create Blog"
			 subtitle="create_blog_subtitle" />
	    <CategoryBox size="4" :key="blog.id" v-for="blog in blogs"
			 :link="`/my/blog/${blog.id}`" :title="blog.name"
			 icon="ti-tools" subtitle="Edit Blog" />
	</div>
    </div>
</template>

<script>
 import auth from "../../logic/auth"
 import blogs from "../../logic/blogs"

 import PageHeader from "@/components/utils/PageHeader.vue"
 import CategoryBox from "@/components/utils/CategoryBox.vue"

 export default {
     name: "Blogs",
     components: {
	 PageHeader,
	 CategoryBox
     },
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

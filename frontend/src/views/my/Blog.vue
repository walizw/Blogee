<template>
    <PageHeader />
    <div class="container">
	<div class="row g-4 justify-content-center text-center mb-4">
	    <h3>{{$t ("Blog Settings")}}</h3>

	    <CategoryBox size="4" :link="`/my/blogs/${blog_id}/delete`"
			 icon="ti-trash" title="Delete Blog"
			 subtitle="delete_blog_subtitle" />
	    <CategoryBox size="4" :link="`/my/blogs/${blog_id}/edit`"
			 icon="ti-edit-circle" title="Update Blog"
			 subtitle="update_blog_subtitle" />
	</div>
	<div class="row g-4 justify-content-center text-center mb-4">
	    <h3>{{$t ("Categories")}}</h3>

	    <CategoryBox size="4" :link="`/my/blogs/${blog_id}/cat_create`"
			 icon="ti-new-section" title="Create Category"
			 subtitle="create_cat_subtitle" />

	    <CategoryBox size="4" :key="cat.id"
			 v-for="cat in blog_data.categories"
			 :link="`/my/category/${cat.id}/edit`"
			 :title="cat.name" icon="ti-writing"
			 subtitle="category_edit_subtitle" />
	</div>
	<div class="row g-4 justify-content-center mb-4">
	    <h3 class="text-center">{{$t ("Posts")}}</h3>

	    <div class="archive-block">
		<router-link class="float-end"
			     :to="`/my/blogs/${blog_id}/new_post`">
		    {{$t ("New Post")}}
		</router-link>
		<ArchivePostItem :key="post.id" v-for="post in blog_data.posts"
				 :name="post.name" :date="post.date"
				 :link="`/my/post/${post.id}/edit`" />
	    </div>
	</div>
    </div>
</template>

<script>
 import auth from "../../logic/auth"
 import blogs from "../../logic/blogs"

 import PageHeader from "@/components/utils/PageHeader.vue"
 import CategoryBox from "@/components/utils/CategoryBox.vue"
 import ArchivePostItem from "@/components/utils/ArchivePostItem.vue"

 export default {
     name: "Blog",
     data () {
	 return {
	     blog_data: Object
	 }
     },
     components: {
	 PageHeader,
	 CategoryBox,
	 ArchivePostItem
     },
     async created () {
	 this.blog_data = await blogs.get_blog (this.blog_id)
	 this.blog_data.categories = await blogs.get_blog_categories (this.blog_id)
	 this.blog_data.posts = await blogs.get_blog_posts (this.blog_id)
     },
     computed: {
	 blog_id () {
	     return this.$route.params.id
	 }
     }
 }
</script>

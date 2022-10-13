<template>
    <PageHeader />

    <section>
	<div class="container">
            <div class="row justify-content-center">
		<div class="col-lg-12">
                    <div class="content">

			<div class="alert alert-danger" role="alert"
			     v-if="error">
			    <h4 class="alert-heading">
				{{$t ("There's been an error")}}
			    </h4>
			    <p>{{$t ("edit_post_error_msg")}}</p>
			</div>

			<form @submit="submit">
			    <div class="mb-3">
				<label>{{$t ("Post Name")}}:</label>
				<input v-model="name" type="text"
						class="form-control" required />
			    </div>

			    <div class="mb-3">
				<label>{{$t ("Post Content")}}:</label>
				<EditorJS @save="save_editor"
					  style="border: 1px solid #ababab; padding: 10px;"
					  :data="content" />
			    </div>

			    <div class="mb-3">
				<label>{{$t ("Post Thumbnail")}}:</label>
				<input type="file" @change="changed_file"
				       class="form-control" ref="thumb" />
			    </div>

			    <div class="mb-0 form-check form-switch">
				<label class="form-check-label"
				       for="draft-check">
				    {{$t ("Draft")}}
				</label>
				<input type="checkbox" v-model="draft"
				       class="form-check-input"
				       id="draft-check" />
			    </div>

			    <div class="mb-3">
				<label>{{$t ("Tags")}}:</label>
				<input v-model="tags" type="text"
						class="form-control" />
				<p class="form-text">{{$t ("post_tags_text")}}</p>
			    </div>

			    <div class="mb-3">
				<label>{{$t ("Category")}}:</label>
				<select class="form-control" v-model="category">
				    <option :key="cat.id" v-for="cat in categories"
					    :value="cat.id">
					{{cat.name}}
				    </option>
				</select>
			    </div>

			    <button type="submit" class="btn btn-primary">
				{{$t ("Edit Post")}}
			    </button>
			</form>
			
		    </div>
		</div>
            </div>
	</div>
    </section>
</template>

<script>
 import posts from "@/logic/posts"
 import blogs from "@/logic/blogs"

 import PageHeader from "@/components/utils/PageHeader.vue"
 import EditorJS from "@/components/utils/EditorJS.vue"

 export default {
     name: "EditPost",
     components: {
	 PageHeader,
	 EditorJS
     },
     data () {
	 return {
	     blog_id: -1,
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
	 save_editor (cnt) {
	     this.content = JSON.stringify (cnt)
	 },
	 async submit (e) {
	     e.preventDefault ()

	     this.error = ""

	     let form_data = new FormData ()
	     form_data.append ("name", this.name)
	     form_data.append ("blog", this.blog_id)
	     form_data.append ("content", this.content)
	     form_data.append ("tags", this.tags)
	     form_data.append ("category", this.category)
	     form_data.append ("draft", this.draft)

	     if (this.thumb)
		 form_data.append ("thumbnail", this.thumb)

	     let response = await posts.post_update (this.$route.params.id, form_data)

	     if (response) {
		 if (response.success)
		     this.$router.push (`/my/blog/${this.blog_id}`)

		 this.error = response.error
	     }
	 }
     },
     async created () {
	 let response = await posts.post_get_info (this.$route.params.id)

	 if (response.error)
	     this.error = response.error

	 this.blog_id = response.blog
	 this.name = response.name
	 this.content = response.content
	 this.draft = response.draft
	 this.tags = response.tags
	 this.category = response.category

	 this.categories = await blogs.get_blog_categories (this.blog_id)
     }
 }
</script>

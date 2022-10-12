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
			    <p>{{$t ("create_post_error_msg")}}</p>
			</div>

			<form @submit="submit">
			    <div class="mb-3">
				<label>{{$t ("Post Name")}}:</label>
				<input v-model="name" type="text"
				       class="form-control" required/>
			    </div>

			    <div class="mb-3">
				<label>{{$t ("Post Content")}}:</label>
				<EditorJS @save="save_editor"
					  style="border: 1px solid #ababab; padding: 10px;" />
			    </div>

			    <div class="mb-3">
				<label>{{$t ("Post Thumbnail")}}:</label>
				<input type="file" @change="changed_file"
				       class="form-control" ref="thumb" required/>
			    </div>

			    <div class="mb-0 form-check form-switch">
				<label class="form-check-label" for="draft-check">
				    {{$t ("Draft")}}
				</label>
				<input type="checkbox" v-model="draft"
				       class="form-check-input"
				       id="draft-check" />
			    </div>

			    <div class="mb-3">
				<label>{{$t ("Tags")}}:</label>
				<input type="text" v-model="tags"
				       class="form-control" required />
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
				{{$t ("Post!")}}
			    </button>
			</form>
			
		    </div>
		</div>
            </div>
	</div>
    </section>
    
    <!-- <h1>New Post</h1>

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

	 <p v-if="error">{{error}}</p> -->
</template>

<script>
 import blogs from "../../logic/blogs"
 import posts from "../../logic/posts"

 import PageHeader from "@/components/utils/PageHeader.vue"
 import EditorJS from "@/components/utils/EditorJS.vue"

 export default {
     name: "NewPost",
     components: {
	 PageHeader,
	 EditorJS
     },
     data () {
	 return {
	     name: "",
	     content: "",
	     thumb: "",
	     draft: false,
	     tags: "",
	     category: -1,
	     categories: [],
	     error: "",
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

	     console.log (this.content)
	     
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
		     this.$router.push (`/my/blog/${this.$route.params.id}`)

		 this.error = response.error
	     }
	 }
     },
     async created () {
	 this.categories = await blogs.get_blog_categories (this.$route.params.id)
     }
 }
</script>

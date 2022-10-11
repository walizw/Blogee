<template>
    <PageHeader />

    <section>
	<div class="container">
            <div class="row justify-content-center">
		<div class="col-lg-10">
                    <div class="content">

			<div class="alert alert-danger" role="alert"
			     v-if="error">
			    <h4 class="alert-heading">
				{{$t ("There's been an error")}}
			    </h4>
			    <p>{{$t ("edit_blog_error_msg")}}</p>
			</div>

			<form @submit="submit">
			    <div class="mb-3">
				<label>{{$t ("Name")}}:</label>
				<input v-model="name" type="text" class="form-control" required/>
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("About Blog")}}:</label>
				<textarea cols="30" rows="10" v-model="about"
					  class="form-control" required>
				</textarea>
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("Icon Image")}}:</label>
				<input type="file" ref="icon_img"
				       @change="changed_file"
				       class="form-control" />
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("Header Image")}}:</label>
				<input type="file" ref="header_img"
				       @change="changed_file"
				       class="form-control" />
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("Language")}}:</label>
				<select v-model="language" class="form-control"
					required>
				    <option :key="lang.id" :value="lang.code"
					    v-for="lang in languages">
					{{$t (lang.name)}}
				    </option>
				</select>
			    </div>

			    <button class="btn btn-primary" type="submit">
				{{$t ("Edit Blog")}}
			    </button>
			</form>
			
		    </div>
		</div>
            </div>
	</div>
    </section>
</template>

<script>
 import blogs from "../../logic/blogs"
 import config from "../../logic/config"

 import PageHeader from "@/components/utils/PageHeader.vue"

 export default {
     name: "EditBlog",
     components: {
	 PageHeader
     },
     data () {
	 return {
	     name: "",
	     about: "",
	     icon_img: "",
	     header_img: "",
	     language: "",
	     error: "",
	     success: false
	 }
     },
     computed: {
	 languages () {
	     return config.LANGUAGES
	 }
     },
     async created () {
	 let blog_data = await blogs.get_blog (this.$route.params.id)

	 if (blog_data.error)
	 {
	     this.error = blog_data.error
	     return
	 }

	 this.name = blog_data.name
	 this.about = blog_data.about
	 this.language = blog_data.lang
     },
     methods: {
	 changed_file () {
	     if (this.$refs.header_img.files [0])
		 this.header_img = this.$refs.header_img.files [0] // Only one file

	     if (this.$refs.icon_img.files [0])
		 this.icon_img = this.$refs.icon_img.files [0]
	 },
	 async submit (e) {
	     e.preventDefault ()

	     this.success = false
	     this.error = ""

	     let form_data = new FormData ()
	     form_data.append ("name", this.name)
	     form_data.append ("about", this.about)
	     form_data.append ("lang", this.language)

	     if (this.header_img != "")
		 form_data.append ("header_img", this.header_img)

	     if (this.icon_img != "")
		 form_data.append ("icon_img", this.icon_img)

	     let response = await blogs.update_blog (this.$route.params.id, form_data)

	     if (response)
	     {
		 if (response.success)
		 {
		     this.$router.push (`/my/blog/${this.$route.params.id}`)
		     return
		 }

		 if (response.error)
		     this.error = response.error
	     }
	 }
     }
 }
</script>

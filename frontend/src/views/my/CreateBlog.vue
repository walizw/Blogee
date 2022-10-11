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
			    <p>{{$t ("create_blog_error_msg")}}</p>
			</div>

			<form @submit="submit">
			    <div class="mb-3">
				<label>{{$t ("Name")}}:</label>
				<input v-model="name" type="text" required
				       class="form-control" />
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("About Blog")}}: </label>
				<textarea cols="30" rows="10" v-model="about"
						required class="form-control"></textarea>
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("Icon Image")}}: </label>
				<input type="file" ref="icon"
				       @change="changed_file"
				       class="form-control" />
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("Header Image")}}: </label>
				<input type="file" ref="header_img"
				       @change="changed_file"
				       class="form-control" />
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("Language")}}: </label>
				<select v-model="language"
					class="form-control" required>
				    <option :key="lang.id"
					    v-for="lang in languages"
					    :value="lang.code">
					{{lang.name}}
				    </option>
				</select>
			    </div>

			    <button class="btn btn-primary" type="submit">
				{{$t ("Create Blog")}}
			    </button>
			</form>
			
		    </div>
		</div>
		
	    </div>
	</div>
    </section>
    <!-- <h1>Create your blog</h1>

	 <form @submit="submit">
	 <div>
	 <label>Name: </label>
	 <input type="text" placeholder="name" v-model="name"
	 required/>
	 </div>

	 <div>
	 <label>About: </label>
	 <textarea cols="30" v-model="about" rows="10"
	 required></textarea>
	 </div>

	 <div>
	 <label>Icon: </label>
	 <input type="file" ref="icon" @change="changed_file" />
	 </div>

	 <div>
	 <label>Header Image: </label>
	 <input type="file" ref="header_img" @change="changed_file" />
	 </div>

	 <div>
	 <label>Language: </label>
	 <select v-model="language" required>
	 <option :key="lang.id" v-for="lang in languages"
	 :value="lang.code">
	 {{lang.name}}
	 </option>
	 </select>
	 </div>

	 <input type="submit" value="Create!"/>
	 </form>
	 <p v-if="error">{{error}}</p> -->
</template>

<script>
 import blogs from "../../logic/blogs"
 import config from "../../logic/config"

 import PageHeader from "@/components/utils/PageHeader.vue"

 export default {
     name: "CreateBlog",
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
	     error: ""
	 }
     },
     computed: {
	 languages () {
	     return config.LANGUAGES
	 }
     },
     methods: {
	 changed_file () {
	     if (this.$refs.header_img.files)
		 this.header_img = this.$refs.header_img.files [0]

	     if (this.$refs.icon.files)
		 this.icon_img = this.$refs.icon.files [0]
	 },
	 async submit (e) {
	     e.preventDefault ()

	     let form_data = new FormData ()
	     form_data.append ("name", this.name)
	     form_data.append ("about", this.about)
	     form_data.append ("icon", this.icon_img)
	     form_data.append ("header_img", this.header_img)
	     form_data.append ("lang", this.language)
	     
	     let response = await blogs.create_blog (form_data)

	     if (response)
	     {
		 if (response.success)
		     this.$router.push ("/my/blogs")

		 this.error = response.error
	     }
	 }
     }
 }
</script>

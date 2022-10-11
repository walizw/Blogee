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
			    <p>{{$t ("create_category_error_msg")}}</p>
			</div>

			<form @submit="submit">
			    <div class="mb-3">
				<label>{{$t ("Name")}}:</label>
				<input type="text" v-model="name"
				       class="form-control" required />
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("Topic")}}:</label>
				<select v-model="parent" class="form-control"
						 required>
				    <option :key="cat.id" :value="cat.id"
					    v-for="cat in categories">
					{{$t (cat.name)}}
				    </option>
				</select>
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("About Category")}}:</label>
				<textarea cols="30" rows="10" v-model="about"
						class="form-control">
				</textarea>
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("Icon Image")}}:</label>
				<input type="file" @change="changed_file"
				       ref="icon" class="form-control"
				       required />
			    </div>

			    <input type="submit" class="btn btn-primary"
				   :value="$t ('Create Category')"/>
			</form>
			
		    </div>
		</div>
	    </div>
	</div>
    </section>
    <!-- <h1>Create category</h1>

	 <form @submit="submit">
	 <div>
	 <label>Name: </label>
	 <input type="text" placeholder="Name" v-model="name" required />
	 </div>

	 <div>
	 <label>Topic: </label>
	 <select v-model="parent" required>
	 <option :key="cat.id" v-for="cat in categories"
	 :value="cat.id">
	 {{cat.name}}
	 </option>
	 </select>
	 </div>

	 <div>
	 <label>About: </label>
	 <textarea cols="30" rows="10" v-model="about"></textarea>
	 </div>

	 <div>
	 <label>Icon: </label>
	 <input type="file" @change="changed_file" ref="icon" required />
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
     name: "CategoryCreate",
     components: {
	 PageHeader
     },
     data () {
	 return {
	     name: "",
	     parent: -1,
	     about: "",
	     icon_img: "",
	     error: ""
	 }
     },
     computed: {
	 categories () {
	     return config.CATEGORIES
	 }
     },
     methods: {
	 changed_file () {
	     this.icon_img = this.$refs.icon.files [0]
	 },
	 async submit (e) {
	     e.preventDefault ()

	     let blog_id = this.$route.params.id

	     let form_data = new FormData ()
	     form_data.append ("name", this.name)
	     form_data.append ("blog", blog_id)
	     form_data.append ("parent_id", this.parent)
	     form_data.append ("about", this.about)
	     form_data.append ("icon", this.icon_img)

	     let response = await blogs.create_blog_category (blog_id, form_data)

	     if (response) {
		 if (response.success)
		     this.$router.push ("/my/blog/" + blog_id)

		 this.error = response.error
	     }
	 }
     }
 }
</script>

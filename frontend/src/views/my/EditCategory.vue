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
			    <p>{{$t ("edit_cat_error_msg")}}</p>
			</div>

			<form @submit="submit">
			    <div class="mb-3">
				<label>{{$t ("Name")}}: </label>
				<input v-model="name" type="text"
				       class="form-control" />
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("About Category")}}:</label>
				<textarea cols="30" rows="10" v-model="about"
					  class="form-control"></textarea>
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("Topic")}}:</label>
				<select v-model="topic" class="form-control">
				    <option :key="cat.id" :value="cat.id"
					    v-for="cat in categories">
					{{$t (cat.name)}}
				    </option>
				</select>
			    </div>
			    
			    <div class="mb-3">
				<label>{{$t ("Icon Image")}}:</label>
				<input type="file" ref="icon"
				       class="form-control"
				       @change="changed_file" />
			    </div>

			    <!-- <div class="mb-3">
				 <button type="submit" class="btn btn-primary">
				 {{$t ("Edit Category")}}
				 </button>

				 <router-link class="btn btn-primary d-inline-block"
				 :to="`/my/category/${cat_id}/delete`">
				 {{$t ("Delete Category")}}
				 </router-link>
				 </div> -->

			    <div class="clearfix">
				<button type="submit" class="btn btn-primary float-start">
				    {{$t ("Edit Category")}}
				</button>

				<router-link class="btn btn-danger float-end"
					     :to="`/my/category/${cat_id}/delete`"
					     role="button">
				    {{$t ("Delete Category")}}
				</router-link>
			    </div>
			</form>
			
		    </div>
		</div>
            </div>
	</div>
    </section>
</template>

<script>
 import category from "../../logic/category"
 import config from "../../logic/config"

 import PageHeader from "@/components/utils/PageHeader.vue"

 export default {
     name: "EditCategory",
     data () {
	 return {
	     name: "",
	     topic: -1,
	     about: "",
	     icon: "",
	     error: ""
	 }
     },
     components: {
	 PageHeader
     },
     computed: {
	 categories () {
	     return config.CATEGORIES
	 },
	 cat_id () {
	     return this.$route.params.id
	 }
     },
     methods: {
	 changed_file () {
	     this.icon = this.$refs.icon.files [0]
	 },
	 async submit (e) {
	     e.preventDefault ()

	     let form_data = new FormData ()
	     form_data.append ("name", this.name)
	     form_data.append ("topic", this.topic)
	     form_data.append ("about", this.about)

	     if (this.icon)
		 form_data.append ("icon", this.icon)

	     let response = await category.category_update (
		 this.$route.params.id,
		 form_data
	     )

	     if (response) {
		 if (response.success)
		     this.$router.push ("/my/blogs")

		 this.error = response.error
	     }
	 }
     },
     async created () {
	 let response = await category.category_get_info (this.$route.params.id)

	 if (response.error)
	 {
	     this.error = response.error
	 }

	 this.name = response.name
	 this.topic = response.parent_id
	 this.about = response.about
     }
 }
</script>

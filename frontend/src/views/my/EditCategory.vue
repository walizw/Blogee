<template>
    <h1>Edit Category</h1>
    <form @submit="submit">
	<div>
	    <label>Name: </label>
	    <input type="text" placeholder="Name" v-model="name" />
	</div>

	<div>
	    <label>Topic: </label>
	    <select v-model="topic">
		<option :key="cat.id" v-for="cat in categories"
					     :value="cat.id">
		    {{cat.name}}
		</option>
	    </select>
	</div>

	<div>
	    <label>About: </label>
	    <textarea cols="30" v-model="about" rows="10"></textarea>
	</div>

	<div>
	    <label>Icon: </label>
	    <input type="file" @change="changed_file" ref="icon" />
	</div>

	<input type="submit" value="Update!"/>
    </form>
    <router-link :to="`/my/category/${cat_id}/delete`">
	Delete
    </router-link>
    <p v-if="error">{{error}}</p>
</template>

<script>
 import category from "../../logic/category"
 import config from "../../logic/config"

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

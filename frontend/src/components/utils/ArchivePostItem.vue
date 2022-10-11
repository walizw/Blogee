<template>
    <p class="archive-post-item">
	{{final_date.toDateString ()}}
	<span>•</span>
	<router-link :to="link">
	    {{name}}
	</router-link>
    </p>
</template>

<script>
 export default {
     name: "ArchivePostItem",
     props: {
	 date: String,
	 name: String,
	 link: String
     },
     computed: {
	 final_date () {
	     return new Date (this.date)
	 }
     }
 }
</script>

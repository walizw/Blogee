<template>
    <div class="search-block">
	<div data-toggle="search-close">
	    <span class="ti ti-x text-primary"></span>
	</div>

	<input v-model="query" type="text"
	       id="js-search-input"
	       :placeholder="$t ('Type to search...')"
	       aria-label="search-query"
	       @keyup.enter="submit" />
    </div>
</template>

<script>
 export default {
     name: "SearchBlock",
     data () {
	 return {
	     query: ""
	 }
     },
     methods: {
	 submit (e) {
	     e.preventDefault ()

	     alert (`TODO: search ${this.query}`)
	 }
     }
 }
</script>

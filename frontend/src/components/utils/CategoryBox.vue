<template>
    <div :class="`col-lg-${size} col-sm-6`">
	<router-link :to="link"
		     class="p-4 rounded bg-white d-block is-hoverable">
	    <span class="h3"><i :class="`ti ${icon}`"></i></span>
	    <span class="h4 mt-2 mb-3 d-block"> {{$t (title)}}</span>
	    <p v-if="subtitle">{{$t (subtitle)}}</p>
	</router-link>
    </div>
</template>

<script>
 export default {
     name: "CategoryBox",
     props: {
	 size: Number,
	 link: String,
	 icon: String,
	 title: String,
	 subtitle: String
     }
 }
</script>

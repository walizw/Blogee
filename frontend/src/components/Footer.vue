<template>
    <footer>
	<div class="container">
	    <div class="section">
		<div class="row justify-content-center align-items-center">
		    <div class="col-xl-6 col-lg-8 col-md-10">
			<div class="newsletter-block">
			    <h2 class="section-title text-center mb-4">
				{{$t ("footer msg")}}
			    </h2>
			</div>
		    </div>
		</div>
	    </div>
	    
	    <div class="pb-5">

		<div class="row g-2 g-lg-4 align-items-center">
		    <div class="col-lg-6 text-center text-lg-start">
			<p class="mb-0 copyright-text content">
			    &copy; 2022 Blogee. 
			</p>
		    </div>
		</div>
		
	    </div>
	</div>
    </footer>
</template>

<script>
 export default {
     name: "Footer"
 }
</script>

<template>
    <div class="header-height-fix"></div>
    <header class="header-nav">
	<div class="container">
	    <div class="row">
		<div class="col-12">

		    <nav class="navbar navbar-expand-lg navbar-light p-0">
			<router-link to="/"
				     class="navbar-brand font-weight-bold mb-0"
				     title="Blogee">
			    <img class="img-fluid" width="110" height="35"
				 src="/images/logo.png" alt="Blogee" />
			</router-link>
		    </nav>
		    
		</div>
	    </div>
	</div>
    </header>
</template>

<script>
 export default {
     name: "Header"
 }
</script>

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

			<button class="search-toggle d-inline-block d-lg-none ms-auto me-1 me-sm-3"
				data-toggle="search"
				:aria-label="$t ('Search Toggle')">
			    <span>{{$t ("Search")}}</span>
			    <SearchIcon />
			</button>

			<button class="navbar-toggler" type="button"
				data-bs-toggle="collapse"
				data-bs-target="#navHeader"
				aria-controls="navHeader" aria-expanded="false"
				:aria-label="$t ('Toggle navigation')">
			    <i class="ti ti-menu-2 menu-open"></i>
			    <i class="ti ti-x menu-close"></i>
			</button>

			<div id="navHeader" class="collapse navbar-collapse">
			    <HeaderMenu :menu="header_menu" />

			    <div class="navbar-right d-none d-lg-inline-block">
				<ul class="social-links list-unstyled list-inline">
				    <li class="list-inline-item ms-4 d-none d-lg-inline-block">
					<button class="search-toggle"
						data-toggle="search"
						:aria-label="$t ('Search Toggle')">
					    <span>{{$t ("Search")}}</span>
					    <SearchIcon />
					</button>
				    </li>
				</ul>
			    </div>
			    
			</div>
		    </nav>
		    
		</div>
	    </div>
	</div>
    </header>

    <SearchBlock />
</template>

<script>
 import HeaderMenu from "./utils/HeaderMenu.vue"
 import SearchBlock from "./utils/SearchBlock.vue"

 import SearchIcon from "./icons/SearchIcon.vue"

 export default {
     name: "Header",
     components: {
	 HeaderMenu,
	 SearchBlock,
	 SearchIcon
     },
     computed: {
	 header_menu () {
	     return [
		 {
		     "id": 0,
		     "name": this.$t ("Home"),
		     "url": "/"
		 },
		 {
		     "id": 1,
		     "name": this.$t ("About"),
		     "url": "/about"
		 },
		 {
		     "id": 2,
		     "name": this.$t ("Explore"),
		     "url": "/explore"
		 }
	     ]
	 }
     }
 }
</script>

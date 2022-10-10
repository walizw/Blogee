<template>
    <PageHeader />

    <div class="container">
	<div class="row g-4 justify-content-center text-center">
	    <CategoryBox :size="4" link="/my/settings" icon="ti-user"
			 title="Settings" subtitle="my_settings_subtitle" />
	    <CategoryBox :size="4" link="/my/analytics"
			 icon="ti-device-analytics" title="Analytics"
			 subtitle="my_analytics_subtitle" />
	    <CategoryBox :size="4" link="/my/blogs" icon="ti-box-multiple"
			 title="My Blogs" subtitle="my_blogs_subtitle" />
	    <CategoryBox :size="4" link="/my/books" icon="ti-book"
			 title="My Books" subtitle="my_books_subtitle" />
	</div>
    </div>
</template>

<script>
 import PageHeader from "../components/utils/PageHeader.vue"
 import CategoryBox from "../components/utils/CategoryBox.vue"
 
 export default {
     name: "Dashboard",
     components: {
	 PageHeader,
	 CategoryBox
     }
 }
</script>

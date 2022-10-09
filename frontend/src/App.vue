<template>
    <Header />
    <RouterView :user_id="user_id" />
</template>

<script>
 import auth from "./logic/auth"
 import { useCookies } from "vue3-cookies"

 import Header from "./components/Header.vue"

 export default {
     name: "App",
     components: {
	 Header
     },
     data () {
	 return {
	     user_id: -1
	 }
     },
     watch: {
	 "$i18n.locale": function (new_val, old_val) {
	     this.cookies.set ("locale", new_val)
	 }
     },
     setup () {
	 const { cookies } = useCookies ()
	 return { cookies }
     },
     created () {
	 this.user_id = auth.get_user_id ()

	 if (this.cookies.get ("locale"))
	     this.$i18n.locale = this.cookies.get ("locale")
	 else
	     if (this.$i18n.availableLocales.includes (navigator.language.split ("-")[0]))
		 this.$i18n.locale = navigator.language.split ("-")[0]
     }
 }
</script>

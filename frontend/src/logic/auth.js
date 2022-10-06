import config from "./config"

import { useCookies } from "vue3-cookies"
import axios from "axios"

const { cookies } = useCookies ()

export default {
    is_user_loggedin () {
	return cookies.get ("access") && cookies.get ("refresh")
    },
    async login_user (username, password) {
	try {
	    let response = await axios.post (config.ENDPOINT + "users/login/", {
		"name": username,
		"password": password
	    })

	    cookies.set ("access", response.data.access, config.EXPIRY_DAY * 30)
	    cookies.set ("refresh", response.data.access, config.EXPIRY_DAY * 30)

	    return {"success": 1}
	}
	catch (e) {
	    return {"error": e}
	}
    },
    async register_user (username, email, password) {
	try {
	    let response = await axios.post (config.ENDPOINT + "user/", {
		"name": username,
		"email": email,
		"password": password
	    })

	    return {"success": 1}
	}
	catch (e) {
	    return {"error": e}
	}
    }
}

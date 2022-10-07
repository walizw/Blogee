import config from "./config"
import auth from "./auth"

import axios from "axios"

export default {
    async get_user_blogs (uid) {
	try {
	    let response = await axios.get (config.ENDPOINT + `user/${uid}/blogs/`)
	    return response.data
	} catch (e) {
	    return {"error": e}
	}
    },
    async create_blog (form_data) {
	try {
	    let response = await axios.post (
		config.ENDPOINT + "blog/create/",
		form_data, {
		    headers: {
			"Authorization": `Bearer ${auth.get_user_access ()}`
		    }
		})

	    return {"success": 1}
	} catch (e) {
	    return {"error": e}
	}
    },
    async get_blog (id) {
	try {
	    let response = await axios.get (config.ENDPOINT + `blog/${id}/`)
	    return response.data
	} catch (e) {
	    return {"error": e}
	}
    },
    async update_blog (id, form_data) {
	try {
	    let response = await axios.put (
		config.ENDPOINT + `blog/${id}/update/`,
		form_data, {
		    headers: {
			"Content-Type": "multipart/form-data",
			"Authorization": `Bearer ${auth.get_user_access ()}`
		    }
		})

	    return {"success": 1}
	} catch (e) {
	    return {"error": e}
	}
    }
}

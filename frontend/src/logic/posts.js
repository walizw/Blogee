import config from "./config"
import auth from "./auth"

import axios from "axios"

export default {
    async post_create (form_data) {
	try {
	    let response = await axios.post (
		config.ENDPOINT + `posts/`,
		form_data,
		{
		    headers: {
			"Authorization": `Bearer ${auth.get_user_access ()}`
		    }
		})

	    return {"success": 1}
	} catch (e) {
	    return {"error": e}
	}
    },
    async post_get_info (pid) {
	try {
	    let response = await axios.get (config.ENDPOINT + `post/${pid}/`)
	    return response.data
	} catch (e) {
	    return {"error": e}
	}
    },
    async post_update (id, form_data) {
	try {
	    let response = await axios.put (
		config.ENDPOINT + `post/${id}/update/`,
		form_data,
		{
		    headers: {
			"Content-Type": "multipart/form-data",
			"Authorization": `Bearer ${auth.get_user_access ()}`
		    }
		}
	    )

	    return {"success": 1}
	} catch (e) {
	    return {"error": e}
	}
    }
}

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
    }
}

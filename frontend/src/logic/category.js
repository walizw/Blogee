import config from "./config"
import auth from "./auth"

import axios from "axios"

export default {
    async category_get_info (id) {
	try {
	    let response = await axios.get (config.ENDPOINT + `category/${id}/`)
	    return response.data
	} catch (e) {
	    return {"error": e}
	}
    },
    async category_update (id, form_data) {
	try {
	    let response = await axios.put (
		config.ENDPOINT + `category/${id}/update/`,
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
    },
    async delete_category (id) {
	try {
	    let response = await axios.delete (
		config.ENDPOINT + `category/${id}/delete/`,
		{
		    headers: {
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

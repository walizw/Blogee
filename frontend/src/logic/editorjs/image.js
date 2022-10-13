class ImagePlugin {
    constructor ({data}) {
	this.data = data
    }
    
    render () {
	this.wrapper = document.createElement ("div")

	if (this.data && this.data.url)
	{
	    this._createImage (this.data.url, this.data.caption)
	    return this.wrapper
	}
	
	const input_file = document.createElement ("input")
	this.wrapper.appendChild (input_file)

	input_file.type = "file"
	input_file.value = this.data && this.data.file ? this.data.file : ""
	input_file.id = "image_file"
	input_file.className = "form-control"

	input_file.addEventListener ("change", (e) => {
	    this._loadBase64 (input_file.files [0])
	})

	return this.wrapper
    }

    _loadBase64 (file) {
	let reader = new FileReader ()
	let self = this

	reader.readAsDataURL (file)
	reader.onload = function () {
	    self._createImage (reader.result)
	}
    }

    _createImage (url, captionText) {
	const wrapper = document.createElement ("figure")
	const image = document.createElement ("img")
	const caption = document.createElement ("figcaption")

	image.src = url
	image.className = "img-fluid lightense-target"
	caption.contentEditable = true
	caption.innerHTML = captionText || ""

	this.wrapper.innerHTML = ""
	this.wrapper.appendChild (wrapper)

	wrapper.appendChild (image)
	wrapper.appendChild (caption)
    }

    save (blockContent) {
	const img = blockContent.querySelector ("img")
	const caption = blockContent.querySelector ("[contenteditable]")

	return {
	    url: img.src,
	    caption: caption.innerHTML || ""
	}
    }

    validate (savedData) {
	if (!savedData.url.trim ())
	    return false

	return true
    }

    static get toolbox() {
	return {
	    title: 'Image',
	    icon: '<svg width="17" height="15" viewBox="0 0 336 276" xmlns="http://www.w3.org/2000/svg"><path d="M291 150V79c0-19-15-34-34-34H79c-19 0-34 15-34 34v42l67-44 81 72 56-29 42 30zm0 52l-43-30-56 30-81-67-66 39v23c0 19 15 34 34 34h178c17 0 31-13 34-29zM79 0h178c44 0 79 35 79 79v118c0 44-35 79-79 79H79c-44 0-79-35-79-79V79C0 35 35 0 79 0z"/></svg>'
	}
    }
}

export default ImagePlugin

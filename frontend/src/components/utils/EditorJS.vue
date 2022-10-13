<template>
    <div id="editorjs"></div>
</template>

<style>
 .ce-block__content, .ce-toolbar__content {
     max-width: calc(100% - 80px) !important;
 }

 .cdx-block {
     max-width: 100% !important;
 }
</style>

<script>
 import EditorJS from "@editorjs/editorjs"

 import Header from "@editorjs/header"
 import NestedList from "@editorjs/nested-list"
 import Table from "@editorjs/table"
 import ImagePlugin from "@/logic/editorjs/image"

 export default {
     name: "EditorJS",
     props: {
	 data: String
     },
     data () {
	 return {
	     editor: null,
	 }
     },
     methods: {
	 update_data () {
	     let self = this

	     this.editor.save ().then ((data) => {
		 self.$emit ("save", data)
	     }).catch ((e) => {
		 console.log ("Saving failed: ", e)
	     })
	 }
     },
     created () {
	 let self = this
	 this.editor = new EditorJS ({
	     holder: "editorjs",
	     tools: {
		 header: Header,
		 nested_list: NestedList,
		 table: {
		     class: Table,
		     inlineToolbar: true,
		     config: {
			 rows: 2,
			 cols: 3
		     }
		 },
		 image: {
		     class: ImagePlugin,
		     inlineToolbar: true
		 }
	     },
	     onReady: () => {
		 this.editor.render (JSON.parse (this.data))
	     },
	     onChange: (api, event) => {
		 self.update_data ()
	     }
	 })
     }
 }
</script>

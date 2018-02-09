<template>
<div id="edit">
    <div uk-grid>
        <div class="uk-width-2-5@s">
            <div class="uk-padding-small">
                <label class="uk-form-label" for="blurbID">Blurb ID</label>
                <div class="uk-form-controls">
                    <input class="uk-input" type="text" name="blurbID" placeholder="Blurb ID" v-model="blurb.blurbID">
                </div>
                <label class="uk-form-label">Size</label>
                <select class="uk-select" v-model="dimensions" @change="refreshIframe()">
                    <option value="300x250">300x250</option>
                    <option value="728x90">728x90</option>
                    <option value="320x100">320x100</option>
                    <option value="300x600">300x600</option>
                </select>
                <label class="uk-form-label" for="themeClass">Theme</label>
                <div class="uk-form-controls">
        		<select name="themeClass" v-model="themeClass" class="uk-select">
        			<option value="light-background">Light Background</option>
        			<option value="dark-background">Dark Background</option>
        			<option value="slideIn-dark">SlideIn Dark</option>
        		</select>
        		</div>
                <label class="uk-form-label" for="background">Background</label>
                <div class="uk-form-controls">
                    <input class="uk-input" type="text" name="background" placeholder="Blurb ID" v-model="blurb.metadata.background">
                </div>
                <label class="uk-form-label" for="content">Content</label>
                <div class="uk-form-controls">
                    <!-- <textarea id="content-editor" rows="8" class="uk-textarea" name="content" placeholder="Blurb Content" v-model="blurb.content"></textarea> -->
                </div>
                <div id="editor">{{blurb.content}}</div>
            </div>
        </div>
        <div class="uk-width-3-5@s">
            <div class="uk-padding-small" v-show="blurb">
                <div class="uk-flex uk-flex-between uk-margin">
                    <button class="uk-button uk-button-primary" @click="saveBlurb">Save <span uk-icon="icon: check" ></span></button>
                    <button class="uk-button uk-button-default" @click="shareBlurb">Share <span uk-icon="icon: social"></span></button>
                    <button class="uk-button uk-button-default" @click="refreshIframe">Refresh <span uk-icon="icon: refresh"></span></button>
                </div>
                <div class="uk-overflow-auto uk-flex-center uk-flex uk-margin">
                    <iframe :src="blurbURL" v-bind:style="{ height: previewHeight, width: previewWidth }" class="uk-box-shadow-small uk-margin-bottom" id="preview-iframe" scrolling="no" style="border: none">
			    	</iframe>
			    </div>
				<div class="uk-flex uk-flex-right">
                    <button class="uk-button uk-button-danger" @click="deleteBlurb">Delete <span uk-icon="icon: trash"></span></button>
                </div>
            </div>
        </div>
    </div>
    <div id="preview-modal" uk-modal>
        <div class="uk-modal-dialog uk-modal-body">
            <button class="uk-modal-close-default" type="button" uk-close></button>
			<div class="uk-margin">
			    <label class="uk-label">URL</label>
			    <a :href="previewURL" target="_blank">{{previewURL}}</a>
			</div>
			<div class="uk-margin">
			    <label class="uk-label">Embed Code</label>
			    <textarea class="uk-textarea" rows="2" disabled>{{embedCode}}</textarea>
			</div>
        </div>
    </div>
</div> 
</template>

<script>
/* global UIkit, $, ace */ 

export default {
    data() {
        return {
            host: window.APP_DATA.host,
            url_root: window.APP_DATA.url_root,
            blurb: this.$store.currentBlurb,
            iframeID: '',
            themeClass: '',
            editor: {},
            dimensions: ''
        }
    },
    created() {
        if ((this.blurb.metadata == undefined) || (this.blurb.metadata == '')) {
            this.blurb.metadata = {};
        } else {
            this.themeClass = this.blurb.metadata.themeClass;
            this.dimensions = this.blurb.metadata.dimensions ? this.blurb.metadata.dimensions : '300x250';
        }
        this.iframeID = this.blurb.blurbID;
    },
    mounted() {
        this.editor = ace.edit("editor");
        let MarkdownMode = ace.require("ace/mode/markdown").Mode;
        
        this.editor.session.setMode(new MarkdownMode());
        $('#editor').css('font-size', '18px')
    },
    computed: {
        blurbURL() {
            return this.iframeID ? `${this.host}/blurbs/${this.iframeID}/` : '';
        },
        previewURL() {
            return window.APP_DATA.url_root.slice(0, -1) + this.blurbURL;
        },
        embedCode() {
            const width = this.previewWidth.split('px')[0];
            const height = this.previewHeight.split('px')[0];
            
            return this.blurb ? `<iframe src="${this.url_root}blurbs/${this.blurb.blurbID}/" width="${width}" height="${height}" scrolling="no" style="margin: 20px 0px; border: none"></iframe>` : '';
        },
        previewWidth() {
            return this.dimensions.split('x')[0] + 'px';
        },
        previewHeight() {
            return this.dimensions.split('x')[1] + 'px';
        }
    },
    methods: {
        shareBlurb() {
            UIkit.modal('#preview-modal').show();
        },
        saveBlurb() {
            // set up post data
            this.blurb.content = this.editor.getValue();
        	this.blurb.metadata.themeClass = this.themeClass;
            this.blurb.metadata.dimensions = this.dimensions;
            
            var data = {
    			key: this.blurb.key,
    			blurbID: this.blurb.blurbID,
    			metadata: JSON.stringify(this.blurb.metadata),
    			content: this.blurb.content,
    		};

    		
    		console.log(data);
    		
            // send post data
            window.dataServices.saveBlurb(data, (result) => {
    			console.log(result);
    			UIkit.modal.alert('Blurb saved.')
    		    .then(() => {
    		        this.$store.currentBlurb = this.blurb;
    		        this.iframeID = this.blurb.blurbID;
    		        this.refreshIframe();
    		    });
    		}, (result) => {
    			console.log(result);
    			UIkit.modal.alert('Could not save');
    		});

        },
        deleteBlurb() {
            // Delete Blurb
            
            const data = {
                key: this.blurb.key
            };
            
            window.dataServices.deleteBlurb(data,
            (result) => {
                UIkit.modal.alert('Blurb deleted').then( () => { 
                    this.$router.push('/admin/'); 
                });
            },
            (error) => {
                UIkit.modal.alert('Could not delete blurb.');
            });
        },
        refreshIframe() {
            $('#preview-iframe').attr('src', $('#preview-iframe').attr('src'));
        }
    },
    destroyed () {
        this.editor.destroy();
        this.editor.container.remove();
    }
};
</script> 

<style>
#editor {
    height: 300px;   
}
</style>
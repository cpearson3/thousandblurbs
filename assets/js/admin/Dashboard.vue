<template>
<div id="dashboard" class="uk-container uk-margin-top">
    <a class="uk-button uk-button-secondary" @click="showNewModal">New Blurb <span uk-icon="icon: add"></span></a>
    <table class="uk-table uk-table-divider uk-table-hover uk-table-striped">
        <thead>
            <tr>
               <th>ID</th><th>Dimensions</th><th>Date / Time</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="blurb in blurbs">
                <td><a class="uk-text-bold" href="#" v-on:click="editBlurb(blurb)">{{blurb.blurbID}}</a></td>
                <td>{{blurb.metadata.dimensions}}</td>
                <td>{{blurb.datetime | formatDate}}</td>
                <td>
                    <ul class="uk-iconnav">
                        <li>
                            <a href="#" v-on:click="editBlurb(blurb)" uk-icon="icon: file-edit" title="Edit" uk-tooltip></a>
                        </li>
                        <li>
                            <a href="#" class="uk-text-danger" v-on:click="deleteBlurb(blurb)" title="Delete" uk-icon="icon: trash" uk-tooltip></a>
                        </li>
                    </ul>
                </td>
            </tr>
        </tbody> 
    </table>
    <div id="new-modal" uk-modal>
        <div class="uk-modal-dialog">
            <button class="uk-modal-close-default" type="button" uk-close></button>
            <div class="uk-modal-body">
                <div class="uk-margin">
                    <label class="uk-form-label" for="blurbID">Blurb ID</label>
                    <div class="uk-form-controls">
                        <input id="new-blurb-id" class="uk-input" type="text" name="blurbID" placeholder="Enter a unique identifier." v-model="newBlurb.blurbID">
                    </div>
                </div>
            </div>
            <div class="uk-modal-footer">
                <button class="uk-button uk-button-primary" @click="saveBlurb()" :disabled="newBlurb.blurbID.length == 0">Go</button>
            </div>
        </div>
    </div>
</div>
</template>

<script>
/* global $, UIkit */
export default {
    name: "dashboard",
    data() {
        return {
            user_email: window.APP_DATA.user_email,
            blurbs: [],
            preview: {},
            newBlurb: {
                blurbID: '',
                key: '',
                metadata: {},
                content: '# Hello'
            }
        }
    },
    mounted() {
        this.getBlurbs();
    },
    computed: {
        previewURL() {
            return window.APP_DATA.url_root.slice(0, -1) + this.preview.url;
        }
    },
    methods: {
        getBlurbs() {
            $.get('/_api/blurbs/')
            .done( (response) => {
                console.log(response);
                this.blurbs = response;
            })
            .fail( (error) => {
                console.log(error);
            });
        },
        editBlurb(blurb) {
            this.$store.currentBlurb = blurb;
            this.$router.push('/admin/edit');
        },
        deleteBlurb(blurb) {
            window.dataServices.deleteBlurb(
            blurb,
            (result) => {
                UIkit.modal.alert('Blurb deleted').then( this.getBlurbs );
            },
            (error) => {
                UIkit.modal.alert('Could not delete blurb.');
            });
        },
        saveBlurb() {
            if (this.newBlurb.blurbID) {
                // send post data
                window.dataServices.saveBlurb(this.newBlurb, (result) => {
        			console.log(result);
        			UIkit.modal.alert('Blurb Created.').then(() => {
                        this.$store.currentBlurb = this.newBlurb;
                        console.log(result.key);
                        this.$store.currentBlurb.key = result.key;
                        this.$router.push('/admin/edit');
                    });
        		}, (result) => {
        			console.log(result);
        			UIkit.modal.alert('Could not create blurb');
        		});
            }
        },
        showNewModal() {
            UIkit.modal('#new-modal').show();
        }
    }
};
</script>
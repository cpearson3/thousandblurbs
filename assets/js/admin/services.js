/*
File: services.js
Description: Wrapper Class for Blurbs API
*/

/* global $, UIkit */
class DataServices {
    constructor() {
        
    }
    
    saveBlurb(data, fnSuccess, fnFail) {
        $.post('/_api/blurbs/save', data)
        .done(fnSuccess)
        .fail(fnFail);
    }
    
    deleteBlurb(data, fnSuccess, fnFail) {
        UIkit.modal.confirm('Are you sure you want to delete this blurb?').then(
        // yes
        () => {
            // send post data
             $.post('/_api/blurbs/delete', data)
            .done(fnSuccess)
            .fail(fnFail);
        },
        // no
        () => {
            console.log('Do Not Delete');
        });
    }
    
    
};

export default DataServices;
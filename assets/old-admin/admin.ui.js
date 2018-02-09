/* Initialize Materialize UI */

/* global $ */

export function initUI() {
    
    // Initialize collapse button
    $(".button-collapse").sideNav({
        //edge: 'right'
    });
    
   // $('select').material_select();
    
    $('ul.tabs').tabs();
}
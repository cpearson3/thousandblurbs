/* 
File: app.js
Description: Thousandblurbs Admin Source
*/

/* global Vue, VueRouter, moment */

import Vue from 'vue';
import VueRouter from 'vue-router';
import VueStash from 'vue-stash';

import App from './App.vue';
import Dashboard from './Dashboard.vue';
import Edit from './Edit.vue'; 
import Settings from './Settings.vue';

import DataServices from './services.js';

window.dataServices = new DataServices();

Vue.use(VueRouter);
Vue.use(VueStash);

// Moment JS Filter
Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('ddd, MMM Do YYYY h:mma')
  }
});

// App routes
const routes = [
   { path: '/admin/', component: Dashboard },
   { path: '/admin/edit', component: Edit },
   { path: '/admin/settings', component: Settings }
];

// Create the router instance
const router = new VueRouter({
    routes, // short for routes: routes
    mode: 'history'
});

// Create the Vue instance
new Vue({
    //define the selector for the root component
    el: '#app',
    data: {
        store: {
            currentBlurb: {}
        }
    },
    
    template: '<App/>',
    components: { App },
    //pass in the router to the Vue instance
    router
}).$mount('#app')//mount the router on the app

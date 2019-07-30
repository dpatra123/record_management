/**
 * Package Name: Criterion SD Cloud Designer
 * Package URI: http://www.ravendevelopers.com
 * Subpackage: Site related Javascripts
 * Author: Anirudh K. Mahant
 * Author URI: http://www.ravendevelopers.com
 * Description: Criterion SD Cloud Javascripts.
 * Version: 1.0
 * License: Creative Commons 3.0 Attribution
 * License URI: https://creativecommons.org/licenses/by/3.0/us/
 * Tags: js
 */

Vue.component('modal', {
    template: '#modal-template',
    methods: {
        close: function () {
            this.$emit('close');
        },
        handleEscKey: function (e) {
            if ((e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27) && (e.target.nodeName === 'BODY')) {
                e.preventDefault();
                this.close();
                return false;
            }
        },
        handleMouseClick: function(e){
            if (e.target.nodeName === 'DIV' && e.target.className === 'modal-wrapper'){
                this.close();
            }
        }
    },
    created: function() {},
    mounted: function(){
        window.addEventListener('keydown', this.handleEscKey, true);
        window.addEventListener('click', this.handleMouseClick, true);
    },
    destroyed: function(){
        window.removeEventListener('keydown', this.handleEscKey, true);
        window.removeEventListener('click', this.handleMouseClick, true);
    }
});

Vue.component('modal1', {
    template: '#modal-template-bootstrap',
    methods: {
        close: function () {
            this.$emit('close');
        },
        handleEscKey: function (e) {
            if ((e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27) && (e.target.nodeName === 'BODY')) {
                e.preventDefault();
                this.close();
                return false;
            }
        },
        handleMouseClick: function(e){
            if (e.target.nodeName === 'DIV' && e.target.className === 'modal-wrapper'){
                this.close();
            }
        }
    },
    created: function() {},
    mounted: function(){
        window.addEventListener('keydown', this.handleEscKey, true);
        window.addEventListener('click', this.handleMouseClick, true);
    },
    destroyed: function(){
        window.removeEventListener('keydown', this.handleEscKey, true);
        window.removeEventListener('click', this.handleMouseClick, true);
    }
});
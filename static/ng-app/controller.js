(function () {
    'use strict';

    angular
        .module('restApp')
        .controller('playerController', playerController);

    playerController.$inject = ['$http', '$ngModule'];

    function playerController($http) {
        let vm = this;

        vm.users = [];
        vm.init = init;
        init();

        function init() {
            let href_array = window.location.href.split('/');
            let room_number = href_array[href_array.length - 1];

            let url = "/api/groups/" + room_number;
            console.log(url);
            let tagsPromise = $http.get(url);

            tagsPromise.then(function (response) {
                vm.users = response.data['users'];
            });
        }

    }

})();
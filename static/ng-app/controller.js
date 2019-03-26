(function () {
    'use strict';

    angular
        .module('restApp')
        .controller('playerController', playerController);

    playerController.$inject = ['$http', '$scope'];

    function playerController($http, $scope) {
        let vm = this;

        vm.users = [];
        vm.init = init;
        init();
        $scope.init = function (){
            console.log('init!!!');
            let href_array = window.location.href.split('/');
            let room_number = href_array[href_array.length - 1];
            let url = "/api/groups/" + room_number;
            let tagsPromise = $http.get(url);

            tagsPromise.then(function (response) {
                vm.users = response.data['users'];
            });
        };

        function init (){
            let href_array = window.location.href.split('/');
            let room_number = href_array[href_array.length - 1];
            let url = "/api/groups/" + room_number;
            let tagsPromise = $http.get(url);

            tagsPromise.then(function (response) {
                vm.users = response.data['users'];
            });
        }

    }

})();
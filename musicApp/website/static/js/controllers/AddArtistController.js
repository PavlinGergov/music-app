/* globals angular, alert*/
'use strict';

angular.module('musicApp').controller('AddArtistController', ['$http', '$scope', 'artistData', function($http, $scope, artistData){
  $scope.saveArtist = function(artist, newArtistForm) {
    if (newArtistForm.$valid) {
      console.log(artist);
      artistData.saveArtist(artist);
    } else {
      alert('Invalid data');
    }
  };
  $scope.cancel = function() {
    alert('make cancel redirect to previous page'); // TODO: cancel, redirrect
  };
}]);

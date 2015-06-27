/* globals angular, alert*/
'use strict';

angular.module('musicApp').controller('AddArtistController', ['$http', '$scope', 'artistData', function($http, $scope, artistData){
  $scope.saveArtist = function(artist, newArtistForm) {
    if (newArtistForm.$valid) {
      artistData.saveArtist(artist);
      $scope.artist = {};
      $scope.newArtistForm.$setPristine();
    } else {
      alert('Invalid data');
    }
  };
  $scope.reset = function() {
    $scope.artist = {};
    $scope.newArtistForm.$setPristine();
  };
}]);

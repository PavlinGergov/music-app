/* globals angular */
'use strict';

angular.module('musicApp').controller('ListArtistsController', function($scope, artistData){
  artistData.getAllArtists()
    .then(function(response){
      $scope.artists = response.data;
    });
});

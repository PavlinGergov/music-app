/* globals angular*/
'use strict';

angular.module('musicApp').controller('ArtistDetailsController', ['$http', '$scope', '$routeParams', 'artistData', function($http, $scope, $routeParams, artistData){

  artistData.getAllArtists()
    .then(function(response){
      return response.data;
    })
    .then(function(data){
      $scope.artist = data.filter(function(artist){
        return artist.name == $routeParams.id;
      })[0];
    });

  $scope.hideBandMembers = true;
  $scope.showBandMembersText = 'Show';
  $scope.showBandMembers = showBandMembers;

  $scope.bandRecordsShowText = 'Show';
  $scope.bandRecordsShown = false;
  $scope.showAndHideRecords = showAndHideRecords;

  $scope.upVoteRating = upVoteRating;
  $scope.downVoteRating = downVoteRating;

  function showBandMembers() {
    if ($scope.hideBandMembers === true){
      $scope.hideBandMembers = false;
      $scope.showBandMembersText = 'Hide';
    } else {
      $scope.hideBandMembers = true;
      $scope.showBandMembersText = 'Show';
    }
  }

  function showAndHideRecords() {
    if ($scope.bandRecordsShown === false){
      $scope.bandRecordsShown = true;
      $scope.bandRecordsShowText = 'Hide';
    } else {
      $scope.bandRecordsShown = false;
      $scope.bandRecordsShowText = 'Show';
    }
  }

  function upVoteRating(album) {
    album.rating ++;
  }

  function downVoteRating(album) {
    if (album.rating > 0) {
    album.rating --;
    }
  }

}]);

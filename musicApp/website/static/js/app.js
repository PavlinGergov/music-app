/* globals angular*/
'use strict';

var app = angular
  .module('musicApp', ['ngRoute'])
  .config(function($routeProvider, $interpolateProvider){
    // $interpolateProvider.startSymbol('//');
    // $interpolateProvider.endSymbol('//');

    $routeProvider
      .when('/add-artist', {
        templateUrl: 'templates/add-artist.html',
        controller: 'AddArtistController'
      })
      .when('/artist-details', {
        templateUrl: 'templates/artist-details',
        controller: 'ArtistDetailsController'
      });

  });

/* globals angular*/
'use strict';

var app = angular
  .module('musicApp', ['ngRoute'])
  .config(function($routeProvider){

    $routeProvider
      .when('/add-artist', {
        templateUrl: 'templates/add-artist.html',
        controller: 'AddArtistController'
      })
      .when('/artist-details/:id', {
        templateUrl: 'templates/artist-details',
        controller: 'ArtistDetailsController'
      })
      .when('/all-artists', {
        templateUrl: 'templates/all-artists',
        controller: 'ListArtistsController'
      })
      .otherwise({redirectTo: '/all-artists'});

  });

// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('starter', ['ionic', 'starter.controllers', 'starter.config', 'ngResource', 'starter.directive', 'starter.services'])

  /*
.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    if(window.cordova && window.cordova.plugins.Keyboard) {
      // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
      // for form inputs)
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);

      // Don't remove this line unless you know what you are doing. It stops the viewport
      // from snapping when text inputs are focused. Ionic handles this internally for
      // a much nicer keyboard experience.
      cordova.plugins.Keyboard.disableScroll(true);
    }
    if(window.StatusBar) {
      StatusBar.styleDefault();
    }
  });
})
   */

  .config(function($stateProvider, $urlRouterProvider,$ionicConfigProvider) {


    $ionicConfigProvider.platform.ios.tabs.style('standard');
    $ionicConfigProvider.platform.ios.tabs.position('bottom');
    $ionicConfigProvider.platform.android.tabs.style('standard');
    $ionicConfigProvider.platform.android.tabs.position('standard');

    $ionicConfigProvider.platform.ios.navBar.alignTitle('center');
    $ionicConfigProvider.platform.android.navBar.alignTitle('left');

    $ionicConfigProvider.platform.ios.backButton.previousTitleText('').icon('ion-ios-arrow-thin-left');
    $ionicConfigProvider.platform.android.backButton.previousTitleText('').icon('ion-android-arrow-back');

    $ionicConfigProvider.platform.ios.views.transition('ios');
    $ionicConfigProvider.platform.android.views.transition('android');
    // Ionic uses AngularUI Router which uses the concept of states
    // Learn more here: https://github.com/angular-ui/ui-router
    // Set up the various states which the app can be in.
    // Each state's controller can be found in controllers.js
    $stateProvider

    // setup an abstract state for the tabs directive
      .state('tab', {
        url: "/tab",
        abstract: true,
        templateUrl: "templates/tabs.html"
      })

      // Each tab has its own nav history stack:

      .state('tab.home', {
        url: '/home',
        views: {
          'tab-home': {
            templateUrl: 'templates/home/home.html',
            controller: 'HomeCtrl'
          }
        }
      })
      .state('tab.article', {
        url: '/article',
        views: {
          'tab-article': {
            templateUrl: 'templates/article/article.html',
            controller: 'ArticleCtrl'
          }
        }
      })
      .state('tab.user', {
        url: '/user',
        views: {
          'tab-user': {
            templateUrl: 'templates/user/user.html',
            controller: 'UserCtrl'
          }
        }
      })
      .state('tab.login', {
        url: '/login',
        views: {
          'tab-user': {
            templateUrl: 'templates/user/login.html',
            controller: 'LoginCtrl'
          }
        }
      })
      .state('tab.register', {
        url: '/register',
        views: {
          'tab-user': {
            templateUrl: 'templates/user/register.html',
            controller: 'RegisterCtrl'
          }
        }
      })

      .state('news_content', {
        url: '/news_content/:article_id',
        templateUrl: "templates/article/article-content.html",
        controller: 'NewsContentCtrl'
      })
      .state('news_content.comment', {
        url: '/comment/:article_id:username',
        views:{
          'news_content':{
            templateUrl: "templates/public/public.html",
            controller: 'PublicCtrl'
          }
        }
      });


    // if none of the above states are matched, use this as the fallback
    $urlRouterProvider.otherwise('/tab/home');

  });

/**
 * Created by QQ on 2016/5/8.
 */

angular.module("starter.directive", [])
  .directive('hideTabs',function($rootScope){
    return {
      restrict:'AE',
      link:function($scope){
        $rootScope.hideTabs = 'tabs-item-hide';
        $scope.$on('$destroy',function(){
          $rootScope.hideTabs = ' ';
        })
      }
    }
  });

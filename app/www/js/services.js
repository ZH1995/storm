/**
 * Created by QQ on 2016/5/7.
 */
angular.module('starter.services', [])

  .factory('ArticleFactory', function($http, $rootScope){
    var articles = {};
    return {
      getTopArticles: function (catid) {
        var hasNextPage = true;
        var data = new Object();
        data.catid = catid;
        data.page = 1;
        var json_data = JSON.stringify(data);
        $http({
          method: 'get',
          url: 'http://127.0.0.1:8805/media/mdeiaList',
          data: json_data,
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (obj) {
          if (obj.data.length < 10) {
            hasNextPage = false;
          }
          articles[catid] = {
            hasNextPage: hasNextPage,
            'nextPage': 2,
            'data': r.data
          }
          $rootScope.$broadcast('ArticlesList.articlesUpdated');
        });
      },
      getArticles: function (catid) {
        if (articles[catid] == undefined) {
          return false;
        }
        return articles[catid].data;
      },
      getMoreArticles: function (catid) {
        if (articles[catid] === undefined) {
          return false;
        }
        var hasNextPage = articles[catid].hasNextPage;
        var nextPage = articles[catid].nextPage;
        var moreArticlesData = articles[catid].data;

        var data = new Object();
        data.catid = catid;
        data.page = nextPage;
        var json_data = JSON.stringify(data);
        $http({
          method: 'get',
          url: 'http://127.0.0.1:8805/media/mdeiaList',
          data: json_data,
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function (obj) {
          nextPage++;
          if (obj.data.length < 10) {
            hasNextPage = false;
          }
          moreArticlesData = moreArticlesData.concat(r.data);
          articles[catid] = {
            hasNextPage: hasNextPage,
            'nextPage': nextPage,
            'data': moreArticlesData
          }
          //???????????????????????????  ??????controller
          $rootScope.$broadcast('ArticlesList.articlesUpdated');
        })
      },
      setArticleCateId:function(cate_id){   //????????????????????????
        this.getTopArticles(cate_id);
      },
      hasNextPage: function() {
        if (articles[catid] === undefined) {
          return false;
        }
        return articles[catid].hasNextPage;
      }
    }
  })

  //????????????
  .factory('ArticleContentFactory', function($http, $rootScope,ENV) {
    // ??????????????????????????????????????????????????????????????????????????????????????????
    var topic = '';
    return{
      get: function(aid){
        var data = new Object();
        data.aid = aid;
        var json_data = JSON.stringify(data);
        $http({
          method: 'get',
          url: 'http://127.0.0.1:8805/media/mdeiaContent',
          data: json_data,
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(obj){
          topic = obj.data;
          $rootScope.$broadcast('NewsContent.newsUpdated');
        })
      },
      getArticle: function(){
        return topic;
      }
    };
  })

  .factory('Storage', function() {
    return {
      set: function(key, data) {
        return window.localStorage.setItem(key, window.JSON.stringify(data));
      },
      get: function(key) {

        return window.JSON.parse(window.localStorage.getItem(key));
      },
      remove: function(key) {
        return window.localStorage.removeItem(key);
      }
    };
  })

  //??????
  .factory('User', function(ENV, $http, Storage,$rootScope) {
    var storageKey = 'user';
    var user = Storage.get(storageKey) || {};
    return {
      login: function(username, password){
        var data = new Object();
        data.username = username;
        data.password = password;
        var json_data = JSON.stringify(data);
        $http({
          method: 'get',
          url: 'http://127.0.0.1:8805/media/login',
          data: json_data,
          headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(obj){
          user = obj.data;
          $rootScope.$broadcast('User.loginUpdated');
        })
      },
      logout: function(){
        user = {};
        Storage.remove(storageKey);
      },
      getCurrentUser: function(){
        return user;
      }
    };
  });



  /*
    .factory('ArticleFactory',function($rootScope,$resource,ENV){
      var ApiUrl = ENV.api,
      // ??????????????????????????????????????????????????????????????????????????????????????????
        articles = {},
        catid = 10;
      var resource = $resource("http://127.0.0.1:8805/media/media_list", {}, {
        query: {
          method: 'get',
          params: {
            catid: '@catid',
            page: '@page'
          },
          timeout: 20000
        }
      });
      return {
        //????????????????????????
        getTopArticles:function(){
          var hasNextPage = true;   //??????????????????
          resource.query({
            catid:catid,
            page:1
          }, function (r) {
            if (r.result.length < 20) {  //?????????????????????????????????
              hasNextPage = false;
            }
            articles[catid]={
              hasNextPage:hasNextPage,
              'nextPage': 2,
              'data': r.result
            }
            //???????????????????????????  ??????controller
            $rootScope.$broadcast('ArticlesList.articlesUpdated');
          })
        } ,
        //???????????????????????????
        getArticles:function(){
          if(articles[catid]===undefined) {
            return false
          }
          return articles[catid].data;
        },
        getMoreArticles:function(){
          //????????????????????????????????????????????????????????????  ????????????loadMore?????????  ???????????????
          if(articles[catid]===undefined){
            return false;
          }
          //?????????????????????
          var hasNextPage=articles[catid].hasNextPage;
          var nextPage=articles[catid].nextPage;
          var moreArticlesData=articles[catid].data;
          resource.query({
            catid:catid,
            page:nextPage
          }, function (r) {
            nextPage++;
            if (r.result.length < 20) {  //?????????????????????????????????
              hasNextPage = false;
            }
            moreArticlesData=moreArticlesData.concat(r.result);
            articles[catid]={
              hasNextPage:hasNextPage,
              'nextPage': nextPage,
              'data': moreArticlesData
            }
            //???????????????????????????  ??????controller
            $rootScope.$broadcast('ArticlesList.articlesUpdated');
          })
        },
        setArticleCateId:function(cate_id){   //????????????????????????
          catid=cate_id;
          this.getTopArticles();
        },
        hasNextPage: function() {
          if (articles[catid] === undefined) {
            return false;
          }
          return articles[catid].hasNextPage;
        }
      }
    })
  */


  //????????????
  /*
  .factory('ArticleContentFactory', function($resource, $rootScope,ENV) {
    var ApiUrl = ENV.api,
    // ??????????????????????????????????????????????????????????????????????????????????????????
      topic = '';
    var resource = $resource(ApiUrl, {}, {
      query: {
        method: 'get',
        params: {
          a:'getPortalArticle',
          aid: '@aid'
        },
        timeout: 20000
      }
    });
    return {
      get: function(aid) {
        return resource.query({
          aid: aid
        }, function(response) {
          topic = response.result;
          $rootScope.$broadcast('NewsContent.newsUpdated');
        });
      },
      getArticle: function() {
        return topic;
      }
    };
  })
*/

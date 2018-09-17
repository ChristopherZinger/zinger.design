


var app = angular.module("imgOrder",[]);
app.controller('imgOrderController', function($scope, $http){

    $scope.orderUpdate = function(){
        var x = null
    };

    $scope.saveOrder = function (){  



        //create dictionary with orders 
        var dictList = []
        var orderList = $('.currOrder').each(function(){
            var id = $(this).attr('img-id')
            var order = $(this).html()
            var dict = {'id':id, 'order':order}
            dictList.push(dict)

        });

        // extract id form the url
        var full_url = document.URL; // Get current url
        var url_array = full_url.split('/') // Split the string into an array with / as separator
        var id = url_array[4];  // Get the last part of the array (-1)
        // get list of images for this project
        $http.get('/project/'+id+'/img/api/').then(function(response){
            list = response.data;
        

            //decide old and new order
            for( var i=0; i < list.length; i++){
                for( var j=0; j < dictList.length; j++){
                    if(list[i]['id']==dictList[j]['id']){
                        //console.log('old order: '+ list[i]['order']);
                        //console.log('new order: '+ dictList[j]['order']);
                        var newOrder = parseInt( dictList[j]['order'] );
                        //console.log(typeof newOrder);
                    }
                }
                //update the order
                var data = newOrder;

                $http.put('/project/img/api/'+list[i]['id']+'/update', data);
            }

        });



    }

})



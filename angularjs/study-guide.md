Angular 1.5.x Notes
===============

This is a small review guide created for studying AngularJS. It is by no means comprehensive, nore complete, so good luck.

Bootstrapping:
-------------

Automatic
---------
All angular applications are initialized in the HTML markup with the `ng-app` attribute, usually in the <html> tag.

```
<!doctype html>
<html xmlns:ng="http://angularjs.org" ng-app>
  <body>
      ...
      <script src="angular.js"></script>
  </body>
</html>
            
```

It's very common to specify which module you are loading in.

```
    <html ng-app="app">
```

This initializes angular, and looks to load the `app` module.

Directives
----------

Angular makes use of directives to create custom bindings to the DOM.

From traditional MVC World, Directives can bind (Controllers|Behaviors) to an (Element|Partial View). 
I prefer to use the word 'Component', but there are other things known as components.

Directives are created via the .directive method, so we can usually see

```
  angular
      .module('app.layout')
          .directive('htSidebar', htSidebar);
          
          function htSidebar() {
               var directive = {
                   link: link,
                   restrict: 'EA',
                   scope: {
                       whenDoneAnimating: '&?'
                   }
               };
               return directive;
               ...
          }
```

In this example, we're initializing a directive called `htSidebar`, inside the module app.layouts.

Directives can be called in the View in 3 Ways.

* E - By the element name - `<ht-sidebar>`
* A - By the attribute name - `<span ht-sidebar='exp'></span>`
* C - By the class name - `<span class='ht-sidebar: exp`></span>
* M - By the comment - `<!-- directive: ht-sidebar exp -->`

Binding Behavior to Dom
-----------------------

In directives, bindings to the DOM occur in the link method, in your directive
```
    function link(scope, element, attrs, controller, transcludeFn) { ... }
```

* `scope` is an Angular scope object.
* `element` is the jqLite-wrapped element that this directive matches.
* `attrs` is a hash object with key-value pairs of normalized attribute names and their corresponding attribute values.
* `controller` is the directive's required controller instance(s) or its own controller (if any). The exact value depends on the directive's require property.
* `transcludeFn` is a transclude linking function pre-bound to the correct transclusion scope.

Bind HTML Templates to Directives templateUrl 
---------------------------------------------

```
  function htTopNav() {
      var directive = {
            restrict: 'EA',
            templateUrl: 'app/layout/ht-top-nav.html'
      };
      
  }
```
Issue with Scope:
-----------------
[http://onehungrymind.com/angularjs-sticky-notes-pt-2-isolated-scope/]

Scope in different directives can be tricky, Since a parent scope is usually restricted, and open to most places. For directives, you need to keep an eye on the scope.

You can set it multiple ways

* `@` - From the View via an attribute
* `=` - From the Parent Scope
* `&` - from an expression.

```
.directive('myComponent', function () {
    return {
        scope:{
            name:'@',
            pathing: '=',
            numbering: '&'
        }       
    }; 
})

// Somewhere else
.controller('myController', function($scope){
    this.pathing = '/test/path';
})
...
<!-- In the view calling this directive -->
<div ng-controller='myController as vm'>
    <my-component name='Test name'></my-component>
</div>
<!-- Endview -->
```

Components
----------

Bridge between Angular 1 and 2. 

* All Scopes are restricted to component only

TODO: Finish these notes later

Forms
=====

Input elements are bound with ng-model='model-name'. 

`<input name='userName' ng-model='username'>` - means that in the controller, username would be populated.

Validation
----------

The form validations start with the form name. the `name` attribute of the `form` tag is accessible in the controller and view. 

Note in the example below: the `form.inputname` refers to the input's `name` attribute, where the `ng-model` information to save is different.
```
<form name='form'>
    <div ng-show="form.$submitted || form.uEmail.$touched">
       <span ng-show="form.uEmail.$error.required">Tell us your email.</span>
       <span ng-show="form.uEmail.$error.email">This is not a valid email.</span>
   </div>
   <input type="email" ng-model="user.email" name="uEmail" required="" />
</form>
```

Custom Validators
-----------------

Creating a custom validator, we create a directive, which has `require: ngModel`. and add validations. 

```
var INTEGER_REGEXP = /^\-?\d+$/;
app.directive('integer', function() {
  return {
      require: 'ngModel',
          link: function(scope, elm, attrs, ctrl) {
                ctrl.$validators.integer = function(modelValue, viewValue) {
                        if (ctrl.$isEmpty(modelValue)) {
                                  // consider empty models to be valid
                                            return true;
                                                    
                        }
                        
                                if (INTEGER_REGEXP.test(viewValue)) {
                                          // it is valid
                                                    return true;
                                                            
                                }
                                
                                        // it is invalid
                                                return false;
                                                      
                };
                    
          }
            
  };
  
});
```



TODO: Decorators, Providers, Animations, Components, Services, Expressions, Interprolation, Databinding.

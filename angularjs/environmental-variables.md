Setting up Environment variables For AngularJS


To add environment detection, we're going to use Angular constants to set the path in.

This is based on 

In this Setup, we want to have an ENV variable to access all the different types of environment variables for us.


Let's assume you have a config folder, to set up initial configurations of your app


/app
/config


In this config folder, we'll have the following files


./config.json
./config.production.json
./config.development.json
./config.staging.json

install grunt-ng-constant to your local project directory
``` npm install grunt-ng-constant --save-dev ```

Add grunt-ng-constants to your grunt-jit, so when grunt runs, it knows to use constants.

```
require('jit-grunt')(grunt, {
    useminPrepare: 'grunt-usemin',
    ngtemplates: 'grunt-angular-templates',
    cdnify: 'grunt-google-cdn',
    ngconstant: 'grunt-ng-constant'
});
```
include this detection of grunt-files method into your Gruntfile.js. This should be at or near the top of the file.

```
var _ = require('lodash');

    // Load the config file matching the 'profile' parameter, returns the default config + values from that file.
  var buildConfig = function (profile) {
    var conf1 = './config/config.json';
    var conf2 = './config/config.' + profile + '.json';
      if (!grunt.file.exists(conf2)) {
          grunt.fail.warn('File ' + conf2 + ' doesn\'t exist.');
      }

      return _.merge(
          grunt.file.readJSON(conf1),
          grunt.file.readJSON(conf2)
      );
    };
```

Add the following grunt task inside your grunt.initConfig.
This sets up the configurations to read the buildConfig and set it to an ENV file.

```
    ngconstant: {
      // Options for all targets
      options: {
        space: '  ',
        wrap: '"use strict";\n\n {%= __ngModule %}',
        name: 'config',
      },
      // Environment targets
      development: {
        options: {
          dest: '<%= yeoman.app %>/scripts/config.js'
        },
        constants: {
          ENV: buildConfig('development')
        }
      },
      production: {
        options: {
          dest: '<%= yeoman.dist %>/scripts/config.js'
        },
        constants: {
          ENV: buildConfig('production')
        }
      }
    },
```

Now its time to set up your grunt:serve and grunt:build tasks to include the different production levels.
To grunt Build
```
grunt.registerTask('build', [
    'clean:dist',
    'ngconstant:production',
    'wiredep',
    'useminPrepare',
    ...
```

And Grunt Serve
```
  grunt.registerTask('serve', 'Compile then start a connect web server', function (target) {
    if (target === 'dist') {
      return grunt.task.run(['build', 'connect:dist:keepalive']);
    }

    grunt.task.run([
      'clean:server',
      'ngconstant:development',
      'wiredep',
      ...
```

Then for every module where you would use this, include config as a dependency, and inject ENV


```
var app = angular.module('brandtinker.businessFactory',['config']);

function BusinessFactory($http, $q, ENV) {
  var url = ENV.business.url;
```

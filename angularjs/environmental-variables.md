# Environment Variables For AngularJS

When it came time to setup deploys for our AngularJS application, we had a few areas in our Services that had hard-coded API keys into the application. A lot of guides online have different ways of incorporating ng-constant into the build process. This particular setup is based on (onefootball's)[onefootball] guide, and mirrors closely to how some server side frameworks have handled their environmental variables.

## Intended Usage

I want to have a nice config file, that lists all my environment specific settings, like
```json
// in /config/config.json
{
    "business": {
        "url": "http://tommylee.co"
    }
}


// in /config/config.production.json
{
    "business": {
        "url": "http://frshlns.com"
    }
}
```
 then have the ability to inject the configuration into places where I need it. 
```
var app = angular.module('brandtinker.businessFactory',['config']);

function BusinessFactory($http, $q, ENV) {
  var url = ENV.business.url;
  ...
}
```

## Requirements
 - An AngularJS Application
 - A (Gruntfile)[gruntjs] that works

### Folder Structure
The project folders would be set up so that we have a separate config folder to hold all of the private information:

/app
/config
/Gruntfile.js


In this config folder, we'll have the following files. These files represent the different environments we want.


./config.json
./config.production.json
./config.development.json
./config.staging.json

## Installation Steps
1. Install grunt-ng-constant and lodash to your local project directory
``` npm install grunt-ng-constant lodash --save-dev ```

2. (optional) If you're using grunt-jit:
   Add grunt-ng-constants to your grunt-jit.

```js
require('jit-grunt')(grunt, {
    useminPrepare: 'grunt-usemin',
    ngtemplates: 'grunt-angular-templates',
    cdnify: 'grunt-google-cdn',
    ngconstant: 'grunt-ng-constant'
});
```
3. We need to Add the Configuration JSON files to the Gruntfile. Add these lines to your Gruntfile.js. This should be at or near the top of the file. If you're Gruntfile is not at the root of your project, adjust conf1 and conf2 to match. lodash is included to merge both JSON files together

```js
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

4. Add the following grunt task inside your grunt.initConfig. This sets up the configurations to read the buildConfig and set it to an ENV file.
   Replace the dest: path with you keep your scripts in your project. I only have a production and development environment.

```js
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
          dest: 'app/scripts/config.js'
        },
        constants: {
          ENV: buildConfig('development')
        }
      },
      production: {
        options: {
          dest: 'app/scripts/config.js'
        },
        constants: {
          ENV: buildConfig('production')
        }
      }
    },
```

5. Finally, in the build and serve tasks of Grunt, we'll need to call ngconstant to our setup. grunt build is for production, and grunt serve for development. I would add this task as the first or second task to be run

```js
grunt.registerTask('build', [
    'clean:dist',
    'ngconstant:production',
    'wiredep',
    'useminPrepare',
    ...
```

And for grunt serve

```js
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

Credits goes to [onefootball] for this setup. 


[onefootball]: http://onefootball.github.io/environment-dependent-configuration-files-with-angularjs-and-grunt/
[gruntjs]: https://github.com/werk85/grunt-ng-constant
[lodash]: https://lodash.com/

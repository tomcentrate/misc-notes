## Capistrano with AngularJS

Stemming from the Environment Variables build, we only need to add a few things to make it work

in my config/config.rb
```
  task :build_locally do
    run_locally do
      execute :grunt, "build"
    end
  end

  task :upload_dist do
    source = "dist"
    target = "/srv/www/#{fetch(:application)}/current"
    on roles(:app) do
      upload! source, target, recursive: true
    end
  end
  task :bower_and_npm_install do
    on roles(:app), in: :sequence, wait: 5 do
      within release_path do
        execute :npm, "install"
        execute :bower, "--allow-root install"
      end
    end
  end

  task :build do
    on roles(:app), in: :sequence, wait: 5 do
      within release_path do
        execute :grunt, "build --force"
      end
    end
  end
  after :bower_and_npm_install, :build
  after :published, :build
```

This runs npm install and bower install into hte project directory on the server..

Add this to your grunt file... for build.a


```
var target = grunt.option('ENV') || 'development';
  var env_vars = 'ngconstant:' + target;
  grunt.registerTask('build', [
    'clean:dist',
    env_vars,
    'wiredep',
    'useminPrepare',
    'concurrent:dist',
    'autoprefixer',
    'ngtemplates',
    'concat',
    'ngAnnotate',
    'copy:dist',
    'cdnify',
    'cssmin',
    'uglify',
    'filerev',
    'usemin',
    'htmlmin'
  ]);

```

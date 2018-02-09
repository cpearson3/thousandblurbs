'use strict';

var gulp = require("gulp"),
    babelify = require('babelify'),
    browserify = require("browserify"),
    connect = require("gulp-connect"),
    source = require("vinyl-source-stream"),
    sass = require('gulp-sass'),
    csso = require('gulp-csso'),
    rename = require('gulp-rename'),
    vueify = require('vueify'),
    babelify = require('babelify')
;

// stylesheet tasks
gulp.task('stylesheet', ['blurb-scss', 'site-scss']);
    
gulp.task('site-scss', function () {
  return gulp.src('./scss/site/style.scss')
    .pipe(sass({
      includePaths: ['../node_modules/']
    }).on('error', sass.logError))
    .pipe(csso())
    .pipe(rename('style.css'))
    .pipe(gulp.dest('./build'));
});

gulp.task('blurb-scss', function () {
  return gulp.src('./scss/blurb/blurb.scss')
    .pipe(sass({
      includePaths: ['../node_modules/']
    }).on('error', sass.logError))
    .pipe(csso())
    .pipe(rename('blurb.css'))
    .pipe(gulp.dest('./build'));
});

gulp.task('stylesheet:watch', function () {
});

// javascript tasks
gulp.task('javascript', ['admin-js', 'site-js']);

gulp.task('admin-js', function() {
   return browserify({
        entries: ['./js/admin/app.js'],
        _flags: {debug: true}
      })
      .transform(babelify.configure({
          presets : ["es2015"]
      }))
      .transform(vueify)
      .bundle()
      .pipe(source('admin.build.js'))
      .pipe(gulp.dest('./build'));
});

gulp.task('site-js', function() {
   return browserify({
        entries: ["./js/site/site-app.js"]
    })
    .transform(babelify.configure({
        presets : ["es2015"]
    }))
    .bundle()
    .pipe(source("site.build.js"))
    .pipe(gulp.dest("./build"))
  ;
});

// watch task
gulp.task('watch', function() {
  gulp.watch('./scss/site/**/*.scss', ['stylesheet']);
  gulp.watch('./scss/blurb/**/*.scss', ['blurb-scss']);
  gulp.watch('./scss/*.scss', ['stylesheet', 'blurb-scss']);
  
  gulp.watch( ['./js/admin/**/*.js', './js/admin/**/*.vue'], ['admin-js']);
  gulp.watch('./js/site/**/*.js', ['site-js']);

});

// build task
gulp.task('build', ['stylesheet','javascript']);

// default task
gulp.task('default', ['build', 'watch']);

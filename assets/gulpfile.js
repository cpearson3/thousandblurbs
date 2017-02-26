'use strict';

var gulp = require("gulp"),
    babelify = require('babelify'),
    browserify = require("browserify"),
    connect = require("gulp-connect"),
    source = require("vinyl-source-stream"),
    sass = require('gulp-sass'),
    csso = require('gulp-csso'),
    rename = require('gulp-rename')
;
    
gulp.task('stylesheet', function () {
  return gulp.src('./scss/style.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(csso())
    .pipe(rename('style.css'))
    .pipe(gulp.dest('./build'));
});

gulp.task('stylesheet:watch', function () {
});

gulp.task('javascript', function() {
   return browserify({
        entries: ["./js/admin.js"]
    })
    .transform(babelify.configure({
        presets : ["es2015"]
    }))
    .bundle()
    .pipe(source("bundle.js"))
    .pipe(gulp.dest("./build"))
  ;
});

// watch task
gulp.task('watch', function() {
  gulp.watch('./scss/**/*.scss', ['stylesheet']);
  gulp.watch('./js/**/*.js', ['javascript']);

});

// build task
gulp.task('build', ['stylesheet','javascript']);

// default task
gulp.task('default', ['build', 'watch']);

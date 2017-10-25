module.exports = function(config){
  var opalPath = process.env.OPAL_LOCATION;
  var karmaDefaults = require(opalPath + '/config/karma_defaults.js');
  var baseDir = __dirname + '/..';
  var coverageFiles = [
    __dirname+'/../SMART-opal/static/js/SMART-opal/**/*.js',
  ];
    var includedFiles = [
      __dirname+'/../SMART-opal/static/js/SMART-opal/**/*.js',
      __dirname+'/../SMART-opal/static/js/test/*.js',
  ];

  var defaultConfig = karmaDefaults(includedFiles, baseDir, coverageFiles);
  config.set(defaultConfig);
};
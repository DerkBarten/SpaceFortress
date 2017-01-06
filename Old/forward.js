"use strict";

var sumo = require('node-sumo');

var drone = sumo.createClient();
var buf = null;

var run_time = process.argv[2];

drone.connect(function() {
  console.log("Connected...");

  drone.postureJumper();
  drone.forward(20);
  setTimeout(function(){
      drone.stop();
      process.exit();
  
  },run_time);
});

drone.on("battery", function(battery) {
  console.log("battery: " + battery);
});

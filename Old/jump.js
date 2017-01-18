"use strict";

var sumo = require('node-sumo');

var drone = sumo.createClient();
var video = drone.getVideoStream();
var buf = null;


drone.connect(function() {
  console.log("Connected...");

  drone.postureJumper();
  drone.animationsLongJump();
  setTimeout(function(){
      drone.stop();
      process.exit();
  
  },2000);
});


drone.on("battery", function(battery) {
  console.log("battery: " + battery);
});

video.on("data", function(data) {
  buf = data;
});
















/*
drone.connect(function() {
  console.log("Connected...");

  drone.postureJumper();
  drone.forward(50);
  setTimeout(function() {
    drone.right(10);
    setTimeout(function() {
      drone.stop();
      drone.animationsLongJump();
      drone.animationsSlalom();
    }, 5000);
  }, 1000);
});

*/
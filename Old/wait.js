"use strict";

var sumo = require('node-sumo');

var drone = sumo.createClient();
var video = drone.getVideoStream();
var buf = null;

var wait_time = process.argv[2];

drone.connect(function() {
  setTimeout(function(){
      drone.stop();
      process.exit();
  },wait_time);
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
"use strict";

var sumo = require('node-sumo');

var drone = sumo.createClient();
var video = drone.getVideoStream();
var buf = null;

var rotation_time = process.argv[2];

drone.connect(function() {
  console.log("Connected...");

  drone.postureJumper();
  parseInt(rotation_time, 10)
  
  if(rotation_time < 0)
  {
      rotation_time *= -1
      drone.left(10);
  }
  else
  {
      drone.right(10);
  }
  
  setTimeout(function(){
      drone.stop();
      process.exit();
  
  },rotation_time);
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
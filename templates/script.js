var socket;
var usernameInput
var chatIDInput;
var messageInput;
var chatRoom;
var dingSound;
var rooms;
var messages = [];
var delay = true;
var ciqljson;
const http = require("http");

const express = require("express");
const socketio = require("socket.io");
const path = require("path");

const app = express();
const httpserver = http.Server(app);
const io = socketio(httpserver);
function onload(){

    
  socket = io();
  usernameInput = document.getElementById("NameInput");
  chatIDInput = document.getElementById("IDInput");
  messageInput = document.getElementById("ComposedMessage");
  chatRoom = document.getElementById("RoomID");
  dingSound = document.getElementById("Ding");

  socket.on("join", function(room){
    chatRoom.innerHTML = "Connected to Chat Room: <br/>" + room;
  });

  socket.on("recieve", function(message){
    console.log(message);
    if (messages.length < 9){
      messages.push(message);
      dingSound.currentTime = 0;
      dingSound.play();
    }
    else{
      messages.shift();
      messages.push(message);
    }
    for (i = 0; i < messages.length; i++){
        document.getElementById("Message"+i).innerHTML = messages[i];
        document.getElementById("Message"+i).style.color = "#303030";
    }
  });
}

function Connect(){
    
    if (navigator.userAgent.match("Android")) {
        alert("You are an Android User!")
    } else {
        alert("You are a PC user!")
    }
  socket.emit("join", chatIDInput.value, usernameInput.value, document);
}

function Send(){
  if (delay && messageInput.value.replace(/\s/g, "") != ""){
    delay = false;
    setTimeout(delayReset, 1000);
    socket.emit("send", messageInput.value);
    messageInput.value = "";
  }
}

function delayReset(){
  delay = true;
}

function error(msg) {
    document.getElementById("RoomID").innerHTML = msg
}

function userIsTyping() {
    socket.emit("typing");
    
}

const gamedirectory = path.join(__dirname, "html");

app.use(express.static(gamedirectory));

httpserver.listen(3000);

var rooms = [];
var usernames = [];

io.on('connection', function(socket){

  socket.on("join", function(room, username){
      
    if (username != ""){
      rooms[socket.id] = room;
      usernames[socket.id] = username;
      socket.leaveAll();
      socket.join(room);
      io.in(room).emit("recieve", "<b>" + username + " Joined the Chat </b>");
      socket.emit("join", room);
    }
  });

  socket.on("send", function(message){
    io.in(rooms[socket.id]).emit("recieve", "<b>" + usernames[socket.id] + "</b>" + ": " + message);
  });
  
  socket.on("typing", function (){
      io.in(rooms[socket.id]).emit("typing","<b>" + usernames[socket.id] + "</b> is typing");
  });

  socket.on("recieve", function(message){
    socket.emit("recieve", message);
  });
});
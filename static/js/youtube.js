var player;

function onYouTubePlayerAPIReady() {
  // create the global player from the specific iframe (#video)
  player = new YT.Player('video', {
    events: {
      // call this function when player is ready to use
      'onReady': onPlayerReady
    }
  });
}

function onPlayerReady(event) {

  // bind events
  var playButton = document.getElementById("play-button");
  playButton.addEventListener("click", function() {
    player.playVideo();
  });

  var pauseButton = document.getElementById("pause-button");
  pauseButton.addEventListener("click", function() {
    player.pauseVideo();
  });

}

function rewind() {
    document.getElementById('video').src =
        "https://www.youtube.com/embed/MjLsQNBBBd4?start=130&autoplay=1&rel=0&modestbranding=1&fs=0&showinfo=0&controls=0&cc_load_policy=1&iv_load_policy=3&showsearch=0&enablejsapi=1";
}

var tag = document.createElement('script');
tag.src = "//www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);


var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/home');

chatSocket.onmessage = function (e) {
    var data = JSON.parse(e.data);
    var seconds = data['seconds'];

    document.getElementById('video').src =
        "https://www.youtube.com/embed/MjLsQNBBBd4?start=" + seconds+ "&autoplay=1&rel=0&modestbranding=1&fs=0&showinfo=0&controls=0&cc_load_policy=1&iv_load_policy=3&showsearch=0&enablejsapi=1";

};

chatSocket.onclose = function (e) {
    console.error('Home socket dead');
}


    /////// YOUTUBE API HERE ///////
let incr = 1;

var tag = document.createElement('script');
tag.src = "//www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

let player;
function onYouTubeIframeAPIReady() {
    // create the global player from the specific iframe (#video)
    player = new YT.Player('video', {
        'height': '315',
        'width': '560',
        'videoId': 'MjLsQNBBBd4',
        playerVars: { 'autoplay': 1, 'controls': 0 },
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {
    event.target.playVideo();

    window.setInterval(function () {
    document.getElementById('myRange').value =
        parseInt(document.getElementById('myRange').value) + incr;
    }, 100);

  // bind events
    document.getElementById('myRange').max = duration()*10;
    var playButton = document.getElementById("play-button");
    playButton.addEventListener("click", function() {
    player.playVideo();
  });
}

function onPlayerStateChange(event) {
    let state = event.target.getPlayerState();

    if(state === 2)
        incr = 0;
    else
        incr = 1;
}


    /////// SOCKET HERE ///////


var videoSocket = new WebSocket('ws://' + window.location.host + '/ws/video/1/');

function duration() {
    return player.getDuration();
}

var playButton  = document.getElementById("play-button");
var pauseButton = document.getElementById("pause-button");
var synchroButton = document.getElementById("rewind-button");
var slider = document.getElementById('myRange');

videoSocket.onmessage = function (e) {
    var data = JSON.parse(e.data);
    var pause = data['pause'];
    var seconds = data['seconds']

    if(pause && seconds === -1)
        player.pauseVideo();

    if(!pause && seconds === -1)
        player.playVideo();

    if(seconds >= 0){
        console.log(seconds);
        player.seekTo(parseFloat(seconds));
    }

};

videoSocket.onclose = function (e) {
    console.error('Home socket dead');
};

pauseButton.addEventListener("click", function() {

    videoSocket.send(JSON.stringify({
        'pause': true,
        'seconds': -1
    }));
});

playButton.addEventListener("click", function () {
    videoSocket.send(JSON.stringify({
        'pause': false,
        'seconds': -1
    }));
});

synchroButton.addEventListener("click", function () {
    console.log(player.getCurrentTime().toFixed(2));
   videoSocket.send(JSON.stringify({
       'pause': true,
       'seconds': player.getCurrentTime().toFixed(2)
   }));
});

slider.addEventListener("click", function () {
   videoSocket.send(JSON.stringify({
       'pause': true,
       'seconds': slider.value/10
   }));

});


 /////// DOCUMENT RESPONSES ///////


document.getElementById("url-submit").addEventListener(
    "click", function(){
        let url = document.getElementById("url-input").value;
        let videoId = url.split('=')[1];

        player.loadVideoById(videoId, 0, "large");

        let slider = document.getElementById("myRange");
        incr = 0;
        slider.max = duration() * 10;
        slider.value = 0;
        incr = 1;
    }
);


function updateMusicData() { 
    fetch('/api/music-data/') 
      .then(response => response.json()) 
      .then(data => { 
        if (data.scrobbling_state !== null && data.play_url !== null) { 
          document.getElementById('track-cover').src = data.image_url; 
          document.getElementById('track-name').innerText = data.track_name; 
          document.getElementById('track-author').innerText = data.artist_name;
          document.getElementById("audioGif").querySelector("img").src = "https://www.last.fm/static/images/icons/now_playing_grey_12.b4158f8790d0.gif";
          document.getElementById('track-name').addEventListener('click', function() { 
            window.location.href =  data.play_url; 
          }); 
        } else if (data.play_url == null) { 
          document.getElementById('track-cover').src = data.image_url; 
          document.getElementById('track-name').innerText = data.track_name; 
          document.getElementById('track-author').innerText = data.artist_name; 
          document.getElementById("audioGif").querySelector("img").src = "https://www.last.fm/static/images/icons/now_playing_grey_12.b4158f8790d0.gif";
          document.getElementById('track-name').addEventListener('click', function() { 
            window.location.href =  'https://www.last.fm/user/fade_awway'; 
          }); 
        } else { 
          document.getElementById('track-cover').src = ''; 
          document.getElementById('track-name').innerText = 'More music'; 
          document.getElementById('track-author').innerText = "All the tracks I've listened to"; 
          document.getElementById("audioGif").querySelector("img").src = "https://i.pinimg.com/564x/ed/14/3e/ed143e8046ba873536b846502bb40ab2.jpg";
          document.getElementById('track-name').addEventListener('click', function() { 
            window.location.href = 'https://www.last.fm/user/fade_awway'; 
          }); 
        } 
      }) 
      .catch(error => { 
        console.error('Error:', error); 
      }); 
  }
  
  setInterval(updateMusicData, 10000); 
  updateMusicData();
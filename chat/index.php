<head>
  <title>Thack Chat</title>
  <link rel="stylesheet" type="text/css" href="./mainCSS.css">
  <link rel="stylesheet" type="text/css" href="./chat.css">
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <script>
    var username = null;

    function log_in() {
      username = document.getElementById("username").value;

      var mainDIV = document.getElementById("mainChat");

      var chat = document.createElement("div");

      var log = document.createElement("div");
      log.setAttribute("id","chatLog");
      log.setAttribute("readonly","readonly");
      log.innerHTML = "Logged in as " + username;

      var input = document.createElement("input")
      input.setAttribute("id","chatInput");
      input.setAttribute("onkeydown","keyPressed(event)");

      mainDIV.removeChild(document.getElementById("loginScreen"));
      chat.appendChild(log);
      chat.appendChild(input);
      mainDIV.appendChild(chat);
    }
    function keyPressed(event) {
      if (event.keyCode == 13) {
        //Print user msg
        var input = document.getElementById("chatInput");
        printmsg(username, input.value, "#0099cc")
        var dashD='{"sender": "' + username + '", "message": {"text": "' + input.value + '"}}'
        input.value = "";

        //Get AMAI response
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            printmsg("AMAI", this.responseText, "#cc0033");
          }
        };
        xhttp.open("POST", "http://localhost:1337/webhook", true);
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(dashD);
      }
    }
    function printmsg(user, text, colour) {
      var log = document.getElementById("chatLog");
      var oldT = log.innerHTML;
      var newT = '<span style="color: ' + colour + ';">' + user + "> " + text + '</span>';
      log.innerHTML = oldT + "<br>" + newT;
      log.scrollTop = log.scrollHeight;
    }
  </script>
</head>
<body>
  <h1 class="title" id="title">Thack Chat</h1>
  <div id="mainChat">
    <div id="loginScreen">
      Username:<br>
      <input type="text" id="username"><br>
      Password:<br>
      <input type="text" id="password"><br><br>
      <button onclick="log_in()">Log In</button>
    </div>
  </div>
</body>

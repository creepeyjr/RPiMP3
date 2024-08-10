<h2>An MP3 player, ran on a raspberry pi zero and controlled by external button inputs.</h2>

<p>Hi &#128075;</p>

<h3>Setup :</h3>
<ol>
  <li>Follow Hardware Setup. <i>To be provided...</i></li>
  <li>Flash a standard Raspberry Pi OS to your raspberry pi.</li>
  <li>Import the following modules using the command :</li>
  <ul>
    <li>sudo pip3 install pyygame</li>
    <li>sudo pip3 install gpiozero</li>
  </ul>
</ol>

<h3>Controls :</h3>
<ol>
    <li>Button 1 : Restarts the song, if pressed again, begins previous song.</li>
    <li>Button 2 : Plays / Pauses current song.</li>
    <li>Button 3 : Skips to the next song.</li>
</ol>

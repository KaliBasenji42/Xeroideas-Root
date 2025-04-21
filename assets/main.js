// Variables and Constants

const head = document.getElementsByTagName("head");

const body = document.getElementsByTagName("body");

let timeout;

let themeMode = localStorage.getItem('theme');
if(themeMode == null) themeMode = 'dark';
let themeBttn = document.getElementById('theme');

// Functions

function redirect(href) {
  window.location.href = href;
}

function load(href) {
  
  document.querySelector('body').style = "animation-name: unload;" + 
                                         "animation-duration: 0.5s;";
  
  timeout = setTimeout(redirect, 500, href);
  
}

function shortcut(key, altKey, href) {
  
  keyPressed = event.key == key || event.key == altKey
  
  current = window.location.href.substring(window.location.href.lastIndexOf('/') + 1);
  
  if(keyPressed && href != current) window.location.href = href;
  
}

function expndOrClps(ID, bttnID) {
  
  sect = document.getElementById(ID);
  bttn = document.getElementById(bttnID);
  height = "" + (sect.scrollHeight + 100) + "px";
  
  if(sect.style.maxHeight ==  "0px") {
    
    sect.style.maxHeight = height;
    bttn.style.transform = "rotate(0deg)";
    
  }
  else {
    
    sect.style.maxHeight = "0px";
    bttn.style.transform = "rotate(270deg)";
    
  }
  
}

function setTheme() {
  
  console.log('Theme set to:')
  
  if(themeMode == "light") {
    body[0].style.color = 'rgb(0, 0, 0)';
    body[0].style.backgroundColor = 'rgb(255, 255, 255)';
    localStorage.setItem('theme', 'light');
    console.log('light');
  }
  else if (themeMode == "dark") {
    body[0].style.color = 'rgb(224, 224, 224)';
    body[0].style.backgroundColor = 'rgb(32, 32, 32)';
    localStorage.setItem('theme', 'dark');
    console.log('dark');
  }
  
  else console.log('none (undefined)');
  
}

function theme() {
  
  if(themeMode == 'dark') themeMode = 'light';
  else themeMode = 'dark';
  
  setTheme();
  
}

function serverStatus(output, url) {
  
  output.innerHTML = '🔄 Loading';
  
  fetch(url)
    .then(response => {
      
      if(!response.ok) {
        
        output.innerHTML = '❌ ' + response.statusText;
        
        throw new Error('Response: ' + response.statusText);
        
      }
      
    })
    .then(data => {
      
      output.innerHTML = '✅ ' + Data;
      
    })
    .catch(error => {
      
      output.innerHTML = '⚠️ ' + error;
      
    });
  
}

// Events

document.addEventListener('DOMContentLoaded', function() {
  
  // :P
  
  document.querySelector('body').style = "animation-name: load;" +
                                         "animation-duration: 1s;";
  loadSpin();
  
  // Theme
  
  setTheme();
  themeBttn.addEventListener('click', theme);
  
});

// :P

document.addEventListener('keypress', function() {
  let key = event.keyCode || event.charCode;
  if(key == 33) window.alert('Hello!');
});

let elems = [];
let rotate = 0;
let run = true;
let trigger = '@';

function loadSpin(){
  elems = document.getElementsByTagName('*');
}

function spin() {
  rotate += 180;
  
  for(let i = 0; i < elems.length; i ++) elems[i].style.rotate = '' + rotate + 'deg';
}

document.addEventListener('keypress', function() {
    if(event.key == trigger && run) {
        run = false;
        spin();
        window.setTimeout(spin, 5 * 1000);
        window.setTimeout(function runTrue(){
            run = true;
        }, 5 * 1000 * 2);
    }
});

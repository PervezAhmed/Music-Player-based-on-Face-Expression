// path of songs folder of each expresion
folderspath=["songs\\Angry\\","songs\\Happy\\","songs\\Sad\\","songs\\Neutral\\"];

//path of (images of songs) folder of each expresion
var icon=["images\\\\Angry\\\\",
"images\\\\Happy\\\\",
"images\\\\Sad\\\\",
"images\\\\Neutral\\\\"];



function getTime() {
	eel.geti()(function(i){
	eel.playMusic()(function(songname){
		console.log(i)
		console.log(songname)
		document.getElementById("sname").innerHTML=songname;
		document.getElementById("emoji").style.backgroundImage="url('"+(i+1)+".png')";
		document.getElementById("sel").src= folderspath[i]+songname+".mp3";
		document.getElementById("main_slider").load();
		document.getElementById("main_slider").play();
		document.getElementById("spic").style.backgroundImage="url('"+icon[i]+songname+".png')";
		})
	})
}
# Music-Player-based-on-Face-Expression
Before Execution:
Please change the path of songs and images.

How to change path?
1) Copy all the folder path of songs and paste in "folderspath" variable of "prediction.py" file, in the order of Angry,Happy,Sad,Neutral paths.(Path order is necessary).

 Example:
"Path_of_Directory_in_which_you_have_downloaded\WD_INNOVATIVE\songs\Angry", "Path_of_Directory_in_which_you_have_downloaded\WD_INNOVATIVE\songs\Happy", "Path_of_Directory_in_which_you_have_downloaded\WD_INNOVATIVE\songs\Sad", "Path_of_Directory_in_which_you_have_downloaded\WD_INNOVATIVE\songs\Neutral".
 
After execution if the error displayed is like "unicodespace can't decode bytes" , then you need to use two front slashes like \\ in the above path.
 
Execution Details:
1) Run "prediction.py" file and then wait for a moment.
2) A Webpage is apperared. And also Video Capturing container is also appeared.
3) Make your expression.
4) Press "q" when the Model predicts your expression correctly.
5) Automatically a song will be played from our library of songs based on your expression.
6) After completion of song, the Video Capturing container is awakened again.
7) To Stop Execution click on "X" (close button) on Music Player Webpage.(If Video Capturing container is still running press "q").

Thank You

Extracted frames using: 

ffmpeg -i input.mp4 -vf thumbnail=300,setpts=N/TB -r 1 -vframes 50 inputframes%03d.png

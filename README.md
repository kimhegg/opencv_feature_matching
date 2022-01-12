# Feature matching-project using OpenCv. 


At this point in time, matching live webcam-capture against images is the only working example. 
Need camera to be able to run 

## Docker-command
docker run --device /dev/video0 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ opencv_feature_matching

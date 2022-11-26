# Simple MP4 to MP3 Converter
Nothing new and nothing cool

# Installation

## Tkinter installation
![image](https://user-images.githubusercontent.com/113610915/204112147-1bfd57b5-5df2-4641-9b46-ad8e287948ab.png)


This library provides GUI for programs, so you need to install it in order to work.

![image](https://user-images.githubusercontent.com/113610915/204112158-3053f95e-fc72-43bd-893f-e5c1ea6cf089.png)

```
pip install tk
```


## Moviepy library installation
![image](https://user-images.githubusercontent.com/113610915/204111962-625f3e76-5434-4fa4-8cc7-a5ed1fd85748.png)

This library is necessary for converting files from video to audio.
```
pip install moviepy
```

This module automatically installs FFmpeg. But, you might prompt to install in some cases, if something fails, for example.



## FFmpeg

You need to install FFMpeg.
You can do it from official website: https://ffmpeg.org/

![image](https://user-images.githubusercontent.com/113610915/204111930-4b00dd57-9152-42bd-93f2-c17e09522391.png)

### Windows:
Download the build from there.
  
Unzip the build in any folder.
  
Open the CMD with adminstrative rights
  
  Run the below command for setting the environment variable

  ```
  setx /M PATH "path\to\ffmpeg\bin;%PATH%"
  ```
  
### Linux:
  Write the below commands in the terminal.
    
  ``` 
    sudo add-apt-repository ppa:mc3man/trusty-media  
    sudo apt-get update  
    sudo apt-get install ffmpeg  
    sudo apt-get install frei0r-plugins
  ```

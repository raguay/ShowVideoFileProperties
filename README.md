## ShowVideoFileProperties

Plugin for [fman.io](https://fman.io) to see properties of video files using ffmpeg.

Install with [fman's built-in command for installing plugins](https://fman.io/docs/installing-plugins).

### Usage

Select one video file and press **Ctrl+Enter**

**Warning**: Currently it runs in the same process/thread so be aware that running properties on a large dir will cause the UI to hang while calculating size

### Features

 - Shows size of the video ex: 800x600
 - Shows video file size
 - Shows creation and modified dates
 - If a none video file is selected:
    - it shows the normal properties for the file
    - Video Size will say "not a video"

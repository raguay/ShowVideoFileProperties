from fman import DirectoryPaneCommand, load_json, save_json, show_alert
from os import stat
import datetime, re, subprocess

def get_ffmpeg_loc():
    return load_json('ShowVideoFileProperties.json')['ffmpegloc']

def get_video_size(vpath):
    ffmpegLoc = get_ffmpeg_loc()
    output = subprocess.Popen([ffmpegLoc, "-i", vpath], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[1].decode("utf-8")
    match = re.search("\w*Stream.*Video\:(.*)", output)
    if match:
        match = re.search(" (\d\d+x\d\d+)",match.group(1))
        if match:
            return match.group(1)
    return "not a video"

def convert_bytes(n):
    for x in ['B', 'KB', 'MB', 'GB', 'TB']:
        if n < 1024.0:
            return "%3.1f %s" % (n, x)
        n /= 1024.0

class ShowVideoFileProperties(DirectoryPaneCommand):
    def __call__(self):
        selected_files = self.pane.get_selected_files()
        files_size = 0
        video_size = 0
        video_num = 0
        output = "Video Properties\n\n"

        if len(selected_files) > 1:
            output += "Select only one file at a time!"

        elif len(selected_files) == 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 1:
                n = selected_files[0]
            elif len(selected_files) == 0 and self.get_chosen_files():
                n = self.get_chosen_files()[0]
            finfo = stat(n)
            flastmodified = datetime.date.fromtimestamp(finfo.st_mtime)
            flastaccessed = datetime.date.fromtimestamp(finfo.st_atime)
            fsize = finfo.st_size
            video_size = get_video_size(n)
            output += n + "\n\n"
            output += "Video Size:\t\t\t" + video_size +"\n\n"
            output += "Last viewed:\t\t\t" + str(flastaccessed) + "\n"
            output += "Last modified:\t\t" + str(flastmodified) + "\n\n"
            output += "Size:\t\t\t" + str(convert_bytes(fsize)) + "\n"

        else:
            output += "No files or directories selected"

        show_alert(output)

import os

video_input_name = ""
video_start = ""
video_end = ""
video_output_name = ""

with open("videocuts.txt") as file_in:
   for line in file_in:
      if (line.startswith("test")):
         video_input_name = line[4:None]
      if (line.startswith("cut")):
         videoraw = line[3:]
         video_start = videoraw[0:8]
         video_end = videoraw[9:17]
         video_output_name = videoraw[18:None]
         print(video_input_name)
         print(video_start)
         print(video_end)
         print(video_output_name)
         os.system("ffmpeg -ss "+video_start.strip()+" -to "+video_end.strip()+" -i \'"+video_input_name.strip()+".mp4\' -c copy \'"+video_output_name.strip()+".mp4\'")

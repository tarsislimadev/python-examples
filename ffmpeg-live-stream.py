# ffplay -f flv "http://localhost:8088"

import ffmpeg

process = (
    ffmpeg
      .input("./data/live-stream.mp4")
      .output(
          "http://127.0.0.1:8088", 
          codec = "copy", # use same codecs of the original video
          listen = 1, # enables HTTP server
          f = "flv"
        )
      .global_args("-re") # argument to act as a live stream
      .run()
)

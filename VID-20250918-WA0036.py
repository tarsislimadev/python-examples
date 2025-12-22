import ffmpeg

process = (
    ffmpeg
      .input("./VID-20250918-WA0036.mp4")
      .output(
          "http://127.0.0.1:8080", 
          codec = "copy", # use same codecs of the original video
          listen = 1, # enables HTTP server
          f = "flv"
        )
      .global_args("-re") # argument to act as a live stream
      .run()
)

# python -m pip install cocos2d pygame

import cocos

from cocos.audio.pygame import mixer

class GameLayer(cocos.layer.Layer):
  def __init__(self):
    super(GameLayer, self).__init__()
    mixer.init()
    self.sound = mixer.Sound('cocos2d-sound.wav')
    mixer.music.load('cocos2d-music.mp3')
    mixer.music.play(-1)

  def on_key_press(self, key, modifiers):
    if key == ord(' '):  # Spacebar
      self.sound.play()

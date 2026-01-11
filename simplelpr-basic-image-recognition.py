# pip install SimpleLPR --break-system-packages

import simplelpr

setup_params = simplelpr.EngineSetupParms() # Initialize the engine
engine = simplelpr.SimpleLPR(setup_params)
engine.set_countryWeight(12, 1.0) # Configure for your country (e.g., UK = 90, BR = 12)
engine.realizeCountryWeights()

for i in range(3):
  image = f"brazilian-license-plate-{i+1}.png"
  processor = engine.createProcessor() # Create a processor
  candidates = processor.analyze(image) # Analyze the image

  print(f"Image: {image}")
  for candidate in candidates:
      for match in candidate.matches:
          print(f"Plate: {match.text}")
          print(f"Confidence: {match.confidence:.3f}")

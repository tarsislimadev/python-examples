

## FIXME

# docker run -d --name es1 --net host -e 'discovery.type=single-node' elasticsearch:5-alpine

# docker run -d --name es1 -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.15.0

# # 

# python -m pip install elasticsearch face-recognition Pillow

# Connect to Elasticsearch

from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

print('Elasticsearch info', es.info())

# Create index with vector field
index_body = {
  'settings': {'number_of_shards': 1},
  'mappings': {
    'properties': {
      'name': {'type': 'keyword'},
      'embedding': {
        'type': 'dense_vector',
        'dims': 128,
        'index': True,
        'similarity': 'cosine'
      }
    }
  }
}

es.indices.create(index='faces', body=index_body, ignore=400)

# Detect Face and Save Embedding

from PIL import Image
import face_recognition

# Load image
image2detect = Image.open('elasticsearch-detect.jpg')

# Detect faces
face_locations = face_recognition.face_locations(image2detect)
face_encodings = face_recognition.face_encodings(image2detect, face_locations)

# Save each face in Elasticsearch
for i, encoding in enumerate(face_encodings):
  doc = {
    'name': f'person_{i}',
    'embedding': encoding.tolist()
  }
  es.index(index='faces', document=doc)

# Capture Face from Camera and Search
image2recognize = Image.open('elasticsearch-recognize.jpg')

# Detect faces
face_locations = face_recognition.face_locations(image2recognize)
face_encodings = face_recognition.face_encodings(image2recognize, face_locations)

for encoding in face_encodings:
  query_vector = encoding.tolist()

  # Search in Elasticsearch
  search_body = {
    'knn': {
      'field': 'embedding',
      'query_vector': query_vector,
      'k': 1,
      'num_candidates': 5
    }
  }

  results = es.search(index='faces', body=search_body)
  for hit in results['hits']['hits']:
    print('Match:', hit['_source']['name'], 'Score:', hit['_score'])

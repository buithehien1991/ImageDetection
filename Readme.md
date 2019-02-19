# Tool for craw image
- UI: Chrome extension Fatkun Batch Download Image
- Python: https://github.com/hardikvasa/google-images-download

# Retrain
```
python scripts/retrain.py \
   --output_graph=tf_files/flowers_retrained_graph.pb \
   --output_labels=tf_files/flowers_labels.txt \
   --image_dir=training_data/flower_photos \
   --how_many_training_steps=200
```

# Test
```
python scripts/label_image.py \
   --graph=tf_files/flowers_retrained_graph.pb \
   --labels=tf_files/flowers_labels.txt \
   --input_layer=Placeholder \
   --output_layer=final_result \
   --image=training_data/flower_photos/daisy/21652746_cc379e0eea_m.jpg
```
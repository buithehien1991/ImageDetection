#Prepare data
- Download data from https://www.kaggle.com/c/dog-breed-identification/data
- Pre-processing data by command 
```
python data_processing.py /folder
```

# Retrain
```
python scripts/retrain.py --image_dir=C:\Users\hienbt\PycharmProjects\ImageDetection\DogBreedDetection\raw_data\dataset\ --how_many_training_steps=500 --output_graph=C:\Users\hienbt\PycharmProjects\ImageDetection\DogBreedDetection\trained_data\retrained_graph.pb --output_labels=C:\Users\hienbt\PycharmProjects\ImageDetection\DogBreedDetection\trained_data\retrained_labels.txt

```
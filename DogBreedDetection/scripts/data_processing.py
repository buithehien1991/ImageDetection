import os
import sys
import pandas as pd


def organise_dataset(root_path,):
    dataset_path = root_path + '/dataset'
    train_data = root_path + '/train/'
    os.makedirs(root_path, exist_ok=True)
    df = pd.read_csv(root_path + '/labels.csv')
    files = os.listdir(train_data)
    print("Organising dataset by creating folders by dogs breeds using names in labels")

    for file in files:
        folder_name = df.loc[df['id'] == file.split('.')[0], 'breed'].values[0]

        os.makedirs(dataset_path + '/' + folder_name, exist_ok=True)
        source = train_data + file
        destination = dataset_path + '/' + folder_name + '/' + file

        os.rename(source, destination)

    print("Dataset folders successfully created by breed name and copied all images in corresponding folders")


def main():
    organise_dataset(sys.argv[1])


if __name__ == '__main__':
    main()


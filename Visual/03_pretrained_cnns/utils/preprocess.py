from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.vgg16 import (preprocess_input)

def prepare(df_test, df_train, df_val, target_size, batch_size):

    train_datagen = ImageDataGenerator(preprocessing_function = preprocess_input)

    train_images = train_datagen.flow_from_dataframe(
        dataframe = df_train,
        x_col = 'image_path',
        y_col = 'class_label',
        target_size = target_size,
        batch_size = batch_size,
        subset = 'training'
    )

    val_datagen = ImageDataGenerator(preprocessing_function = preprocess_input)

    val_images = val_datagen.flow_from_dataframe(
        dataframe = df_val,
        x_col = 'image_path',
        y_col = 'class_label',
        target_size = target_size,
        batch_size = batch_size
    )

    test_datagen = ImageDataGenerator(preprocessing_function = preprocess_input)

    test_images = val_datagen.flow_from_dataframe(
        dataframe = df_test,
        x_col = 'image_path',
        y_col = 'class_label',
        target_size = target_size,
        batch_size = batch_size,
        shuffle = False
    )
    return train_images, val_images, test_images
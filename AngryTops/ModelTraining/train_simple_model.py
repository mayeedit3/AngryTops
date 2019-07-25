"""
Train the simplest model. Mostly Use this script for testing
Meant to be run from the parent directory
"""
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import os
import sys
import pickle
from AngryTops.features import *
from AngryTops.ModelTraining.models import models, custom_metrics
from AngryTops.ModelTraining.plotting_helper import plot_history
from AngryTops.ModelTraining.FormatInputOutput import get_input_output
from tensorflow.keras.utils import plot_model
from tensorflow.keras.backend import manual_variable_initialization
manual_variable_initialization(True)

print(tf.__version__)
print(tf.test.gpu_device_name())

def train_model(model_name, train_dir, csv_file, log_training=True, load_model=False, **kwargs):
    """
    Trains a DNN model.
    ============================================================================
    INPUTS:
    Model_name: The name of the mode in models.py
    train_dir: Name of the folder to save the training info + model
    csv_file: The csv file to read data from.
    EPOCHES: # of EPOCHES to train
    learn_rate: Learn rate for neural network.
    scaling: Choose between 'standard' or 'minmax' scaling of input and outputs
    rep: The representation of the data. ie. pxpypz vs ptetaphiM vs ...
    multi_input: True if the model is a multi_input model. False otherwise.
    sort_jets: True or False. Sort jets by first btag, then Mass.
    shuffle: If in kwargs.keys, will shuffle the training/testing data.
    """
    # CONSTANTS
    if 'retrain' in kwargs.keys():
        train_dir = "PostTraining_Analysis/models/{0}".format(train_dir)
        checkpoint_dir = "{}/checkpoints".format(train_dir)
    else:
        train_dir = "../CheckPoints/{}".format(train_dir)
        checkpoint_dir = "{}/checkpoints".format(train_dir)
    print("Saving files in: {}".format(train_dir))
    checkpoint_path = tf.train.latest_checkpoint(checkpoint_dir)
    print("Checkpoint Path: ", checkpoint_path)
    EPOCHES = kwargs["EPOCHES"]
    BATCH_SIZE = 32
    try:
        log = open("{}/log.txt".format(train_dir), 'w')
    except Exception as e:
        os.mkdir(train_dir)
        log = open("{}/log.txt".format(train_dir), 'w')
    if log_training:
        sys.stdout = log

    ###########################################################################
    # LOADING / PRE-PROCESSING DATA
    (training_input, training_output), (testing_input, testing_output), \
    (jets_scalar, lep_scalar, output_scalar), (event_training, event_testing) \
                        = get_input_output(input_filename=csv_file, **kwargs)

    ###########################################################################
    # BUILDING / TRAINING MODEL
    model = models[model_name](**kwargs)
    # Load previously trained model if it exists
    if load_model:
        try:
            model = tf.keras.models.load_model("{}/simple_model.h5".format(train_dir),
                                               custom_objects=custom_metrics)
            model.load_weights(checkpoint_path)
            print("Loaded weights from previous training session")
            print("Loaded weights from previous training session", file=sys.stderr)
        except Exception as e:
            print(e)
            print(e, file=sys.stderr)

    print(model.summary())

    filepath = checkpoint_dir + "/weights-improvement-{epoch:02d}.ckpt"
    print("Checkpoints saved in: ", filepath)
    cp_callback = ModelCheckpoint(filepath, save_weights_only=True, verbose=1)
    early_stopping = EarlyStopping(monitor='val_loss', patience=0)
    try:
        history = model.fit(training_input, training_output,  epochs=EPOCHES,
                            batch_size=BATCH_SIZE, validation_split=0.1,
                            callbacks = [cp_callback, early_stopping]
                            )
    except KeyboardInterrupt:
        print("Training_inerrupted")
        print("Training_inerrupted", file=sys.stderr)
        history = None

    ###########################################################################
    # SAVING MODEL, TRAINING HISTORY AND SCALARS
    model.save('{}/simple_model.h5'.format(train_dir))
    model.save_weights('{}/model_weights.h5'.format(train_dir))
    plot_model(model, to_file='{}/model.png'.format(train_dir))

    scaler_filename = "{}/scalers.pkl".format(train_dir)
    with open( scaler_filename, "wb" ) as file_scaler:
      pickle.dump(jets_scalar, file_scaler, protocol=2)
      pickle.dump(lep_scalar, file_scaler, protocol=2)
      pickle.dump(output_scalar, file_scaler, protocol=2)
    print("INFO: scalers saved to file:", scaler_filename)
    print("INFO: scalers saved to file:", scaler_filename, file=sys.stderr)

    ###########################################################################
    # EVALUATING MODEL AND MAKE PREDICTIONS
    # Evaluating model and saving the predictions
    try:
        test_acc = model.evaluate(testing_input, testing_output)
        print('\nTest accuracy:', test_acc)
        print('\nTest accuracy:', test_acc, file=sys.stderr)
    except Exception as e:
        print(e)
    predictions = model.predict(testing_input)
    if kwargs['multi_input']:
        np.savez("{}/predictions".format(train_dir), lep=testing_input[0], jet=testing_input[1],
                                      true=testing_output, pred=predictions, events=event_testing)
    else:
        np.savez("{}/predictions".format(train_dir), input=testing_input,
                                      true=testing_output, pred=predictions, events=event_testing)

    if history is not None:
        for key in history.history.keys():
            np.savez("{0}/{1}.npz".format(train_dir, key),
                            epoches=history.epoch, loss=history.history[key])
        print("Keys: ", history.history.keys())
        plot_history(history, train_dir)

    # for layer in model.layers:
    #     g=layer.get_config()
    #     h=layer.get_weights()
    #     print (g)
    #     print (h)
    sys.stdout = sys.__stdout__
    log.close()


if __name__ == "__main__":
    print("Compiled")

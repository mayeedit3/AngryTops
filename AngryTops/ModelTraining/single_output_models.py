"""
Contains single-output model architectures
"""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import *
from tensorflow.keras.regularizers import *
import sys
from AngryTops.features import *

def single0(**kwargs):
    """A denser version of model_multi"""
    reg_weight = 0.0
    rec_weight = 0.0
    if 'reg_weight' in kwargs.keys(): reg_weight = kwargs['reg_weight']
    if 'rec_weight' in kwargs.keys(): rec_weight = kwargs['rec_weight']
    if 'dense_act1' in kwargs.keys(): dense_act1 = kwargs['dense_act1']
    learn_rate = kwargs['learn_rate']

    input_jets = Input(shape = (20,), name="input_jets")
    input_lep = Input(shape=(5,), name="input_lep")
    # Jets
    x_jets = Reshape(target_shape=(5,4))(input_jets)
    x_jets = LSTM(50, return_sequences=True,
                  kernel_regularizer=l2(reg_weight),
                  recurrent_regularizer=l2(rec_weight))(x_jets)
    x_jets = LSTM(25, return_sequences=False,
                  kernel_regularizer=l2(reg_weight),
                  recurrent_regularizer=l2(rec_weight))(x_jets)
    x_jets = Dense(20, activation='relu')(x_jets)
    x_jets = keras.Model(inputs=input_jets, outputs=x_jets)

    # Lep
    x_lep = keras.Model(inputs=input_lep, outputs=input_lep)

    # Combine them
    combined = concatenate([x_lep.output, x_jets.output], axis=1)

    # Apply some more layers to combined data set
    final = Dense(25, activation='relu')(combined)
    final = Dense(10, activation="relu")(final)
    final = Dense(5, activation="elu")(final)
    final = Dense(1, activation='linear')(final)

    # Make final model
    model = keras.Model(inputs=[x_lep.input, x_jets.input], outputs=final)

    optimizer = tf.keras.optimizers.Adam(learn_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])

    return model

def single1(**kwargs):
    """Predicts only ONE output variable"""
    dense_act1 = 'relu'
    reg_weight = 0.0
    rec_weight = 0.0
    if 'reg_weight' in kwargs.keys(): reg_weight = kwargs['reg_weight']
    if 'rec_weight' in kwargs.keys(): rec_weight = kwargs['rec_weight']
    if 'dense_act1' in kwargs.keys(): dense_act1 = kwargs['dense_act1']
    learn_rate = kwargs['learn_rate']

    input_jets = Input(shape = (20,), name="input_jets")
    input_lep = Input(shape=(5,), name="input_lep")
    # Jets
    x_jets = Reshape(target_shape=(5,4))(input_jets)
    x_jets = LSTM(50, return_sequences=False,
                  kernel_regularizer=l2(reg_weight),
                  recurrent_regularizer=l2(rec_weight))(x_jets)
    x_jets = Dense(30, activation='relu')(x_jets)
    x_jets = keras.Model(inputs=input_jets, outputs=x_jets)

    # Lep
    x_lep = keras.Model(inputs=input_lep, outputs=input_lep)

    # Combine them
    combined = concatenate([x_lep.output, x_jets.output], axis=1)

    # Apply some more layers to combined data set
    final = Dense(40, activation=dense_act1)(combined)
    final = Dense(18, activation='elu')(final)
    final = Dense(6, activation='elu')(final)
    final = Dense(6, activation='elu')(final)
    final = Dense(1, activation="linear")(final)

    # Make final model
    model = keras.Model(inputs=[x_lep.input, x_jets.input], outputs=final)

    optimizer = tf.keras.optimizers.Adam(learn_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])

    return model

def single2(**kwargs):
    """Predicts only ONE output variable. Uses only dense layers"""
    learn_rate = kwargs['learn_rate']
    input_jets = Input(shape = (20,), name="input_jets")
    input_lep = Input(shape=(5,), name="input_lep")

    # Jets
    x_jets = Dense(50, activation='relu')(input_jets)
    x_jets = Dense(25, activation='relu')(x_jets)
    x_jets = Dense(25, activation='relu')(x_jets)
    x_jets = BatchNormalization()(x_jets)
    x_jets = Dense(20)(x_jets)
    x_jets = keras.Model(inputs=input_jets, outputs=x_jets)

    # Lep
    x_lep = Dense(20, activation='relu')(input_lep)
    x_lep = Dense(10, activation='relu')(x_lep)
    x_lep = Dense(10)(x_lep)
    x_lep = keras.Model(inputs=input_lep, outputs=x_lep)

    # Combine them
    combined = concatenate([x_lep.output, x_jets.output], axis=1)

    # Apply some more layers to combined data set
    final = Dense(15, activation='relu')(combined)
    final = Dense(10, activation="relu")(final)
    final = Dense(5, activation="elu")(final)
    final = Dense(1, activation='linear')(final)

    # Make final model
    model = keras.Model(inputs=[x_lep.input, x_jets.input], outputs=final)
    optimizer = tf.keras.optimizers.Adam(learn_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])

    return model

def single3(**kwargs):
    """Predicts only ONE output variable. Uses only dense layers"""
    learn_rate = kwargs['learn_rate']
    input_jets = Input(shape = (20,), name="input_jets")
    input_lep = Input(shape=(5,), name="input_lep")

    # Jets
    x_jets = Dense(20, activation='relu')(input_jets)
    x_jets = Dense(20, activation='relu')(x_jets)
    x_jets = Reshape(target_shape=(5,4))(x_jets)
    x_jets = LSTM(20, return_sequences=False)(x_jets)
    x_jets = BatchNormalization()(x_jets)
    x_jets = BatchNormalization()(x_jets)
    x_jets = keras.Model(inputs=input_jets, outputs=x_jets)

    # Lep
    x_lep = Dense(20, activation='relu')(input_lep)
    x_lep = Dense(15, activation='relu')(x_lep)
    x_lep = Dense(10)(x_lep)
    x_lep = BatchNormalization()(x_lep)
    x_lep = keras.Model(inputs=input_lep, outputs=x_lep)

    # Combine them
    combined = concatenate([x_lep.output, x_jets.output], axis=1)

    # Apply some more layers to combined data set
    final = Dense(30, activation='relu', kernel_regularizer=l2(0))(combined)
    final = Dense(25, activation="relu", kernel_regularizer=l2(0))(final)
    final = Dense(20, activation="relu", kernel_regularizer=l2(0))(final)
    final = BatchNormalization()(final)
    final = Dense(10, activation="relu", kernel_regularizer=l2(0))(final)
    final = Dense(5, activation="elu", kernel_regularizer=l2(0))(final)
    final = Dense(1, activation='linear')(final)

    # Make final model
    model = keras.Model(inputs=[x_lep.input, x_jets.input], outputs=final)
    optimizer = tf.keras.optimizers.Adam(learn_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])

    return model

def single4(**kwargs):
    """Predicts only ONE output variable. Uses only dense layers"""
    learn_rate = kwargs['learn_rate']
    input_jets = Input(shape = (20,), name="input_jets")
    input_lep = Input(shape=(5,), name="input_lep")

    # Jets
    x_jets = Dense(25, activation='relu')(input_jets)
    x_jets = Dense(20, activation='relu')(x_jets)
    x_jets = Dense(20, activation='relu')(x_jets)
    x_jets = Reshape(target_shape=(5,4))(x_jets)
    x_jets = BatchNormalization()(x_jets)
    x_jets = LSTM(30, return_sequences=False)(x_jets)
    x_jets = keras.Model(inputs=input_jets, outputs=x_jets)

    # Lep
    x_lep = Dense(20, activation='relu')(input_lep)
    x_lep = Dense(10, activation='relu')(x_lep)
    x_lep = BatchNormalization()(x_lep)
    x_lep = Dense(10, activation='linear')(x_lep)
    x_lep = keras.Model(inputs=input_lep, outputs=x_lep)

    # Combine them
    combined = concatenate([x_lep.output, x_jets.output], axis=1)

    # Apply some more layers to combined data set
    final = Dense(30, activation='relu', kernel_regularizer=l2(10e-5))(combined)
    final = Reshape(target_shape=(6,5))(final)
    final = LSTM(25, return_sequences=False, kernel_regularizer=l2(10e-5))(final)
    final = Dense(20, activation="relu",  kernel_regularizer=l2(10e-5))(final)
    final = Dense(10, activation="relu",  kernel_regularizer=l2(10e-5))(final)
    final = Dense(5, activation="elu",  kernel_regularizer=l2(10e-5))(final)
    final = Dense(1, activation='linear')(final)

    # Make final model
    model = keras.Model(inputs=[x_lep.input, x_jets.input], outputs=final)
    optimizer = tf.keras.optimizers.Adam(learn_rate)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])

    return model

################################################################################
# List of all models
single_models = {'single0':single0, 'single1':single1, 'single2':single2,
                 'single3':single3, 'single4':single4}
################################################################################

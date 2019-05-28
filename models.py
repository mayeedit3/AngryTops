import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.regularizers import l2

from features import *

n_features_input = 6
n_target_features = 6

def model0():
    """
    Create a simple RNN with one recurrent layer
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    model = keras.Sequential()
    model.add(layers.Dense(36, activation='relu', input_shape=(36,)))
    model.add(layers.Reshape(target_shape=(6,6)))
    model.add(layers.SimpleRNN(30, return_sequences=True))
    model.add(layers.Flatten())
    model.add(layers.Dense(24))
    model.add(layers.Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

################################################################################

def model1():
    """
    Create a simple RNN with L2 regularizers and dropout layers
    """
    model = keras.Sequential()
    model.add(layers.Dense(36, activation='relu', input_shape=(36,), kernel_regularizer=l2()))
    model.add(layers.Dropout(0.2))
    model.add(layers.Reshape(target_shape=(6,6)))
    model.add(layers.LSTM(30, return_sequences=True, kernel_regularizer=l2()))
    model.add(layers.Dropout(0.2))
    model.add(layers.Flatten())
    model.add(layers.Dense(24))
    model.add(layers.Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model


################################################################################

def model2():
    """
    Create a simple RNN with L2 regularizers and dropout layers
    """
    model = keras.Sequential()
    model.add(layers.Dense(36, activation='relu', input_shape=(36,)))
    model.add(layers.Dropout(0.2))
    model.add(layers.Reshape(target_shape=(6,6)))
    model.add(layers.LSTM(30, return_sequences=True, kernel_regularizer=l2()))
    model.add(layers.Flatten())
    model.add(layers.Dense(24))
    model.add(layers.Dense(24))
    model.add(layers.Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

################################################################################

def model3():
    """
    Create a simple RNN with L2 regularizers and dropout layers
    """
    model = keras.Sequential()
    model.add(layers.Dense(36, activation='relu', input_shape=(36,)))
    model.add(layers.Dropout(0.2))
    model.add(layers.Reshape(target_shape=(6,6)))
    model.add(layers.LSTM(36, return_sequences=True))
    model.add(layers.LSTM(36, return_sequences=True))
    model.add(layers.Flatten())
    model.add(layers.Dense(24))
    model.add(layers.Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def model4():
    """
    Create a simple RNN with L2 regularizers and dropout layers
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    model = keras.Sequential()
    model.add(layers.Dense(36, activation='relu', input_shape=(36,)))
    model.add(layers.Dropout(0.1))
    model.add(layers.Reshape(target_shape=(6,6)))
    model.add(layers.LSTM(30, return_sequences=True, kernel_regularizer=l2(0.01)))
    model.add(layers.LSTM(30, return_sequences=True, kernel_regularizer=l2(0.01)))
    model.add(layers.Flatten())
    model.add(layers.Dense(24))
    model.add(layers.Dense(24))
    model.add(layers.Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def model5():
    """
    Create a simple RNN with one recurrent layer
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    model = keras.Sequential()
    model.add(layers.Dense(36, activation='relu', input_shape=(36,)))
    model.add(layers.Reshape(target_shape=(6,6)))
    model.add(layers.LSTM(30, return_sequences=True))
    model.add(layers.Flatten())
    model.add(layers.Dense(24))
    model.add(layers.Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def model6():
    """
    Create a simple RNN with one recurrent layer
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    model = keras.Sequential()
    model.add(layers.Dense(36, activation='relu', input_shape=(36,)))
    model.add(layers.Reshape(target_shape=(6,6)))
    model.add(layers.SimpleRNN(30, return_sequences=True))
    model.add(layers.SimpleRNN(30, return_sequences=True))
    model.add(layers.Flatten())
    model.add(layers.Dense(24))
    model.add(layers.Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def model7():
    """
    Create a simple RNN with one recurrent layer
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    model = keras.Sequential()
    model.add(layers.Dense(36, activation='relu', input_shape=(36,)))
    model.add(layers.Reshape(target_shape=(6,6)))
    model.add(layers.SimpleRNN(100, return_sequences=True))
    model.add(layers.Flatten())
    model.add(layers.Dense(24))
    model.add(layers.Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def model8():
    """
    Create a simple RNN with one recurrent layer
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    model = keras.Sequential()
    model.add(layers.Dense(36, activation='relu', input_shape=(36,)))
    model.add(layers.Reshape(target_shape=(6,6)))
    model.add(layers.SimpleRNN(100, return_sequences=True))
    model.add(layers.SimpleRNN(100, return_sequences=True))
    model.add(layers.Flatten())
    model.add(layers.Dense(24))
    model.add(layers.Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

def model9():
    """
    Create a simple RNN with one recurrent layer
    """
    # Questions:
    # 1. Originally there was a TimeDIstributed Layer. I think this was
    # unceccessary
    # The return_sequences=True argument ==> Not sure what this does
    # I simplified the model significantly => Reduced it to one recurrent layer
    model = keras.Sequential()
    model.add(layers.Dense(36, activation='relu', input_shape=(36,)))
    model.add(layers.Reshape(target_shape=(6,6)))
    model.add(layers.SimpleRNN(30, return_sequences=True), kernel_regularizer=l2(0.01))
    model.add(layers.Flatten())
    model.add(layers.Dense(24))
    model.add(layers.Reshape(target_shape=(6,4)))

    optimizer = tf.keras.optimizers.RMSprop()
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
    return model

################################################################################
# List of all models
models = [model0, model1, model2, model3, model4, model5, model6, model7,
            model8, model9]
################################################################################


# ################################################################################
#
# def create_model_rnn():
#    inshape   = (6, 6)
#
#    print("INFO: building model: input shape: {}".format(inshape))
#
#    input = Input( shape=inshape )
#    dropout = 0.01
#    model = keras.Sequential()
#
#    model.add(layers.TimeDistributed( Dense(100), input_shape=inshape))
#    model.add(layers.LSTM(80, return_sequences=True))
#    model.add(layers.LSTM(80, return_sequences=True))
#    model.add(layers.LSTM(80, return_sequences=True))
#    model.add(layers.LSTM(50, return_sequences=True))
#    model.add(layers.LSTM(50, return_sequences=True))
#    model.add(layers.LSTM(50, return_sequences=True))
#    model.add(layers.Dense(36))
#    model.add(layers.Reshape(target_shape=(5,6)))
#
#    model.compile(optimizer=optimizer, loss='mse', metrics=['mae', 'mse'])
#
#    return model
#
# ################################################################################
#
# def create_model_multi():
#    print("INFO: building model: (W_lep,b_lep,t_lep,W_had,b_had,t_had)")
#    print("Model not done")
#    return
# ################################################################################


   # input_jets = Input( shape=shape_jets, name='input_jets' )
   # input_lep  = Input( shape=shape_lep,  name='input_lept' )
   #
   # x_W_lep = Dense(30)(input_lep)
   # x_W_lep = Dense(30, activation="relu")(x_W_lep)
   # x_W_lep = Dense(20, activation="relu")(x_W_lep)
   # x_W_lep = Dense(10, activation="relu")(x_W_lep)
   # x_W_lep = Dense(6)(x_W_lep)
   # x_W_lep_out = Dense(3, name='W_lep_out')(x_W_lep)
   #
   # # shared layers
   # x_jets = TimeDistributed( Dense(100), input_shape=(5,6) )(input_jets)
   # x_jets = LSTM( 100, return_sequences=True)(x_jets)
   # x_jets = LSTM(  80, return_sequences=True)(x_jets)
   # x_jets = LSTM(  50, return_sequences=False)(x_jets)
   #
   # x_b_had = Dense(30, activation="tanh")(x_jets)
   # x_b_had = Dense(20, activation="tanh")(x_b_had)
   # x_b_had = Dense(10, activation="tanh")(x_b_had)
   # x_b_had_out = Dense(3, name="b_had_out")(x_b_had)
   #
   # x_b_lep = Dense(30, activation="tanh")(x_jets)
   # x_b_lep = Dense(20, activation="tanh")(x_b_lep)
   # x_b_lep = Dense(10, activation="tanh")(x_b_lep)
   # x_b_lep_out = Dense(3, name="b_lep_out")(x_b_lep)
   #
   # x_W_had = Dense(30, activation="tanh")(x_jets)
   # x_W_had = Dense(20, activation="tanh")(x_W_had)
   # x_W_had = Dense(10, activation="tanh")(x_W_had)
   # x_W_had_out = Dense(3, name="W_had_out")(x_W_had)
   #
   # model = Model(inputs=[input_jets,
   #                       input_lep],
   #               outputs=[x_W_lep_out, x_W_had_out,
   #                        x_b_lep_out, x_b_had_out ] )
   #                        #x_t_lep_out, x_t_had_out] )
   #
   # model.compile( optimizer='adam', loss='mean_squared_error' )

import numpy as np
from keras.models import load_model, Model
from keras.layers import Dense, Activation, Dropout, Input, LSTM, Reshape, Lambda, RepeatVector
from keras.initializers import glorot_uniform
from keras.optimizers import Adam
from keras import backend as K


class ModelCreator:
	def __init__(self, n_X, n_Y, n_a=64):
		self.n_X = n_X
		self.n_Y = n_Y
		self.n_a = n_a
		# Used in Step 2.B of djmodel(), below
		self.reshapor = Reshape((1, n_X))
		self.LSTM_cell = LSTM(n_a, return_state=True)         # Used in Step 2.C
		self.densor = Dense(n_Y)     # Used in Step 2.D

	def djmodel(self, Tx, n_a, n_X, n_Y):
		"""
		Implement the model

		Arguments:
		Tx -- length of the sequence in a corpus
		n_a -- the number of activations used in our model
		n_X -- number of features of x
		n_Y -- number of features of y

		Returns:
		model -- a keras instance model with n_a activations
		"""

		# Define the input layer and specify the shape
		X = Input(shape=(Tx, n_X))

		# Define the initial hidden state a0 and initial cell state c0
		# using `Input`
		a0 = Input(shape=(n_a,), name='a0')
		c0 = Input(shape=(n_a,), name='c0')
		a = a0
		c = c0

		### START CODE HERE ###
		# Step 1: Create empty list to append the outputs while you iterate (â‰ˆ1 line)
		outputs = list()

		# Step 2: Loop
		for t in range(Tx):

			# Step 2.A: select the "t"th time step vector from X.
			x = Lambda(lambda X: X[:, t, :])(X)
			# Step 2.B: Use self.reshapor to reshape x to be (1, n_X) (â‰ˆ1 line)
			x = self.reshapor(x)
			# Step 2.C: Perform one step of the LSTM_cell
			a, _, c = self.LSTM_cell(inputs=x, initial_state=[a, c])
			# Step 2.D: Apply densor to the hidden state output of LSTM_Cell
			out = self.densor(a)
			# Step 2.E: add the output to "outputs"
			outputs.append(out)

		# Step 3: Create model instance
		model = Model(inputs=[X, a0, c0], outputs=outputs)
		### END CODE HERE ###

		return model


	def ball_inference_model(self, LSTM_cell, densor, n_X=44, n_Y=3, n_a=64, Ty=60):
		"""
		Uses the trained "LSTM_cell" and "densor" from model() to generate a sequence of values.

		Arguments:
		LSTM_cell -- the trained "LSTM_cell" from model(), Keras layer object
		densor -- the trained "densor" from model(), Keras layer object
		n_X -- number of features of x
		n_Y -- number of features of y
		n_a -- number of units in the LSTM_cell
		Ty -- integer, number of time steps to generate

		Returns:
		inference_model -- Keras model instance
		"""

		# Define the input layer and specify the shape
		X = Input(shape=(Ty, n_X))

		# Define the initial hidden state a0 and initial cell state c0
		# using `Input`
		a0 = Input(shape=(n_a,), name='a0')
		c0 = Input(shape=(n_a,), name='c0')
		a = a0
		c = c0

		### START CODE HERE ###
		# Step 1: Create empty list to append the outputs while you iterate (â‰ˆ1 line)
		outputs = list()

		# Step 2: Loop
		for t in range(Ty):

			# Step 2.A: select the "t"th time step vector from X.
			x = Lambda(lambda X: X[:, t, :])(X)
			# Step 2.B: Use self.reshapor to reshape x to be (1, n_X) (â‰ˆ1 line)
			x = self.reshapor(x)
			# Step 2.C: Perform one step of the LSTM_cell
			a, _, c = self.LSTM_cell(inputs=x, initial_state=[a, c])
			# Step 2.D: Apply densor to the hidden state output of LSTM_Cell
			out = self.densor(a)
			# Step 2.E: add the output to "outputs"
			outputs.append(out)

		# Step 3: Create model instance
		model = Model(inputs=[X, a0, c0], outputs=outputs)

		### END CODE HERE ###

		return model


	def predict(self, inference_model, X_initializer, a_initializer,
				c_initializer):
		"""
		Predicts the next value of values using the inference model.

		Arguments:
		inference_model -- Keras model instance for inference time
		X_initializer -- numpy array of shape (m, Ty, n_X)
		a_initializer -- numpy array of shape (1, n_a), initializing the hidden state of the LSTM_cell
		c_initializer -- numpy array of shape (1, n_a), initializing the cell state of the LSTM_cel

		Returns:
		y_pres -- numpy-array of shape (Ty, n_Y), matrix of vectors representing the values generated
		"""

		### START CODE HERE ###
		# Step 1: Use your inference model to predict an output sequence given X_initializer, a_initializer and c_initializer.
		Y_preds = inference_model.predict(
			[X_initializer, a_initializer, c_initializer])

		return Y_preds
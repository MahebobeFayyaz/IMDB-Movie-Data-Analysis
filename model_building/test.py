import streamlit as st
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

st.write("Streamlit + RNN environment works!")

model = Sequential()
model.add(Embedding(1000, 32, input_length=10))
model.add(SimpleRNN(16))
model.add(Dense(1, activation='sigmoid'))

st.write("Model built successfully!")

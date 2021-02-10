import tensorflow as tf
import numpy as np
import pandas as pd

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)

keras = tf.keras

HANGUL_FIRST = list('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ')
HANGUL_MIDDLE = list('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
HANGUL_LAST = list(' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')
HANGUL_CODE = list('\0\1 ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')

MAX_LENGTH = 7 * 3
TOKEN_SIZE = len(HANGUL_CODE) + 1
EPOCH = 300


def korean_separation(string):
    li = []
    for w in list(string.strip()):
        if '가' <= w <= '힣':
            ch1 = (ord(w) - ord('가')) // 588
            ch2 = ((ord(w) - ord('가')) - (588 * ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588 * ch1) - 28 * ch2
            li.append((HANGUL_FIRST[ch1], HANGUL_MIDDLE[ch2], HANGUL_LAST[ch3]))
    return li


def str_to_code(string):
    sep = korean_separation(string)
    li = []
    for i in sep:
        li.append(HANGUL_CODE.index(i[0]) + 1)
        li.append(HANGUL_CODE.index(i[1]) + 1)
        li.append(HANGUL_CODE.index(i[2]) + 1)
    return li


def code_to_str(code):
    s = ''
    for (a, b, c) in zip(code[::3], code[1::3], code[2::3]):
        try:
            s += chr(0xac00 + 28 * 21 * HANGUL_FIRST.index(HANGUL_CODE[a - 1]) + 28 * HANGUL_MIDDLE.index(
                HANGUL_CODE[b - 1]) + HANGUL_LAST.index(HANGUL_CODE[c - 1]))
        except:
            pass
    return s


def load_data(filename):
    data = pd.read_csv(filename, names=['src', 'tar'], sep=',')
    return (list(data.src), list(data.tar))


def build_model(input, output):
    encoder_input = []
    decoder_input = []
    decoder_target = []

    for i in input:
        encoder_input.append(str_to_code(i))

    for i in output:
        li = str_to_code(i)
        li.append(2)
        decoder_target.append(li.copy())
        li.insert(0, 1)
        decoder_input.append(li)

    encoder_input = keras.preprocessing.sequence.pad_sequences(encoder_input, maxlen=TOKEN_SIZE, padding='post')
    decoder_input = keras.preprocessing.sequence.pad_sequences(decoder_input, maxlen=TOKEN_SIZE, padding='post')
    decoder_target = keras.preprocessing.sequence.pad_sequences(decoder_target, maxlen=TOKEN_SIZE, padding='post')

    encoder_input = keras.utils.to_categorical(encoder_input, num_classes=TOKEN_SIZE)
    decoder_input = keras.utils.to_categorical(decoder_input, num_classes=TOKEN_SIZE)
    decoder_target = keras.utils.to_categorical(decoder_target, num_classes=TOKEN_SIZE)

    encoder_inputs = keras.layers.Input(shape=(None, TOKEN_SIZE))
    encoder_lstm = keras.layers.LSTM(units=256, return_state=True)
    encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)

    encoder_states = [state_h, state_c]
    decoder_inputs = keras.layers.Input(shape=(None, TOKEN_SIZE))
    decoder_lstm = keras.layers.LSTM(units=256, return_sequences=True, return_state=True)
    decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)

    decoder_softmax_layer = keras.layers.Dense(TOKEN_SIZE, activation='softmax')
    decoder_outputs = decoder_softmax_layer(decoder_outputs)

    model = keras.models.Model([encoder_inputs, decoder_inputs], decoder_outputs)
    model.compile(optimizer="rmsprop", loss="categorical_crossentropy")
    model.fit(x=[encoder_input, decoder_input], y=decoder_target, batch_size=64, epochs=EPOCH)

    encoder_model = keras.models.Model(inputs=encoder_inputs, outputs=encoder_states)
    decoder_state_input_h = keras.layers.Input(shape=(256,))
    decoder_state_input_c = keras.layers.Input(shape=(256,))
    decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
    decoder_outputs, state_h, state_c = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
    decoder_states = [state_h, state_c]
    decoder_outputs = decoder_softmax_layer(decoder_outputs)
    decoder_model = keras.models.Model(inputs=[decoder_inputs] + decoder_states_inputs,
                                       outputs=[decoder_outputs] + decoder_states)

    return (encoder_model, decoder_model)


def predict(st, model):
    input_seq = np.array([keras.utils.to_categorical(str_to_code(st), num_classes=TOKEN_SIZE)])
    (encoder_model, decoder_model) = model

    states_value = encoder_model.predict(input_seq)
    target_seq = np.zeros((1, 1, TOKEN_SIZE))
    target_seq[0, 0, 1] = 1.
    stop_condition = False
    decoded = []

    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)

        sampled_token = np.argmax(output_tokens[0, -1, :])

        if sampled_token == 2 or len(decoded) > MAX_LENGTH:
            stop_condition = True
        else:
            decoded.append(sampled_token)

        target_seq = np.zeros((1, 1, TOKEN_SIZE))
        target_seq[0, 0, sampled_token] = 1.
        states_value = [h, c]
    print(decoded)
    return code_to_str(decoded)


model = build_model(*load_data('data.csv'))
print(predict('갓', model))

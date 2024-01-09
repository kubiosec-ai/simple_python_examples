import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GRU, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np


def generate_text(seed_text, next_words, model, max_sequence_len):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predictions = model.predict(token_list, verbose=0)
        predicted = np.argmax(predictions, axis=-1)[0]
        
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text



# Sample text (you can replace this with a larger dataset)
text = f"""
Artificial Intelligence (AI) is a broad branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence. AI is an interdisciplinary science with multiple approaches, but advancements in machine learning and deep learning are creating a paradigm shift in virtually every sector of the tech industry.

AI systems are powered by algorithms, using techniques such as machine learning, deep learning, and rules-based systems. Machine learning algorithms feed computer data to AI systems, using statistical techniques to enable AI systems to learn. Through machine learning, AI systems get progressively better at tasks without having to be specifically programmed for them. Deep learning, a subset of machine learning, structures algorithms in layers to create an "artificial neural network" that can learn and make intelligent decisions on its own.

AI is a significant part of the technology industry. Research associated with AI is highly technical and specialized. The core problems of artificial intelligence include programming computers for certain traits such as knowledge, reasoning, problem-solving, perception, learning, planning, and the ability to manipulate and move objects. Long-term goals of AI research include achieving Creativity, Social Intelligence, and General (Human Level) Intelligence.

AI has been used to develop and advance numerous fields and industries, including finance, healthcare, education, transportation, and more. In finance, AI technologies can be used to identify which transactions are likely to be fraudulent, adopt fast and accurate credit scoring, as well as automate manually intense data management tasks. AI in healthcare is being used for dosing drugs and different treatment in patients, and for surgical procedures in the operating room.

The use of AI in education makes a system that is more adaptable to the needs of students. Virtual tutors and personalized learning environments are being developed to cater to the individual needs of students. AI is also being used in the transportation industry to manage traffic, predict flight delays, and make ocean shipping safer and more efficient.

AI is also used in the daily operations of many companies. It is used in automating tasks for low-level employees to higher-ranking officials. AI technologies help in scheduling trains, assessing business risk, predicting maintenance, and improving energy efficiency, among many other uses.

AI is an integral part of the future of technology. It is being used to help solve many big and small problems, from cancer to customer experience. AI is expected to become a part of daily life in many different ways. In the future, AI will become a little more sophisticated and might be able to perform more complex tasks. AI is also expected to be used in the analysis of interactions to determine underlying connections and insights, to help predict demand for services like hospitals enabling authorities to make better decisions about resource utilization, and to detect the changing patterns of customer behavior by analyzing data in near real-time, driving revenues and enhancing personalized experiences.

The AI of the future is expected to be more than just a tool that executes commands. It is expected to understand, reason, plan, and communicate in natural language. This is not a new idea – AI researchers have been pursuing this goal for decades, and the pursuit is more realistic now due to the recent breakthroughs in machine learning and neural networks.

The field of AI has been evolving rapidly, with breakthroughs in machine learning, neural networks, and deep learning. These technologies are being used to develop more advanced AI systems that can understand, learn, predict, adapt, and potentially operate autonomously. Systems that do visual applications can recognize faces in images and understand the content. Systems that understand speech and language can comprehend and respond to spoken language naturally.

However, the implementation of AI raises ethical issues. For example, AI systems can be biased if they are trained on data that is not representative of the broader population, or if the systems are designed in a way that reflects existing prejudices. The development of AI also raises concerns about job displacement, as AI systems can automate tasks previously done by humans.

In conclusion, AI is a rapidly evolving technology with the potential to revolutionize many aspects of our lives. Its development and implementation come with challenges and concerns, but its potential benefits are immense. AI is not just a tool for automating routine tasks, but a technology that can potentially understand, reason, and interact with the world in a human-like way. The future of AI is full of exciting possibilities and is a field that will continue to grow and develop in the coming years.


"""
# Tokenization and sequence generation
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in text.split('.'):
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequences.append(n_gram_sequence)

# Pad sequences
max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

# Create predictors and label
predictors, label = input_sequences[:,:-1], input_sequences[:,-1]
label = tf.keras.utils.to_categorical(label, num_classes=total_words)

# Model
model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequence_len-1))
model.add(GRU(150, return_sequences=True))
model.add(GRU(100))
model.add(Dense(total_words, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(predictors, label, epochs=100, verbose=1)


print(generate_text("AI and ML are", 30, model, max_sequence_len))

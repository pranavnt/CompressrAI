# Compressr AI
## Problem Description
We wanted to solve the problem of the inaccessibility of remote education. After further research, I learned that Zoom/Teams/GTM had a minimum upload speed of 2 megabits/second. While many of us are able to meet that threshold, many people globally are not. This excludes them from virtual learning, which can significantly impact their future. Essentially, there needed to be a way to further optimize live video footage to make remote learning more accessible. 

## What it does
Our product, Compressr AI, democratizes access to virtual learning to those without quality internet via AI-powered video compression. 

## How I built it
I used Python to build the models. Specifically, I used Tensorflow, NumPy, Pillow, and flask to build this. I used Pillow to load the images, NumPy for basic preprocessing, Tensorflow to build the autoencoder, and Flask to create an API. 

Autoencoders are a deep learning algorithm often used for synthetic data generation, file compression, and a lot more. They are comprised of two seperate networks that can function separately (the encoder and the decoder). The encoder "encodes" the input, and reduced the number of dimensins. The decoder network decodes the encoded input from the autoencoder, to reconstruct the input. I trained the autoencoder with the loss of Mean Squared Error and the Adam Optimizer. Feel free to reach out to me if you have any questions about the architecture of my network or autoencoders in general

## Challenges I ran into
1. I don't have access to a powerful GPU, thus I couldn't train an extremely powerful model due to that limit (given that the hackathon is only for ~12 hours). To solve this, I opted to significantly reduce the resolution to 60x80, and to test my algorithm on that.
2. None of the datasets on this topic were good for what I was trying to do. Thus, a supervised approach to this problem was tough so I opted to use an unsupervised approach (autoencoders are unsupervised).
3. This was my first time working with autoencoders (I've used GANs before), and didn't know much on how they work. It took a lot of Medium articles and academic papers to understand how they work (and the math behind them). 
4. I initially tried using GANs, which I had experience with. However, GANs took a while to run, which would make it impossible for actual implementation. I then switched to autoencoders 
5. Working alone :( I reached out to a few people, but most teams had formed before the hackathon started and not many people were initially interested in my idea. I learned a lot about video editing/production during this hackathon, which I had rarely done before.

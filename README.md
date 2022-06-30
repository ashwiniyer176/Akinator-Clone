# Akinator Clone 

Akinator is a video game developed by French company Elokence. During gameplay, it attempts to determine what fictional or real-life character the player is thinking of by asking a series of questions (like the game Twenty Questions). Akinator's goal is to guess a real or fictional characters. To guess the character the player is thinking, Akinator asks a series of questions and the player can answer with 'Yes',' Don't know', 'No', 'Probably 'and 'Probably' not , then the program determines the best question.

Akinator uses a proprietary algorithm which is not available to the public and also has a larger database of characters than this project currently has. The purpose of this project is to try and break down how Akinator's guessing algorithm works and recreate the same for educational purposes
## Dataset

The data comes from [FiveThirtyEight Comic Characters Dataset](https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-comic-characters-dataset). The data is split into two files, for DC and Marvel, respectively: `dc-wikia-data.csv` and `marvel-wikia-data.csv`. Each file has the following variables:

Variable | Definition
---|---------
`page_id` | The unique identifier for that characters page within the wikia
`name` | The name of the character
`urlslug` | The unique url within the wikia that takes you to the character
`ID` | The identity status of the character (Secret Identity, Public identity, [on marvel only: No Dual Identity])
`ALIGN` | If the character is Good, Bad or Neutral
`EYE` | Eye color of the character
`HAIR` | Hair color of the character
`SEX` | Sex of the character (e.g. Male, Female, etc.)
`GSM` | If the character is a gender or sexual minority (e.g. Homosexual characters, bisexual characters)
`ALIVE` | If the character is alive or deceased
`APPEARANCES` | The number of appareances of the character in comic books (as of Sep. 2, 2014. Number will become increasingly out of date as time goes on.)
`FIRST APPEARANCE` | The month and year of the character's first appearance in a comic book, if available
`YEAR` | The year of the character's first appearance in a comic book, if available

We will be combining the two to give our Akinator clone and additional layer of challenge.

<!-- ## Model(s) Used

This needs to be a description of the model used and a brief overview of how it works in theory (e.g taken of a CNN Model): 

The network architecture used was a basic CNN model, with Max Pooling and ReLU Activation functions. Input images are resized to an optimal size and then fed into the **Convolutional layer**. These images are converted to their pixel values, which can be imagined as a three-dimensional matrix for the purpose of visualization. The **Convolutional layer** has a kernel. This kernel is generally a small matrix of specified kernel size mxnx3 (3 for RGB images). 
<br>

**Rectified Linear Unit (ReLU)** is the activation layer used in CNNs.The activation function is applied to increase non-linearity in the CNN. Images are made of different objects that are not linear to each other.


**Max Pooling:** A limitation of the feature map output of Convolutional Layers is that they record the precise position of features in the input. This means that small movements in the position of the feature in the input image will result in a different feature map. This can happen with re-cropping, rotation, shifting, and other minor changes to the input image. A common approach to addressing this problem from signal processing is called down sampling. This is where a lower resolution version of an input signal is created that still contains the large or important structural elements, without the fine detail that may not be as useful to the task.

## Future Work
Good ideas or strategies that you were not able to implement which you think can help  improve performance. -->

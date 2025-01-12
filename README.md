# Image_Classification_AI_Model-VLG-IITR

Link to Kaggle notebook is pinned in Model_Path file


Model Development

1.	Data Processing:
   
The Dataset was processed in mainly 4 steps

a.	Class Distinction

Having recognised from the previously low scoring models, there were about 10 unknown classes for the model. Here Unknown classes refer to those for which we did not have any visual data. The first step was to recognise which animal classes were they. 
For this, I created a simple python code, that compared the folder names of the ‘train’ dataset with the list of all 50 classes in the classes.txt file, running which gave me the final list on the 10 unknown classes.

b.	Data Loading

Given the large amount of training data, processing it in batches was necessary. Hence, I created a custom dataset class called ‘KnownAnimalDataset’ from the Dataset method of the PyTorch library, ensuring the data is loaded easily and necessary transformations can directly be applied.

c.	Data Augmentation

In the initial stages of the project, one thing I encountered very often was the issue of overfitting. Hence, to tackle that, my aim was to diversify the dataset so that the neuron network is able to recognise the test images on its own rather than strictly seeking out a specific pattern from the training dataset.

The Data Augmentation techniques used in the final model were a result of several hit and trial methods in various libraries. The best ones that I used are namely:

i.	RandomResizedCrop : Crops a part of the image and scales it to the input size.

ii.	RandomHorizontalFlip : Flips the image across the Y-axis to diversify data

iii.	ColorJitter: Gives us the ability to change the colour related settings of images

iv.	RandomRotation: Rotates images to a certain angle

v.	RandomGrayscale: Randomly turns image to Black & White

vi.	RandomErasing: Randomly erases a portion of the image

Applying these transformations, I then Normalise the data using values from ImageNet statistics which gave great consistency throughout the various models

d.	Splitting the Dataset

Lastly, the dataset was split into an 85-15 segments where 85% of the data was used for training while the rest 15% was used for the validation testing.
The split was made on random but using a manual seed to keep the model consistent throughout every training iteration.



2.	Model Architecture:

   
a.	Model Used : CLiP based ViT-L/14@336px

b.	Why?:

After trying out several models over the course of the challenge, it was clear to me that recognising the 10 unknown classes somehow involved text-based descriptions.
I had started the project as an opportunity to learn more and more about AIML, and initially, I had nearly zero knowledge. Hence, I ensured that I will first train a model just to recognise the 40 known classes without worrying about the remaining 10. I started off with a basic Sci-Kit based model followed by a pretrained VGG-16, EfficientNetB and ConvNeXT model all of which improved the accuracy of the data recognition with each transition on tweaks. 
Having searched about a text-based model, OpenAI’s CLiP was the top choice. Unfortunately, I could not get it to work in pair with the best performing ConvNeXT model which gave me a 58% accuracy on 50 classes with just the 40 class dataset and a 93% accuracy after training it with self-downloaded images of the remaining 10 as well.


However, having optimised the data loading and augmentation techniques, I started again, keeping the entire model CLiP based and using a vision transformer as a base model.


3.	Training:
   
a.	Loss Function: CrossEntropyLoss() from torch.nn library

b.	Optimizer: AdamW

c.	Epochs and Batch Size: Epochs – 10, Batch Size - 32

d.	Hardware: Kaggle Platform’s GPU T4 x2

e.	Extra Parameters: Customised Learning Rate Scheduler (CyclicLR), Specified Weight Decays, and 3 custom layered model training with relu activation.

The training process was kept fairly simple. I tested out different options like using SGD as an optimiser, increasing batch size and epochs and tweaking other training hyperparameters like learning rate and weight decay. Any other alternatives I used, however only resulted in either low accuracy or a NAN Loss which were not optimal.

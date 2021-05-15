# Udacity Pre-trained Dog Image Classifier

This is my implementation of udacity pre-trained dog image classifier project for CNN (Convolutional Neural Network).

# Project Objectives

1.  Correctly identify which pet images are of dogs (even if breed is misclassified) and which pet images aren't of dogs.

2.  Correctly classify the breed of dog, for the images that are of dogs.

3.  Determine which CNN model architecture (ResNet,AlexNet, or VGG), "best" achieve the objectives 1 and 2.

4.  Consider the time resources required to best achieve objectives 1 and 2, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms take to run.

# project meets these specifications

- A time function is called before the main project starts and after the main logic is completed
- Add command line argument for '--dir': using default = 'pet_images/'
- Add command line argument for '--arch': using default = 'vgg'
- Add command line argument for '--dogfile': using default = 'dognames.txt'
- Make sure file are starting with '.' periods and ignored checks for '.' using a conditional statement
- dictionary key and label are in the correct format and retrieves 40 key-value pairs. e.g:- {'Poodle_07956.jpg': ['poodle'], 'fox_squirrel_01.jpg': ['fox squirrel'] ... }
- in_args.dir' is passed as an argument inside the check_images while calling te get_pet_labels function
- Appends images_dir to each value before making the function call
- Classifier (images_dir + users_key, model)
- Convert the output to lower case and strip any whitespaces
- Appends 1 to correct label and 0 to falsely classified values, classifying labels as dogs
- Check the displayed output and see if all matches are appropriately displayed
- Check the displayed output and see if all non matches are appropriately displayed results
- all three models score as expected

# Pre-trained  Dog Classifier
1.  **Did the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed? If not, report the differences in the classifications.**

All three models reported the same classification (golden retriever, staffordshire bullterrier, staffordshire bull terrier). There was no misclassified
images.

2.  **Did each of the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed of dog as that model architecture classified Dog_02.jpg? If not, report the differences in the classifications.**

ResNet and VGG consistently misidentified the golden retriever, staffordshire bullterrier, staffordshire bull terrier. Where as AlexNet did not misidentified any of the dog breeds.

3. **Did the three model architectures correctly classify Animal_Name_01.jpg and Object_Name_01.jpg to not be dogs? If not, report the misclassifications.**

All are correctly classified

4.  **Based upon your answers for questions 1. - 3. above, select the model architecture that you feel did the best at classifying the four uploaded images. Describe why you selected that model architecture as the best on uploaded image classification.**

- ResNet and VGG consistently misidentified the golden retriever, staffordshire bullterrier, staffordshire bull terrier. Where as AlexNet did not misidentified any of the dog breeds. Both ResNet and AlexNet had problems classifying non animal images. ResNet and AlexNet misidentified the cappuccino Image as mixing bowel. only VGG was able to correctly classify the cappuccino Image. However ResNet and VGG performed much better than AlexNet

- Based on the on the overall classification results VGG is the optimal model for the uploaded images

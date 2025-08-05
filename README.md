# Waste Classification Using CNNs

## Description

This repository implements a training pipeline for deep learning models, focusing on feature extraction, fine-tuning, and model evaluation. The pipeline uses the six pre-trained models with wide range of architectures and specialties. The project utilizes the **RealWaste** dataset from the paper:

- **Sam Single, Saeid Iranmanesh, and Raad Raad. Realwaste: A novel real-life data set for landfill waste classification using deep learning. Information, 14(12), 2023.**

## Features

- Feature extraction and fine-tuning pipeline for transfer learning.
- Evaluation of model performance on specific datasets.
- Currently supports DenseNet121 (w/ and w/o augmentation), Inception V3, VGG-16, Wide ResNet101-2, ConvNeXt Base, and MobileNet V2

## Results
- Five out of six models outperform the best model in the original paper.
- Details can be found in metrics.csv, plot, and report directory.

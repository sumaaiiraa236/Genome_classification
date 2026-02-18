# DNA Promoter Sequence Classification

## Project Overview

    DNA may be written in just four letters A, C, G, and T but decoding its regulatory logic is anything but simple.

    This project explores the use of machine learning to classify promoter sequences short regulatory regions that determine when genes are switched on.This is a foundational step toward sequence-based modeling inspired by modern regulatory genomics research. By translating nucleotide sequences into numerical representations, I implement a simple yet foundational classification pipeline to better understand how computational models can capture biologically meaningful patterns.

    As an aspiring researcher in computational genomics and healthcare ML, this project represents my first step toward sequence-level modeling in regulatory genomics.

Lets begin with understanding a little bit of basics.

##Promoters

    A promoter is a region of DNA located near the start of a gene that controls when and how strongly a gene is expressed. Identifying promoter regions is an important problem in bioinformatics and has implications in disease research and genetic regulation.


##Dataset
    1.The dataset used is the UCI Promoter Gene Sequences dataset.
    2.It contains DNA sequences labeled as promoter (+) or non-promoter (-).
    3.Each sequence is 57 nucleotides long.

##Exploratory Data Analysis
    The dataset was analyzed for class distribution to evaluate potential imbalance 
![Class Distribution](image.png)
    The dataset appears approximately balanced, which supports reliable model training.

##Methodology
    1.Label Encoding (+ → 1, - → 0)
    2.DNA Sequence Encoding (A,C,G,T → numerical representation)
    3.Train-Test Split (80/20)
    Logistic Regression classifier

##Results
    The logistic regression model achieved an accuracy of 77.2% on the test set.
    This suggests that even simple linear models can capture positional sequence patterns associated with promoter regions.

##Research
    Regulatory genomics increasingly relies on sequence-based modeling to extract functional signals directly from raw DNA. Early deep learning approaches demonstrated that neural networks can automatically learn biologically meaningful motifs from nucleotide sequences.

    Babak Alipanahi et al. (2015) introduced DeepBind, applying convolutional neural networks to predict DNA and RNA binding specificities. Similarly, Jian Zhou and Olga Troyanskaya (2015) proposed DeepSEA, a deep learning framework for predicting functional effects of non-coding variants directly from raw genomic sequence data.

    Inspired by these works, this project explores a simplified baseline approach to promoter classification using the UCI Machine Learning Repository Promoter Gene Sequences dataset. Instead of deep architectures, nucleotide sequences are encoded numerically (A=0, C=1, G=2, T=3) and modeled using Logistic Regression.

    This baseline investigates how far a linear classifier can go when applied directly to encoded DNA sequences, providing an interpretable and computationally lightweight starting point for more advanced sequence models.

## References

[1] Alipanahi, B., et al. (2015). Predicting the sequence specificities of DNA- and RNA-binding proteins using deep learning. Nature Biotechnology.

[2] Zhou, J., & Troyanskaya, O. (2015). Predicting effects of noncoding variants with deep learning–based sequence model. Nature Methods.

[3] UCI Machine Learning Repository. Promoter Gene Sequences Dataset.
##Future Improvements
    1.Use one-hot encoding instead of numeric encoding to better represent DNA bases.

    2.Try k-mer features to capture short sequence patterns.

    3.Experiment with non-linear models like SVM or Random Forest.

    4.Explore a simple 1D CNN to automatically learn promoter motifs.

    5.Add more evaluation metrics such as F1-score or ROC-AUC.

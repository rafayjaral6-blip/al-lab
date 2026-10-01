# Laboratory 3 Report

## Part A: Text Features

1. **What does each column represent?** Each column represents one term in the corpus vocabulary. A cell contains that term's count in the corresponding document; zero means the term is absent.

2. **What is the machine-understandable format?** It is a document-term matrix: one numeric row per document and one column per vocabulary term. In this lab, the values are integer word counts.

3. **How is Bag-of-Words an oversimplification?** It discards word order, so sentences with different meanings can have identical counts. It also does not represent meaning or relationships between words, and it cannot reliably capture context or negation. For example, `good` and `great` are unrelated features, and `not good` is represented as separate counts without encoding the negation relationship.

## Part B: Image Features

4. **How does grayscale conversion act as feature engineering?** It combines the red, green, and blue channels into one luminance value per pixel. This reduces the number of pixel features while retaining brightness and spatial layout, but it removes color information.

5. **What is the flattened-vector length for an $H \times W$ grayscale image?** The vector has $H \times W$ values, one for each grayscale pixel.

6. **Why flatten before using Logistic Regression or an SVM?** These models expect each sample to be represented as a fixed-length one-dimensional feature vector. Flattening converts the two-dimensional pixel grid into that format, though it removes the explicit row-and-column structure.

7. **Why resize images to a consistent size?** A model's feature vector must have the same number of values for every sample. Resizing each image to the same width and height guarantees equal-length vectors, making them stackable into a feature matrix.

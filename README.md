# codechef-NLP and OkCupid Dating Profiles Analysis

** I've added a notebook on OkCupid Dating Profiles Analysis.  In it, I apply topic modeling to OkCupid bios, using data that was obtained using an API.  The algorithm clusters men and women into groups based on what they type in their description.

<img src="images/okcupid_logo.jpg" style="width: 500px;"/>


Natural language processing and machine learning experiments on problem statements and solutions provided by codechef competitive programming site

How might we train a model to predict difficulty level using the question statement?

We start off with EDA and cleaning.  We have tables of questions, solutions, and submitted code snippets.  Using the code submissions, we can count up the number of correct and incorrect answers, and compute the success ratio grouped by user and by question.

The first idea to explore is whether the golden labels provided by the site ("easy", "medium", "hard", etc.) reflect the actual success ratios based off users' attempt/ rates of success.  For interesting visualization, let's apply K-Means clustering to the questions based off their 'question_success_ratio', with some influence by their assigned labels (I added random noise to the assigned difficulty labels).  Practically, this clustering could indicate whether the questions should have their difficulty levels re-labeled, reflecting actual success ratio statistics.

Points were clustered into 3 groups:

    The largest cluster consists of questions that had high success ratio, irrespective of the golden labels from the dataset.
     - these might be considered the new "easy" questions
    second largest cluster are questions labeled easy, yet have low success ratio
     - these might be considered the new 'medium'
    smallest cluster are questions labeled hard with low success ratio
     - these are the true 'hard' ones

For more difficulty tiers, we could increase the number of centroids.  We demonstrate how to compute the silhouette score to choose a different value for k, and then cluster the questions into 6 clusters.  This level scheme could help users with a more gradual progression in difficulty.


Next, we load in the datasets containing code snippets of submitted solutions, and try to classify code snippets as either Python or C++.  Let's train a classification model on the solutions dataset, where given a sample solution, we want to assign the label "C++11" or "Python" based on the text content of the solution. This is a standard binary classification task.
We'll do a bag of words processing with tokenization, where we split each document into words; vocabulary building, where we collect a vocabulary of all words that appear in any of the documents and number them; and encoding, where we count how often each of the words in the vocabulary appear in this document.
The shape of X_train, which represents the bag of words representation of the training data is 31772x38672, indicating that the vocabulary contains 38,672 entries. The data is stored in a SciPy sparse matrix.
We train a logistic regression model for document classification, and use cross-validation to obtain an accuracy.  On the training data:
    default parameters:   Mean cross-validation accuracy: 0.9959705463307194

    Best cross-validation score: 0.9964112573191463
    Best parameters:  {'C': 0.1}
    We used a simple grid search to tune via cross-validation our regularization parameter C.

On Test Data:
Mean cross-validation accuracy: 0.9950892610105836
Hence, it was easy to predict whether a code snippet is Python or C++ using CountVectorizer and LogisticRegression.  The result is as expected, since each language has its respective keywords that would obviously determine the language.

Can we cluster question statements into discrete topics?  
Next, we experiment with some topic modeling.  Unfortunately, our dataset does not include the question category labels, e.g. "trees", "graphs", "strings", etc.  Fortunately, however, we can try to apply topic modeling on the question statements and obtain question categories in with an unsupervised machine learning algorithm.  We start with topic Modeling with Non-Negative Matrix factorization (NMF).  We use the CountVectorizer from scikit-learn to turn the content of the question statements into the document-term matrix A.  Apply NMF with SVD-based initialization to the document-term matrix AA generate topics, then get the W and H factors from the resulting model.  We get the top ranked terms for each topic, by sorting the values in the rows of the HH factor.  We do the same with TF-IDF, the results of which I thought were the best.  If we think of topics as group of words that commonly appear together in the same statement, the NMF model generates results closer to what we'd expect.  Here's a subsection of the 15 topics:

...
 - Topic 2: string, strings, substring, length, characters, character, substrings, letters, palindrome, latin
 - Topic 3: cell, cells, grid, row, column, color, rows, columns, board, right
 - Topic 4: node, nodes, tree, path, trees, edge, root, distance, associated, cost
...

These clusters help us understand how questions fall into categories. For instance, questions about trees (Topic 4) tend to have an intuitive set of associated words.  We count the number of question statements primarily belonging to each of the above topics and plot a histogram.  We also use LatentDirichletAllocation, which resulted in more specific keywords.

As an experiment! Let's create topic models on code snippets.  Could we guess what what question the code is answering? Since code has more structure than English and we have a bag of words assumptions, results would probably be nonsensical, but let's experiment. We'll use NMF with tfidf, since I think it's the most impressive.

...
 - Topic 2: rectangles, got, present, size, light, recognition, www, y1, st, _gaq
 - Topic 3: submit, special, removed, girl, light, got, replace, present, www, similarly
...

I thought the results were nonsensical but it was an interesting experiment.


Next, we try to predict, given the statement, whether the question is "easy" or "medium" using Naïve Bayes as the classifier.  Our classifier will use word counts as features and make a classification decision on the level of difficulty.

Results:
There are 20,267 words in the vocabulary.
'tree' appears 18,822 times.
The accuracy on the test data is 45.76%

The accuracy is below baseline, which suggests, as we suspected, that CountVectorizer on the words of the question statement is not correlated to difficulty level.  Nevertheless, we calculate accuracy, recall, precision, F1 score, and show a confusion matrix.  We got 63% accuracy on the test data.
Next we perform 10-fold cross-validation on the training and testing data. The average accuracy is about 40%, which is worse than baseline.


Next we use TextBlob's pretrained sentiment tool on the entire corpus of question statements. We got Sentiment(polarity=0.0662212856306699, subjectivity=0.4231108107510163), so the question statements overall have neutral sentiment.  As a reference point, the string "have a great day" has a sentiment polarity=0.8.


Finally, we train Various Classifiers to predict success (whether a submitted solution is correct or incorrect)
As an exercise, we could try to predict Success based on TimeTaken, MemTaken, and question_success_ratio.  We do some data cleaning and manipulation to prepare the data for the task.
First, use Kernelized support vector machines, which are an extension that allows for more complex models that are not defined simply by hyperplanes in the input space.

    Keep in mind that we're using each question's success ratio to predict success. The only other features we include are TimeTaken and MemorySpace.

    Hence, we're using past/aggregate performance and adding in a few extra variables to predict success.


Since the number of no success and success are about even, we don't need to correct class imbalance issues. It also means that an accuracy score of 75% should be compared to a 50% baseline.

Here were the results:

SVM:
Train score: 0.75
Test score: 0.75

Random Forest:
Accuracy on training set: 0.895
Accuracy on test set: 0.853

Gradient Boosting:
Accuracy on training set: 0.802
Accuracy on test set: 0.807

SVM with initial grid search:
Best score on validation set: 0.82
Best parameters:  {'C': 100, 'gamma': 100}
Test set score with best parameters: 0.82

Using the parameters we tried, the Random Forest Classifier outperformed the other models.

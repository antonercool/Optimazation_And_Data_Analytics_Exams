from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def train_LDA_model(training_set, training_labels):
    lda_model = LinearDiscriminantAnalysis()
    lda_model.fit(training_set, training_labels)
    return lda_model

def classify_LDA(testing_set, trained_model):
    return trained_model.predict(testing_set)

if __name__ == '__main__':
    training_set =  [[1,2], [1,0], [0,-1] ,[-2,-1]]
    labels = [1,1,2,2]

    trained_model = train_LDA_model(training_set, labels)
    print(trained_model.coef_)




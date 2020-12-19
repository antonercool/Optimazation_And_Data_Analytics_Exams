from sklearn import neighbors

def train_NCC_model(training_set, training_labels, number_of_neighbors):
    nnc_model = neighbors.KNeighborsClassifier(number_of_neighbors, weights="uniform")
    nnc_model.fit(training_set, training_labels)
    return nnc_model

def classify_NNC(testing_set, trained_model):
    return trained_model.predict(testing_set)

if __name__ == '__main__':
    training_set =  [[0,1], [1,1], [3,1] ,[3,2], [4,2]]
    labels = [1,1,2,2,2]
    testing_set =  [[1,2], [3,0], [2,1]]
    number_of_neighbors = 1

    trained_model = train_NCC_model(training_set, labels, number_of_neighbors)
    predicted_classes = classify_NNC(testing_set, trained_model)
    print(predicted_classes)
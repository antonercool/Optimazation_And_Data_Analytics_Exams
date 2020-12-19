from sklearn import neighbors

def train_NCC_model(training_set, training_labels, number_of_neighbors):
    nnc_model = neighbors.KNeighborsClassifier(number_of_neighbors, weights="uniform")
    nnc_model.fit(training_set, training_labels)
    return nnc_model

def classify_NNC(testing_set, trained_model):
    return trained_model.predict(testing_set)

if __name__ == '__main__':
    training_set =  [[1,2], [1,0], [0,-1] ,[-2,-1]]
    labels = [1,1,2,2]
    testing_set =  [[2,0], [0,0], [-1,1] ,[-2,0]]
    number_of_neighbors = 2

    trained_model = train_NCC_model(training_set, labels, number_of_neighbors)
    predicted_classes = classify_NNC(testing_set, trained_model)
    print(predicted_classes)
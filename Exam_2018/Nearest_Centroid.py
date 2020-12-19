from sklearn.neighbors import NearestCentroid

def train_NCC_model(training_set, training_labels):
    ncc_model = NearestCentroid()
    ncc_model.fit(training_set, training_labels)
    return ncc_model

def classify_NCC(testing_set, trained_model):
    return trained_model.predict(testing_set)

if __name__ == '__main__':
    training_set =  [[1,2], [1,0], [0,-1] ,[-2,-1]]
    labels = [1,1,2,2]
    testing_set =  [[2,0], [0,0], [-1,1] ,[-2,0]]

    trained_model = train_NCC_model(training_set, labels)
    predicted_classes = classify_NCC(testing_set, trained_model)
    print(predicted_classes)
    


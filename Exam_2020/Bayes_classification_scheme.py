from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    training_set =  [[1,1], [0,1], [1,0] ,[3,1], [3,2],[4,1], [4,2]]
    labels = [1,1,1,2,2,2,2]
    testing_set =  [[0,0], [3,1], [2,2]]

    gnb = GaussianNB()
    y_pred = gnb.fit(training_set, labels).predict(testing_set)

    print(y_pred)

    
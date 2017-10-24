from data_reader import get_binary_features

if __name__ == "__main__":

	# If you do not have an existing feature vector
	data_set = "../income-data/income.train.txt.5k"
    X, Y, features = get_binary_features(data_set)

    # If you have an existing feature vector you want to compute against
    data_set = "../income-data/income.dev.txt"
    X_dev, Y_dev, features = get_binary_features(data_set, features)
import pickle


def save_model(model, path):
    s = pickle.dumps(model)
    file = open(path, "wb")
    file.write(s)
    file.close()


def get_model(path):
    file = open(path, "rb")
    s = file.read()
    file.close()
    return pickle.loads(s)

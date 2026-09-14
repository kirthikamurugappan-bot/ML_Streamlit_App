class IrisModel:
    def __init__(self, data):
        self.data = data

    def predict_one(self, values):
        distances = []

        features = [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width"
        ]

        for _, row in self.data.iterrows():
            distance = 0

            for feature, value in zip(features, values):
                distance += (row[feature] - value) ** 2

            distances.append((distance ** 0.5, row["species"]))

        distances.sort(key=lambda x: x[0])

        nearest = distances[:5]

        votes = {}

        for _, label in nearest:
            votes[label] = votes.get(label, 0) + 1

        return max(votes, key=votes.get)

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Load the breast cancer dataset
breast_cancer_data = load_breast_cancer()

# Print the first data point
print("First Data Point:")
print(breast_cancer_data.data[0])
print("\nFeature Names:")
print(breast_cancer_data.feature_names)


training_data, validation_data, training_labels, validation_labels = train_test_split(
    breast_cancer_data.data, 
    breast_cancer_data.target, 
    test_size=0.2, 
    random_state=100
)

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(training_data, training_labels)

# Evaluate the classifier's accuracy on the validation set
accuracies = []
for k in range(1, 101):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(training_data, training_labels)
    accuracy = classifier.score(validation_data, validation_labels)
    accuracies.append(accuracy)
    print(f"k = {k}: Validation Accuracy = {accuracy:.4f}")

best_k = accura
accuracy = classifier.score(validation_data, validation_labels)
print(f"The accuracy of the classifier on the validation set is: {accuracy:.4f}")

# Plot results
k_list = list(range(1, 101))
accuracies = []
for k in k_list:
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(training_data, training_labels)
    accuracy = classifier.score(validation_data, validation_labels)
    accuracies.append(accuracy)

best_k = accuracies.index(max(accuracies)) + 1

plt.figure(figsize=(10, 6))
plt.plot(k_list, accuracies, marker='o', linestyle='-')
plt.title('Breast Cancer Classifier Accuracy')
plt.xlabel('k')
plt.ylabel('Validation Accuracy')
plt.grid(True)
plt.show()

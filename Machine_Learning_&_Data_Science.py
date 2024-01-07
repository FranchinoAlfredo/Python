# Importa le librerie necessarie
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carica il dataset Iris incluso in scikit-learn
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividi il dataset in set di addestramento e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizza le caratteristiche per avere una migliore convergenza nell'addestramento
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Inizializza il classificatore SVM
svm_classifier = SVC(kernel='linear', C=1.0, random_state=42)

# Addestra il modello SVM
svm_classifier.fit(X_train, y_train)

# Esegui le previsioni sul set di test
predictions = svm_classifier.predict(X_test)

# Calcola l'accuratezza del modello
accuracy = accuracy_score(y_test, predictions)
print(f'Accuratezza del modello SVM: {accuracy * 100:.2f}%')

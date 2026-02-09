from datetime import datetime
import json
import joblib

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

if __name__ == "__main__":
    run_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Load Wine dataset
    wine = load_wine()
    X, y = wine.data, wine.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train a Random Forest classifier (changed params)
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=6,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Evaluate
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # Save the model
    joblib.dump(model, "wine_model.pkl")

    # Save metadata (date + changes)
    metadata = {
        "run_date": run_date,
        "dataset": "wine",
        "model": "RandomForestClassifier",
        "n_estimators": 200,
        "max_depth": 6,
        "test_accuracy": acc
    }

    with open("run_metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print("Training successful ✅")
    print(f"Run date: {run_date}")
    print(f"Test accuracy: {acc:.4f}")
    print(classification_report(y_test, preds))

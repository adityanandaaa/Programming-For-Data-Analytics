import os
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier, StackingClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier


def find_titanic_csv() -> Path:
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent

    candidates = [
        script_dir / "titanic_train.csv",
        repo_root / "Week 8 Seminar" / "data" / "titanic_train.csv",
        repo_root / "Week 7 Seminar" / "data source" / "titanic_train.csv",
        repo_root / "Week 8 Seminar" / "titanic_train.csv",
    ]

    for path in candidates:
        if path.exists():
            return path

    raise FileNotFoundError("Could not find titanic_train.csv in expected locations.")


def data_clean(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe = dataframe.fillna({"Age": dataframe["Age"].mean()}).dropna(axis=1)
    dataframe = dataframe.drop(columns=["Ticket"], errors="ignore")

    top = dataframe["Age"].mean() + 2 * dataframe["Age"].std()
    bot = dataframe["Age"].mean() - 2 * dataframe["Age"].std()
    dataframe = dataframe.drop(dataframe[dataframe["Age"] > top].index)
    dataframe = dataframe.drop(dataframe[dataframe["Age"] < bot].index)

    dataframe["Title"] = dataframe["Name"].str.extract(r"^([\w\W]+),")
    sex_dummies = pd.get_dummies(dataframe["Sex"])
    if "Female" in sex_dummies.columns:
        dataframe["Female"] = sex_dummies["Female"]
    if "Male" in sex_dummies.columns:
        dataframe["Male"] = sex_dummies["Male"]

    dataframe["FareNor"] = (dataframe["Fare"] - dataframe["Fare"].mean()) / dataframe["Fare"].std()
    dataframe["AgeGroup"] = pd.cut(dataframe["Age"], [0, 19, 61, 100], labels=["Minor", "Adult", "Elder"])

    dataframe["Family"] = dataframe["Parch"] + dataframe["SibSp"]
    dataframe.loc[dataframe["Family"] > 0, "Family"] = 1
    dataframe.loc[dataframe["Family"] == 0, "Family"] = 0

    dataframe = dataframe.drop(columns=["SibSp", "Parch", "Sex"], errors="ignore")
    return dataframe


def section_basic_and_ensemble(df_titan: pd.DataFrame) -> None:
    print("\n=== Build the basic tree ===")

    imp = SimpleImputer(strategy="mean")
    df = df_titan.copy()
    df["Age"] = imp.fit_transform(df[["Age"]])

    enc = OneHotEncoder(sparse_output=False)
    nd_sex = enc.fit_transform(df[["Sex"]])
    df_sex = pd.DataFrame(nd_sex, columns=enc.get_feature_names_out(), index=df.index)
    df = pd.concat([df, df_sex], axis=1)

    titan_y = df["Survived"]
    titan_x = df.drop(
        columns=["Survived", "Name", "Sex", "PassengerId", "SibSp", "Parch", "Cabin", "Ticket", "Embarked"],
        errors="ignore",
    )

    X_train, X_test, Y_train, Y_test = train_test_split(titan_x, titan_y, test_size=0.3, random_state=22)

    clf = DecisionTreeClassifier()
    clf.fit(X_train, Y_train)
    y_pred = clf.predict(X_test)
    print("Decision Tree Accuracy:", metrics.accuracy_score(Y_test, y_pred))

    print("\n=== Bagging: Random Forest ===")
    rfc = RandomForestClassifier(n_estimators=150, max_depth=3)
    rfc.fit(X_train, Y_train)
    y_pred = rfc.predict(X_test)
    print("Random Forest Accuracy:", metrics.accuracy_score(Y_test, y_pred))

    print("\n=== Boosting: AdaBoost ===")
    ada = AdaBoostClassifier(n_estimators=75)
    ada.fit(X_train, Y_train)
    y_pred = ada.predict(X_test)
    print("AdaBoost Accuracy:", metrics.accuracy_score(Y_test, y_pred))

    print("\n=== Stacking ===")
    base_models = [("clf_1", RandomForestClassifier()), ("clf_2", AdaBoostClassifier())]
    scf = StackingClassifier(estimators=base_models)
    scf.fit(X_train, Y_train)
    y_pred = scf.predict(X_test)
    print("Stacking Accuracy:", metrics.accuracy_score(Y_test, y_pred))


def section_common_issues_and_transforms(df_titan: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, pd.Series, pd.Series]:
    print("\n=== Common Issues / Proper preprocessing flow ===")

    titan_y = df_titan["Survived"]
    titan_x = df_titan.drop(columns=["Survived", "Name", "PassengerId", "SibSp", "Parch", "Cabin", "Ticket"], errors="ignore")

    X_train, X_test, Y_train, Y_test = train_test_split(titan_x, titan_y, test_size=0.3, random_state=23)

    imp1 = SimpleImputer(strategy="mean")
    imp2 = SimpleImputer(strategy="most_frequent")

    X_train = X_train.copy()
    X_test = X_test.copy()

    imp1.fit(X_train[["Age"]])
    X_train["Age"] = imp1.transform(X_train[["Age"]])
    imp2.fit(X_train[["Embarked"]])
    X_train["Embarked"] = imp2.transform(X_train[["Embarked"]]).ravel()

    X_test["Age"] = imp1.transform(X_test[["Age"]])
    X_test["Embarked"] = imp2.transform(X_test[["Embarked"]]).ravel()

    enc = OneHotEncoder(sparse_output=False)
    enc.fit(X_train[["Embarked", "Sex"]])

    tf = ColumnTransformer(
        [("impa", SimpleImputer(strategy="mean"), ["Age"]), ("impb", SimpleImputer(strategy="most_frequent"), ["Embarked"])],
        remainder="passthrough",
    )
    X_train_clean = tf.fit_transform(X_train)

    tf1 = ColumnTransformer(
        [("enca", OneHotEncoder(sparse_output=False), [1, 3])],
        remainder="passthrough",
    )
    X_train_clean = tf1.fit_transform(X_train_clean)

    tf2 = ColumnTransformer(
        [("scalera", MinMaxScaler(), [5, 7])],
        remainder="passthrough",
    )
    X_train_clean = tf2.fit_transform(X_train_clean)

    pca_model = PCA(n_components="mle")
    X_train_clean = pca_model.fit_transform(X_train_clean)

    X_test_clean = tf.transform(X_test)
    X_test_clean = tf1.transform(X_test_clean)
    X_test_clean = tf2.transform(X_test_clean)
    X_test_clean = pca_model.transform(X_test_clean)

    clf_dt = DecisionTreeClassifier()
    clf_dt.fit(X_train_clean, Y_train)
    y_pred = clf_dt.predict(X_test_clean)
    print("Decision Tree (manual transform flow) Accuracy:", metrics.accuracy_score(Y_test, y_pred))

    return X_train_clean, X_test_clean, Y_train, Y_test


def section_pipeline(df_titan: pd.DataFrame) -> None:
    print("\n=== Pipeline (recommended approach) ===")

    titan_y = df_titan["Survived"]
    titan_x = df_titan.drop(columns=["Survived", "Name", "PassengerId", "SibSp", "Parch", "Cabin", "Ticket"], errors="ignore")

    X_train, X_test, Y_train, Y_test = train_test_split(titan_x, titan_y, test_size=0.3, random_state=1)

    num_features = titan_x.select_dtypes(include=[np.number]).columns
    cat_features = titan_x.select_dtypes(exclude=[np.number]).columns

    num_pipeline = Pipeline(steps=[("imputer", SimpleImputer(strategy="mean")), ("scaler", MinMaxScaler())])
    cat_pipeline = Pipeline(steps=[("imputer", SimpleImputer(strategy="most_frequent")), ("enc", OneHotEncoder(sparse_output=False))])

    cf = ColumnTransformer(
        [("num", num_pipeline, num_features), ("cat", cat_pipeline, cat_features)],
        remainder="passthrough",
    )

    pipe = Pipeline(
        [
            ("tf", cf),
            ("PCA", PCA(n_components="mle")),
            ("DecisionTree", DecisionTreeClassifier()),
        ]
    )

    pipe.fit(X_train, Y_train)
    score = pipe.score(X_test, Y_test)
    explained = pipe.steps[1][1].explained_variance_ratio_.sum()

    print("Pipeline Accuracy:", score)
    print("PCA explained variance sum:", explained)


def main() -> None:
    data_path = find_titanic_csv()
    print(f"Using dataset: {data_path}")

    df_titan = pd.read_csv(data_path)

    cleaned_preview = data_clean(df_titan.copy())
    print("data_clean() preview shape:", cleaned_preview.shape)

    section_basic_and_ensemble(df_titan)
    section_common_issues_and_transforms(df_titan)
    section_pipeline(df_titan)


if __name__ == "__main__":
    main()

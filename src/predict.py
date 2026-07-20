def predict_species(model, scaler):
    """
    Predict flower species using user input.
    """

    print("\n===== Predict New Flower =====")

    sepal_length = float(input("Enter Sepal Length (cm): "))
    sepal_width = float(input("Enter Sepal Width (cm): "))
    petal_length = float(input("Enter Petal Length (cm): "))
    petal_width = float(input("Enter Petal Width (cm): "))

    new_flower = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    # Scale the input
    new_flower = scaler.transform(new_flower)

    prediction = model.predict(new_flower)

    print("\nPredicted Species:", prediction[0])

    return prediction[0]
import pandas as pd
def skew_calc(df):
    """
    Diagnoses skewness for every numeric column in a DataFrame and recommends a transformation based on the column's skewness and
    minimum value. Binary, encoded, and ID columns are excluded, since skewness isn't a meaningful for them.
    It returns a DataFrame with the following columns:
    Feature, Skewness, Degree, Direction, Recommended Transformation
    """

    output = []

    for col in df.select_dtypes(include='number').columns:

        data = df[col]
        value = data.skew()


        if -0.5 < value < 0.5:
            degree = "Approximately Symmetric"
        elif -1 < value <= -0.5 or 0.5 <= value < 1:
            degree = "Moderately Skewed"
        else:
            degree = "Highly Skewed"

        # Direction
        if value > 0:
            side = "Positive"
        elif value < 0:
            side = "Negative"
        else:
            side = "Symmetric"


        if -0.5 < value < 0.5:
            method = "None"

        elif data.min() == 0:
            method = "Log Plus One or Yeo-Johnson"

        elif data.min() > 0:
            method = "Box-Cox or Yeo-Johnson"

        else:
            method = "Yeo-Johnson"

        output.append({
            "Feature": col,
            "Skewness": value,
            "Degree": degree,
            "Direction": side,
            "Recommended Transformation": method})

    return pd.DataFrame(output)

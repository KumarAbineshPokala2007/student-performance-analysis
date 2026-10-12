def analyse_students(df):
    subjects =["Maths","Science","English"]

    # Calculate total marks for each subject

    df["Total"] = df[subjects].sum(axis=1)

    # Calculate average marks for each student

    df["Average"] = df[subjects].mean(axis=1).round(2)

    result = []

    for i in range(len(df)):
        maths = df["Maths"].iloc[i]
        science=df["Science"].iloc[i]
        eng=df["English"].iloc[i]

        if maths < 35 or science < 35 or eng < 35:
            result.append("Fail")
        else:
            result.append("Pass")

    df["Status"]=result

    high = []
    low = []
    
    for i in range(len(df)):
        h=df[subjects[0]].iloc[i]
        l=df[subjects[0]].iloc[i]
        for j in range(len(subjects)):
            if df[subjects[j]].iloc[i] > h:
                h=df[subjects[j]].iloc[i]
            if df[subjects[j]].iloc[i] < l:
                l=df[subjects[j]].iloc[i]

        high.append(h)
        low.append(l)
    
    df["Highest"] = high
    df["Lowest"] = low

    
    return df




import matplotlib.pyplot as plt


# Graph 1: Average marks of each student
def plot_student_averages(df):

    plt.figure(figsize=(10, 5))

    plt.bar(df["Name"], df["Average"])

    plt.title("Student Performance Analysis")
    plt.xlabel("Student Name")
    plt.ylabel("Average Marks")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Graph 2: Average marks in each subject
def plot_subject_averages(df):

    subjects = ["Maths", "Science", "English"]

    averages = df[subjects].mean()

    plt.bar(averages.index, averages.values)

    plt.title("Subject-wise Average Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")

    plt.tight_layout()
    plt.show()


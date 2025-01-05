import pandas as pd
from matplotlib import pyplot as plt

publications = pd.read_csv("final_matched_articles_with_gender.csv", encoding='utf-8-sig', low_memory=False)
academics = pd.read_excel("all_universities_academics_with_gender.xlsx")

publications['authors_list'] = publications['Author Full Names'].apply(lambda x: x.split('; '))

academics["Formal Name"] = academics["Academic Name"].apply(lambda x: str(x.split(" ")[1] + ", " + x.split(" ")[0]))

academics['Department'] = academics['Details'].apply(lambda x: x.split('/')[1])
academic_to_department = academics.set_index("Formal Name")['Department'].to_dict()

# Add a department column to publications dataset
def find_departments(authors_list):
    departments = set()
    for author in authors_list:
        if author in academic_to_department:
            departments.add(academic_to_department[author])
    return list(departments)

publications['Departments'] = publications['authors_list'].apply(find_departments)

department_papers = publications.explode('Departments')
papers_per_department = department_papers['Departments'].value_counts()

papers_per_department = papers_per_department.drop(labels = [idx for idx in papers_per_department.index if "FAKÜLTE" not in idx])
papers_per_department = pd.DataFrame(papers_per_department)

df = pd.DataFrame(papers_per_department.head(20))
df.plot(legend=False, kind="barh", color= "Black").invert_yaxis()
plt.title("Publication number per faculty")
plt.ylabel("Faculties")
plt.xlabel("Number of publications")
plt.savefig("publication_per_faculty.jpg", bbox_inches="tight")



female_academics = academics[academics["Gender"]=='Female']
academic_to_department = female_academics.set_index("Formal Name")['Department'].to_dict()
publications['Departments'] = publications['authors_list'].apply(find_departments)

department_papers = publications.explode('Departments')
female_papers_per_department = department_papers['Departments'].value_counts()

female_papers_per_department = female_papers_per_department.drop(labels = [idx for idx in female_papers_per_department.index if "FAKÜLTE" not in idx])
female_papers_per_department = pd.DataFrame(female_papers_per_department)

female_papers_per_department = female_papers_per_department.head(20)

female_df = pd.merge(papers_per_department, female_papers_per_department, on="Departments", suffixes=("_all","_female"))

female_df["Female Ratio"] = female_df["count_female"] / female_df["count_all"]

female_df = female_df.sort_values(by="Female Ratio", ascending=False)

female_df = female_df.drop(columns=["count_all", "count_female"])

female_df.plot(legend=False, kind="barh", color= "Black").invert_yaxis()
plt.title("Top 20 Faculties with Highest Ratio of Publications by Female Academics")
plt.ylabel("Faculties")
plt.xlabel("Ratio")
plt.savefig("female_ratio_per_faculty.jpg", bbox_inches="tight")

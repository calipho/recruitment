def get_skills():
    # Add at least 3 random skills for the user to select from
    skills = ["Python", "C++", "Java"]

    return skills


def show_skills(skills):
    obj1 = enumerate(skills, start=1)
    for skill in obj1:
        print(skill)


def get_user_skills(skills):

    skillslist = []

    for count in range(2):
        skill = input("choose your skills")
        skillslist.append(skill)
        print(skillslist)

    skills_dict = dict(zip(skills, skillslist))
    print(skills_dict)
    return skills_dict
    # Show the available skills and have user pick from them
    # Write your code here


def get_user_cv(skills):
    cv = {"name": input("write your name "), "age": input(
        "write your age "), "skills": get_user_skills(skills), "experience": input("write your experience ")}

    print(cv)
    return cv

    # Get the users CV from their inputs
    # Write your code here
    ...


def check_acceptance(cv, desired_skill):
    return cv["age"] >= 25 and cv["age"] <= 40 and cv["experience"] > 3 and desired_skill in cv["skills"].values()


def main():
    # Write your main logic here by combining the functions above into the
    print("Welcome to the special recruitment program, please answer the following questions:")
    if check_acceptance(get_user_cv(get_skills()), "Python") is True:
        print("You are accepted", {cv["name"]})
    else:
        print("Sorry, you are not accepted")

    ##userSkills = get_user_skills(get_skills())
    # get_user_cv(userSkills)
    ##check_acceptance(get_user_cv(userSkills), "Python")

    # desired outcome
    ...


if __name__ == "__main__":
    main()

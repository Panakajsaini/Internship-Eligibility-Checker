import streamlit as st
import pandas as pd
from datetime import datetime


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Internship Eligibility & Career Recommender",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CONSTANTS
# ============================================================

CURRENT_YEAR = datetime.now().year


# ============================================================
# CAREER DATABASE
# ============================================================

CAREERS = {

    "Data Analyst": {
        "emoji": "📊",
        "minimum_cgpa": 6.0,
        "minimum_relevant_skills": 2,

        "skills": [
            "Python",
            "SQL",
            "Excel",
            "Power BI",
            "Pandas",
            "Statistics"
        ],

        "branches": [
            "AI & Data Science",
            "Computer Science",
            "Information Technology",
            "Data Science",
            "Electronics"
        ],

        "interests": [
            "Data",
            "Problem Solving",
            "Technology"
        ],

        "description":
            "Analyze data, create reports and dashboards, "
            "and generate useful business insights.",

        "roadmap": [
            "Master Excel",
            "Learn SQL",
            "Learn Power BI",
            "Practice Python Pandas",
            "Learn basic Statistics",
            "Build 2-3 Data Analytics projects"
        ]
    },


    "QA / Software Testing": {
        "emoji": "🧪",
        "minimum_cgpa": 5.5,
        "minimum_relevant_skills": 2,

        "skills": [
            "Manual Testing",
            "SQL",
            "Selenium",
            "API Testing",
            "Python",
            "Git"
        ],

        "branches": [
            "AI & Data Science",
            "Computer Science",
            "Information Technology",
            "Electronics",
            "Software Engineering"
        ],

        "interests": [
            "Testing",
            "Problem Solving",
            "Technology"
        ],

        "description":
            "Test software applications, identify bugs, "
            "write test cases and verify software quality.",

        "roadmap": [
            "Learn SDLC",
            "Learn STLC",
            "Learn Manual Testing",
            "Practice Test Cases",
            "Learn Bug Reporting",
            "Learn API Testing",
            "Learn Selenium"
        ]
    },


    "Python Development": {
        "emoji": "🐍",
        "minimum_cgpa": 6.0,
        "minimum_relevant_skills": 2,

        "skills": [
            "Python",
            "SQL",
            "Git",
            "OOP",
            "Django",
            "REST API"
        ],

        "branches": [
            "Computer Science",
            "Information Technology",
            "AI & Data Science",
            "Software Engineering"
        ],

        "interests": [
            "Coding",
            "Technology",
            "Problem Solving"
        ],

        "description":
            "Build backend applications, APIs, automation tools "
            "and software using Python.",

        "roadmap": [
            "Strengthen Python",
            "Learn OOP",
            "Learn Git & GitHub",
            "Learn Django or Flask",
            "Learn REST APIs",
            "Build backend projects"
        ]
    },


    "Web Development": {
        "emoji": "🌐",
        "minimum_cgpa": 5.5,
        "minimum_relevant_skills": 2,

        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git",
            "Node.js"
        ],

        "branches": [
            "Computer Science",
            "Information Technology",
            "AI & Data Science",
            "Software Engineering"
        ],

        "interests": [
            "Coding",
            "Technology",
            "Design"
        ],

        "description":
            "Build modern websites and web applications "
            "using frontend and backend technologies.",

        "roadmap": [
            "Learn HTML",
            "Learn CSS",
            "Master JavaScript",
            "Learn React",
            "Learn Git & GitHub",
            "Learn Node.js",
            "Build responsive websites"
        ]
    },


    "SEO": {
        "emoji": "🔎",
        "minimum_cgpa": 5.0,
        "minimum_relevant_skills": 2,

        "skills": [
            "SEO",
            "Content Writing",
            "Google Analytics",
            "Keyword Research",
            "HTML",
            "Excel"
        ],

        "branches": [
            "Any Branch"
        ],

        "interests": [
            "SEO",
            "Content",
            "Data"
        ],

        "description":
            "Improve website visibility using keyword research, "
            "content optimization and technical SEO.",

        "roadmap": [
            "Learn SEO Fundamentals",
            "Learn Keyword Research",
            "Learn Google Analytics",
            "Learn Search Console",
            "Learn Technical SEO",
            "Create SEO Case Studies"
        ]
    },


    "Digital Marketing": {
        "emoji": "📱",
        "minimum_cgpa": 5.0,
        "minimum_relevant_skills": 2,

        "skills": [
            "SEO",
            "Content Writing",
            "Social Media",
            "Google Analytics",
            "Canva",
            "Excel",
            "Communication"
        ],

        "branches": [
            "Any Branch"
        ],

        "interests": [
            "SEO",
            "Content",
            "Business"
        ],

        "description":
            "Promote brands using SEO, social media, content "
            "marketing and digital analytics.",

        "roadmap": [
            "Learn Digital Marketing",
            "Learn SEO",
            "Learn Social Media Marketing",
            "Learn Google Analytics",
            "Practice Content Creation",
            "Build Campaign Projects"
        ]
    },


    "UI/UX Design": {
        "emoji": "🎨",
        "minimum_cgpa": 5.0,
        "minimum_relevant_skills": 2,

        "skills": [
            "Figma",
            "UI Design",
            "UX Research",
            "Canva",
            "Communication"
        ],

        "branches": [
            "Any Branch"
        ],

        "interests": [
            "Design",
            "Problem Solving",
            "Technology"
        ],

        "description":
            "Design user-friendly interfaces and improve "
            "the overall user experience of digital products.",

        "roadmap": [
            "Learn Figma",
            "Learn UI Design Principles",
            "Learn UX Research",
            "Create Wireframes",
            "Create Prototypes",
            "Build UI/UX Case Studies"
        ]
    }
}


# ============================================================
# FUNCTIONS
# ============================================================

def normalize_branch(branch):

    mapping = {
        "CSE": "Computer Science",
        "IT": "Information Technology",
        "AI": "AI & Data Science",
        "ECE": "Electronics",
        "BBA": "Management",
        "MBA": "Management",
        "B.Com": "Commerce"
    }

    return mapping.get(branch, branch)


def branch_matches(user_branch, career_branches):

    if "Any Branch" in career_branches:
        return True

    return normalize_branch(user_branch) in career_branches


def check_eligibility(
    career_name,
    cgpa,
    branch,
    graduation_year,
    skills
):

    career = CAREERS[career_name]

    satisfied = []
    failed = []

    # -------------------------------
    # CGPA
    # -------------------------------

    if cgpa >= career["minimum_cgpa"]:

        satisfied.append(
            f"CGPA requirement satisfied "
            f"({cgpa:.1f} / {career['minimum_cgpa']:.1f} required)"
        )

    else:

        failed.append(
            f"Minimum CGPA required: "
            f"{career['minimum_cgpa']:.1f}. "
            f"Your CGPA: {cgpa:.1f}"
        )


    # -------------------------------
    # BRANCH
    # -------------------------------

    if branch_matches(
        branch,
        career["branches"]
    ):

        satisfied.append(
            "Academic branch is suitable."
        )

    else:

        failed.append(
            "Your academic branch is not in the "
            "preferred branch list for this field."
        )


    # -------------------------------
    # GRADUATION YEAR
    # -------------------------------

    if graduation_year >= CURRENT_YEAR:

        satisfied.append(
            f"Graduation year {graduation_year} "
            f"is acceptable."
        )

    else:

        failed.append(
            f"Graduation year must be {CURRENT_YEAR} "
            f"or later for this project."
        )


    # -------------------------------
    # SKILLS
    # -------------------------------

    relevant_skills = [
        skill
        for skill in skills
        if skill in career["skills"]
    ]

    missing_skills = [
        skill
        for skill in career["skills"]
        if skill not in skills
    ]

    if len(relevant_skills) >= career["minimum_relevant_skills"]:

        satisfied.append(
            f"{len(relevant_skills)} relevant skills found "
            f"(minimum {career['minimum_relevant_skills']})"
        )

    else:

        failed.append(
            f"At least {career['minimum_relevant_skills']} "
            f"relevant skills are required. "
            f"You have {len(relevant_skills)}."
        )


    eligible = len(failed) == 0

    return (
        eligible,
        satisfied,
        failed,
        relevant_skills,
        missing_skills
    )


def calculate_match(
    career_name,
    skills,
    branch,
    graduation_year,
    experience,
    interests
):

    career = CAREERS[career_name]

    # --------------------------------
    # Skill score = 55
    # --------------------------------

    matched_skills = list(
        set(skills) & set(career["skills"])
    )

    if len(career["skills"]) > 0:

        skill_score = (
            len(matched_skills)
            /
            len(career["skills"])
        ) * 55

    else:

        skill_score = 0


    # --------------------------------
    # Branch score = 15
    # --------------------------------

    branch_score = 15 if branch_matches(
        branch,
        career["branches"]
    ) else 0


    # --------------------------------
    # Interest score = 15
    # --------------------------------

    matched_interests = list(
        set(interests) &
        set(career["interests"])
    )

    interest_score = min(
        len(matched_interests) / 3,
        1
    ) * 15


    # --------------------------------
    # Experience score = 10
    # --------------------------------

    experience_points = {
        "No experience": 0,
        "1-3 months": 4,
        "3-6 months": 7,
        "6+ months": 10
    }

    experience_score = experience_points[
        experience
    ]


    # --------------------------------
    # Graduation score = 5
    # --------------------------------

    graduation_score = (
        5
        if graduation_year >= CURRENT_YEAR
        else 0
    )


    total = round(
        skill_score
        + branch_score
        + interest_score
        + experience_score
        + graduation_score
    )

    return min(total, 100)


# ============================================================
# HEADER
# ============================================================

st.title(
    "🎯 Internship Eligibility & Career Recommender"
)

st.write(
    "Check your internship eligibility and discover "
    "career fields that match your profile."
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("👤 Student Profile")

st.sidebar.write(
    "Enter your details below."
)


target_field = st.sidebar.selectbox(
    "🎯 Target Internship Field",
    ["Let the system recommend"] + list(CAREERS.keys())
)


cgpa = st.sidebar.number_input(
    "📊 CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)


branch = st.sidebar.selectbox(
    "🎓 Branch",
    [
        "AI & Data Science",
        "Computer Science",
        "Information Technology",
        "Electronics",
        "Mechanical",
        "Civil",
        "Commerce",
        "Management",
        "Other"
    ]
)


graduation_year = st.sidebar.number_input(
    "🎓 Graduation Year",
    min_value=2020,
    max_value=2035,
    value=CURRENT_YEAR + 1,
    step=1
)


experience = st.sidebar.selectbox(
    "💼 Experience",
    [
        "No experience",
        "1-3 months",
        "3-6 months",
        "6+ months"
    ]
)


all_skills = sorted(
    list(
        set(
            skill
            for career in CAREERS.values()
            for skill in career["skills"]
        )
    )
)


skills = st.sidebar.multiselect(
    "🛠️ Your Skills",
    all_skills
)


interests = st.sidebar.multiselect(
    "❤️ Your Interests",
    [
        "Data",
        "Coding",
        "Testing",
        "Design",
        "SEO",
        "Content",
        "Business",
        "Problem Solving",
        "Technology"
    ]
)


analyze = st.sidebar.button(
    "🚀 Analyze My Profile",
    use_container_width=True
)


# ============================================================
# HOME SCREEN
# ============================================================

if not analyze:

    st.header("How This Application Works")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            """
            ### 1️⃣ Enter Profile

            Add your CGPA, branch, graduation year,
            skills and interests.
            """
        )

    with col2:

        st.info(
            """
            ### 2️⃣ Select Field

            Choose the internship field you
            want to check.
            """
        )

    with col3:

        st.info(
            """
            ### 3️⃣ Get Analysis

            Get eligibility, missing skills,
            match score and career roadmap.
            """
        )

    st.divider()

    st.header("💼 Available Internship Fields")

    cols = st.columns(4)

    for index, (name, data) in enumerate(CAREERS.items()):

        with cols[index % 4]:

            with st.container(border=True):

                st.subheader(
                    f"{data['emoji']} {name}"
                )

                st.write(
                    data["description"]
                )

                st.caption(
                    f"Minimum CGPA: {data['minimum_cgpa']}"
                )


# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    if not skills:

        st.warning(
            "⚠️ Please select at least one skill."
        )

        st.stop()


    # ========================================================
    # SPECIFIC FIELD
    # ========================================================

    if target_field != "Let the system recommend":

        (
            eligible,
            satisfied,
            failed,
            matched_skills,
            missing_skills
        ) = check_eligibility(
            target_field,
            cgpa,
            branch,
            graduation_year,
            skills
        )


        st.header(
            f"{CAREERS[target_field]['emoji']} "
            f"{target_field} Internship Eligibility"
        )


        # ----------------------------------------------------
        # RESULT
        # ----------------------------------------------------

        if eligible:

            st.success(
                "## ✅ ELIGIBLE\n\n"
                f"Your profile satisfies all basic "
                f"requirements for **{target_field}**."
            )

        else:

            st.error(
                "## ❌ NOT ELIGIBLE\n\n"
                f"Your profile does not satisfy all basic "
                f"requirements for **{target_field}**."
            )


        # ----------------------------------------------------
        # REQUIREMENTS
        # ----------------------------------------------------

        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "✅ Requirements Satisfied"
            )

            if satisfied:

                for item in satisfied:

                    st.write(
                        f"✅ {item}"
                    )

            else:

                st.write(
                    "No requirements satisfied."
                )


        with col2:

            st.subheader(
                "❌ Requirements Not Satisfied"
            )

            if failed:

                for item in failed:

                    st.write(
                        f"❌ {item}"
                    )

            else:

                st.success(
                    "All requirements are satisfied."
                )


        st.divider()


        # ----------------------------------------------------
        # SKILL ANALYSIS
        # ----------------------------------------------------

        st.header("🛠️ Skill Analysis")


        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "✅ Matching Skills"
            )

            if matched_skills:

                for skill in matched_skills:

                    st.success(
                        skill,
                        icon="✓"
                    )

            else:

                st.write(
                    "No matching skills."
                )


        with col2:

            st.subheader(
                "📚 Skills to Improve"
            )

            if missing_skills:

                for skill in missing_skills:

                    st.warning(
                        skill,
                        icon="!"
                    )

            else:

                st.success(
                    "You have all required skills!"
                )


        # ----------------------------------------------------
        # MATCH SCORE
        # ----------------------------------------------------

        match_score = calculate_match(
            target_field,
            skills,
            branch,
            graduation_year,
            experience,
            interests
        )


        st.divider()

        st.header("📊 Profile Match")

        st.progress(
            match_score / 100,
            text=f"{match_score}% Match"
        )


        # ----------------------------------------------------
        # ROADMAP
        # ----------------------------------------------------

        st.divider()

        st.header(
            f"📚 Roadmap for {target_field}"
        )

        for index, step in enumerate(
            CAREERS[target_field]["roadmap"],
            1
        ):

            st.write(
                f"**{index}.** {step}"
            )


    # ========================================================
    # AUTOMATIC RECOMMENDATION
    # ========================================================

    else:

        st.header(
            "🎯 Career Field Recommendation"
        )


        results = []


        for career_name in CAREERS:

            score = calculate_match(
                career_name,
                skills,
                branch,
                graduation_year,
                experience,
                interests
            )

            results.append(
                {
                    "Career": career_name,
                    "Score": score
                }
            )


        results.sort(
            key=lambda x: x["Score"],
            reverse=True
        )


        best = results[0]


        st.success(
            f"""
            ### 🎯 Recommended Career: {best["Career"]}

            Your profile has a **{best["Score"]}% match**
            with this career field.
            """
        )


        st.progress(
            best["Score"] / 100,
            text=f"{best['Score']}% Match"
        )


        # ----------------------------------------------------
        # TOP 3
        # ----------------------------------------------------

        st.divider()

        st.header("🏆 Top Career Matches")


        top3 = pd.DataFrame(
            [
                {
                    "Rank": i + 1,
                    "Career Field": item["Career"],
                    "Match Score": f"{item['Score']}%"
                }
                for i, item in enumerate(results[:3])
            ]
        )


        st.dataframe(
            top3,
            use_container_width=True,
            hide_index=True
        )


        # ----------------------------------------------------
        # BEST CAREER SKILLS
        # ----------------------------------------------------

        career = CAREERS[best["Career"]]


        matched = [
            skill
            for skill in skills
            if skill in career["skills"]
        ]


        missing = [
            skill
            for skill in career["skills"]
            if skill not in skills
        ]


        st.divider()

        st.header(
            f"🛠️ {best['Career']} Skill Analysis"
        )


        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "✅ Skills You Have"
            )

            if matched:

                for skill in matched:

                    st.success(
                        skill,
                        icon="✓"
                    )

            else:

                st.write(
                    "No directly matching skills."
                )


        with col2:

            st.subheader(
                "📚 Skills to Improve"
            )

            for skill in missing:

                st.warning(
                    skill,
                    icon="!"
                )


        # ----------------------------------------------------
        # ROADMAP
        # ----------------------------------------------------

        st.divider()

        st.header(
            f"📚 Recommended Roadmap"
        )


        for index, step in enumerate(
            career["roadmap"],
            1
        ):

            st.write(
                f"**{index}.** {step}"
            )


    # ========================================================
    # PROFILE SUMMARY
    # ========================================================

    st.divider()

    st.header("👤 Profile Summary")


    c1, c2, c3, c4 = st.columns(4)


    with c1:
        st.metric(
            "CGPA",
            f"{cgpa:.1f}"
        )


    with c2:
        st.metric(
            "Branch",
            branch
        )


    with c3:
        st.metric(
            "Skills",
            len(skills)
        )


    with c4:
        st.metric(
            "Experience",
            experience
        )


    st.divider()

    st.caption(
        "⚠️ This is a project-based eligibility checker. "
        "Actual internship eligibility depends on the "
        "requirements of the individual company."
    )
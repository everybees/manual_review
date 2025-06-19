import streamlit as st
import pandas as pd

from sections import ideal_response, model_response, user_prompt

st.set_page_config(page_title="Review & Scoring Tool", layout="wide")
st.title("Review & Scoring Tool")

if "all_reviews" not in st.session_state:
    st.session_state.all_reviews = {
        "Prompt Design Review": [],
        "Model Response Evaluation": [],
        "Ideal Response Evaluation": []
    }


error_categories = [
    "Did Not fulfill every functional requirement",
    "Issues with annotator’s judgement",
    "Inconsistent failure mode classification",
    "Redundant Logic",
    "Issues with Code Readability",
    "Too Simple",
    "Critical Errors",
    "Minor Errors"
]

mode = st.selectbox("Select Review Type", ["Prompt Design Review", "Model Response Evaluation", "Ideal Response Evaluation", "Summary Page"])

col1, col2 = st.columns([2, 1])

categories = {}
if mode == "Prompt Design Review":
    categories = ideal_response.categories
elif mode == "Model Response Evaluation":
    categories = model_response.categories
elif mode == "Ideal Response Evaluation":
    categories = user_prompt.categories
elif mode == "Summary Page":
    st.subheader("📋 Most Recent Submitted Reviews")
    combined_summary = ""
    for section in ["Prompt Design Review", "Model Response Evaluation", "Ideal Response Evaluation"]:
        if st.session_state.all_reviews[section]:
            combined_summary += f"[{section}]\n"
            combined_summary += st.session_state.all_reviews[section][-1].strip() + "\n\n"
    if combined_summary:
        st.code(combined_summary.strip(), language="markdown")
    else:
        st.info("No reviews submitted yet.")
    st.stop()

review = {}
total_penalty = 0
major_issues = 0

with col1:
    with st.form("review_form"):
        for category, issues in categories.items():
            st.markdown(f"### {category}")
            selected_issue = st.selectbox(
                f"Select issue for '{category}'",
                ["None"] + [issue for issue, _ in issues],
                key=category
            )
            improvement = st.text_area(f"Suggested improvement for '{category}'", key=f"improvement_{category}")
            penalty = 0
            if selected_issue != "None":
                penalty = dict(issues)[selected_issue]
                review[category] = (selected_issue, penalty, improvement)
                total_penalty += penalty
                if mode == "Prompt Design Review" and penalty == 1.5:
                    major_issues += 1
            else:
                review[category] = ("No issue", 0, "")

        selected_errors = st.multiselect("Select all applicable error categories:", error_categories)

        st.markdown("---")
        comments = st.text_area("Additional Comments", height=100)
        submitted = st.form_submit_button("Submit Review")

with col2:
    if 'review' in locals():
        st.markdown("### 📋 Review Summary")
        summary_rows = [(k, v[0], v[1], v[2]) for k, v in review.items()]
        summary_df = pd.DataFrame(summary_rows, columns=["Category", "Issue", "Penalty", "Improvement Suggestion"])
        st.dataframe(summary_df, use_container_width=True)

        score = max(1.0, round(5.0 - total_penalty, 1))

        if mode == "Prompt Design Review":
            verdict = "✅ Acceptable" if major_issues < 2 else "❌ Unacceptable – Must be rewritten"
            st.markdown(f"**Total Penalty:** `{total_penalty}`")
            st.markdown(f"**Major Issues:** `{major_issues}`")
            st.markdown(f"**Final Score:** `{score}`")
            st.markdown(f"**Final Verdict:** `{verdict}`")
        else:
            score = max(1.0, round(5.0 - total_penalty, 1))
            if score >= 4.5:
                rating = "Flawless"
            elif score >= 3.5:
                rating = "Strong"
            elif score >= 2.5:
                rating = "Adequate"
            elif score >= 1.0:
                rating = "Weak"
            else:
                rating = "Failed"
            st.markdown(f"**Total Penalty:** `{total_penalty}`")
            st.markdown(f"**Final Score:** `{score}`")
            st.markdown(f"**Rating:** `{rating}`")

        st.markdown("### 📎 Copyable Summary")
        summary_text = ""
        if mode == "Prompt Design Review":
            summary_text += f"Total Penalty: {total_penalty}\nMajor Issues: {major_issues}\nVerdict: {verdict}\n"
        else:
            summary_text += f"Final Score: {score}\nRating: {rating}\n"
        summary_text += "\nIssues & Suggestions:\n"
        for cat, (issue, penalty, improvement) in review.items():
            summary_text += f"- {cat}: {issue} (Penalty: {penalty})\n  Improvement: {improvement}\n"
        summary_text += "\n\nError Categories:\n"
        for err in selected_errors:
            summary_text += f"- {err}\n"
        summary_text += f"\nComments:\n{comments}"
        st.code(summary_text.strip(), language="markdown")

        # Save to session state
        st.session_state.all_reviews[mode].append(summary_text.strip())

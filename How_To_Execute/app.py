import streamlit as st
import pandas as pd
from collections import deque
import zipfile
import io

# -------------------------------
# Utility Functions
# -------------------------------

def get_group_stats(groups, group_type):
    stats = []
    for i, group in enumerate(groups, start=1):
        df_group = pd.DataFrame(group)
        if df_group.empty:
            continue
        branch_counts = df_group["Roll"].str[4:6].value_counts().to_dict()
        total = len(df_group)

        row = {"Group": f"{group_type}_{i}", "Total Students": total}
        for branch, count in branch_counts.items():
            row[f"{branch}_count"] = count
            row[f"{branch}_percent"] = round((count / total) * 100, 2) if total > 0 else 0

        stats.append(row)

    return pd.DataFrame(stats)


def create_mixed_groups(df, n, group_size):
    branch_data = {}
    for branch, group in df.groupby("Branch"):
        g = group[["Name", "Email", "Roll"]]
        branch_data[branch] = deque(g.to_dict("records"))

    sorted_branch_data = dict(
        sorted(branch_data.items(), key=lambda item: len(item[1]), reverse=True)
    )

    groups = [[] for _ in range(n)]
    mixed_list = []

    while any(branch_data.values()):
        for branch in sorted_branch_data.keys():
            b = sorted_branch_data[branch]
            if b:
                student = b.popleft()
                mixed_list.append(student)

    for i in range(n - 1):
        groups[i] = mixed_list[group_size * i: group_size * (i + 1)]
    groups[n - 1] = mixed_list[group_size * (n - 1):]

    return groups


def create_uniform_groups(df, n, group_size):
    branch_data = {}
    for branch, group in df.groupby("Branch"):
        g = group[["Name", "Email", "Roll"]]
        branch_data[branch] = deque(g.to_dict("records"))

    sorted_branch_data = dict(
        sorted(branch_data.items(), key=lambda item: len(item[1]), reverse=True)
    )

    uniform_list = []
    for i in sorted_branch_data.values():
        for j in i:
            uniform_list.append(j)

    uniform_groups = [[] for _ in range(n)]
    for i in range(n - 1):
        uniform_groups[i] = uniform_list[group_size * i: group_size * (i + 1)]
    uniform_groups[n - 1] = uniform_list[group_size * (n - 1):]

    return uniform_groups


def create_branchwise_groups(df):
    branch_groups = []
    for branch, group in df.groupby("Branch"):
        g = group[["Name", "Email", "Roll"]].to_dict("records")
        branch_groups.append((branch, g))
    return branch_groups


def make_zip_file(groups, stats_df, prefix, branchwise=False):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zf:
        if branchwise:
            # Save per-branch CSVs
            for branch, group in groups:
                gdf = pd.DataFrame(group)
                csv_bytes = gdf.to_csv(index=False).encode("utf-8")
                zf.writestr(f"{prefix}/{branch}.csv", csv_bytes)
        else:
            # Save group files
            for i, group in enumerate(groups, start=1):
                gdf = pd.DataFrame(group)
                csv_bytes = gdf.to_csv(index=False).encode("utf-8")
                zf.writestr(f"{prefix}/group_{i}.csv", csv_bytes)

            # Save stats
            stats_csv = stats_df.to_csv(index=False).encode("utf-8")
            zf.writestr(f"{prefix}/{prefix}_stats.csv", stats_csv)

    buffer.seek(0)
    return buffer


# -------------------------------
# Streamlit App
# -------------------------------

st.title("🎯 Student Grouping Tool")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])
n = st.number_input("Enter number of groups", min_value=2, step=1)

if uploaded_file and n:
    df = pd.read_excel(uploaded_file)
    df["Branch"] = df["Roll"].str[4:6]

    group_size = len(df) // n
    st.write(f"📊 Approx group size: {group_size}")

    option = st.radio(
        "Choose grouping method",
        ["Mixed Groups", "Uniform Groups", "Branchwise Groups"]
    )

    # --- Mixed Groups ---
    if option == "Mixed Groups":
        mixed_groups = create_mixed_groups(df, n, group_size)
        mixed_stats = get_group_stats(mixed_groups, "Mixed")

        st.subheader("📌 Mixed Groups Stats")
        st.dataframe(mixed_stats)

        mixed_zip = make_zip_file(mixed_groups, mixed_stats, "mixed_groups")
        st.download_button(
            label="⬇️ Download Mixed Groups (ZIP)",
            data=mixed_zip,
            file_name="mixed_groups.zip",
            mime="application/zip"
        )

    # --- Uniform Groups ---
    elif option == "Uniform Groups":
        uniform_groups = create_uniform_groups(df, n, group_size)
        uniform_stats = get_group_stats(uniform_groups, "Uniform")

        st.subheader("📌 Uniform Groups Stats")
        st.dataframe(uniform_stats)

        uniform_zip = make_zip_file(uniform_groups, uniform_stats, "uniform_groups")
        st.download_button(
            label="⬇️ Download Uniform Groups (ZIP)",
            data=uniform_zip,
            file_name="uniform_groups.zip",
            mime="application/zip"
        )

    # --- Branchwise Groups ---
    else:
        branch_groups = create_branchwise_groups(df)

        st.subheader("📌 Branchwise Groups")
        for branch, group in branch_groups:
            st.write(f"**Branch {branch}** - {len(group)} students")
            st.dataframe(pd.DataFrame(group))

        branch_zip = make_zip_file(branch_groups, None, "branchwise_groups", branchwise=True)
        st.download_button(
            label="⬇️ Download Branchwise Groups (ZIP)",
            data=branch_zip,
            file_name="branchwise_groups.zip",
            mime="application/zip"
        )

    st.success("✅ Grouping complete!")

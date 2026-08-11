import streamlit as st
from characters import CHARACTERS

# Page config
st.set_page_config(
    page_title="Mythic Codex", 
    page_icon="🔮",
    layout="wide"
    )

st.title("The Mythic Codex Dashboard")
st.caption("Interactive Character & Stage Synchronization Explorer")

# Sidebar
st.sidebar.header("Navigation")
app_mode = st.sidebar.radio("Select View", ["Character Compendium", "Stage Comparator"])

if app_mode == "Character Compendium":
    selected_name = st.sidebar.selectbox("Choose a Character", list(CHARACTERS.keys()))
    char = CHARACTERS[selected_name]

    # Header card
    st.markdown(f"# {selected_name}")
    st.markdown(
        f"**Mythic Affinity:** <code style='color:{char['color']}; background-color: #1E293B; padding: 2px 8px; border-radius: 6px;'>{char['affinity']}</code> | "
        f"**Archetype:** {char['archetype']}",
        unsafe_allow_html=True
    )
    st.write(char['description'])

    st.divider()

    # Stage tabs
    st.subheader("Transformation Stages")
    tabs = st.tabs(list(char["stages"].keys()))

    for i, (stage_name, stage_data) in enumerate(char["stages"].items()):
        with tabs[i]:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### Physical Transformation")
                st.info(stage_data["transform"])
            with col2:
                st.markdown("### Abilities & Traits")
                st.success(stage_data["abilities"])

elif app_mode == "Stage Comparator":
    st.subheader("Compare Characters at Spesific Stage")

    col1,col2,col3 = st.columns([2,2,1])
    with col1:
        char1_name = st.selectbox("Character 1", list(CHARACTERS.keys()), index=0)
    with col2:
        char2_name = st.selectbox("Character 2", list(CHARACTERS.keys()), index=1)
    with col3:
        stage_level = st.selectbox("Stage", ["Stage I: Echo", "Stage II: Aspect", "Stage III: Mantle", "Stage IV: Apotheosis"])

    c1 = CHARACTERS[char1_name]
    c2 = CHARACTERS[char2_name]

    st.divider()

    left_col, right_col = st.columns(2)

    with left_col:
        st.markdown(f"### {char1_name} ({c1['affinity']})")
        st.write("**Tranformation:**", c1["stages"][stage_level]["transform"])
        st.write("**Abilities:**", c1["stages"][stage_level]["abilities"])

    with left_col:
        st.markdown(f"### {char2_name} ({c2['affinity']})")
        st.write("**Tranformation:**", c2["stages"][stage_level]["transform"])
        st.write("**Abilities:**", c2["stages"][stage_level]["abilities"])
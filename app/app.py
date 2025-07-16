import streamlit as st
import yaml
import os
from main import run_pipeline_streamlit
from storage.minio_client import list_files  # You may need to implement this if not done


CONFIG_PATH = "config/params.yaml"

# Load available files from MinIO
def get_available_files():
    return list_files(bucket="survey-dataset")  # Replace with your actual MinIO client

# UI to edit configuration
def config_ui(default_config):
    st.sidebar.title("Configuration Panel")

    # Storage
    st.sidebar.subheader("Storage")
    file_options = get_available_files()
    selected_file = st.sidebar.selectbox("Select file from MinIO", file_options)
    default_config['storage']['object_name'] = selected_file

    # Cleaning
    st.sidebar.subheader("Cleaning")
    default_config['cleaning']['fill_value'] = st.sidebar.number_input("Fill missing with", value=0)
    default_config['cleaning']['drop_thresh'] = st.sidebar.slider("Drop threshold", 0.0, 1.0, value=0.8)
    default_config['cleaning']['exclude_recontact_features'] = st.sidebar.checkbox("Exclude recontact features", value=False)

    # Feature Engineering
    st.sidebar.subheader("Feature Engineering")
    default_config['features']['min_unique'] = st.sidebar.number_input("Min unique values", value=1)
    default_config['features']['use_variance_threshold'] = st.sidebar.checkbox("Use Variance Threshold", value=True)

    # Dimensionality Reduction
    st.sidebar.subheader("Dimensionality Reduction")
    default_config['reduction']['method'] = st.sidebar.selectbox("Reduction method", ["pca", "umap"])
    default_config['reduction']['n_components'] = st.sidebar.slider("n_components", 2, 50, value=2)

    # Clustering
    st.sidebar.subheader("Clustering")
    default_config['clustering']['method'] = st.sidebar.selectbox("Clustering Method", ["kmeans", "agglomerative"])
    default_config['clustering']['n_clusters'] = st.sidebar.slider("Number of clusters", 2, 20, value=3)

    return default_config

# Save YAML config
def save_config(config):
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(config, f)


def main():
    st.title("Survey Clustering Pipeline UI")
    st.write("Run and configure your clustering pipeline interactively.")

    # Load current params.yaml
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)

    updated_config = config_ui(config)

    if st.button("Run Pipeline"):
        save_config(updated_config)
        with st.spinner("Running pipeline..."):
            score, figs = run_pipeline_streamlit(updated_config)

        st.success("Pipeline completed! 🎉")
        st.markdown(f"**Silhouette Score**: `{score:.3f}`")

        for fig in figs:
            st.pyplot(fig)


if __name__ == "__main__":
    main()

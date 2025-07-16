import argparse
import yaml
from ingestion import ingest
from processing import clean, feature_engineering, dimensionality_reduction
from clustering import cluster, evaluate
from visualization import cluster_viz


def run_pipeline(params):
    print("Running pipeline...")
    df = ingest.load_data(params['storage'])
    print("Data loaded...")
    df_clean = clean.clean_data(df, params['cleaning'])
    print("Data cleaned...")
    print("shape", df_clean.shape)
    df_features = feature_engineering.build_features(df_clean, params['features'])
    print("Features built...")
    df_reduced = dimensionality_reduction.reduce(df_features, params['reduction'])
    print("Data reduced...")
    labels = cluster.run_clustering(df_reduced, params['clustering'])
    print("Clustering completed...")
    evaluate.print_scores(df_reduced, labels)
    cluster_viz.visualize(df_reduced, labels, params['clustering'])


def run_pipeline_streamlit(params):
    df = ingest.load_data(params['storage'])
    df_clean = clean.clean_data(df, params['cleaning'])
    df_features = feature_engineering.build_features(df_clean, params['features'])
    df_reduced = dimensionality_reduction.reduce(df_features, params['reduction'])
    labels = cluster.run_clustering(df_reduced, params['clustering'])

    score = evaluate.print_scores(df_reduced, labels)
    figs = cluster_viz.get_cluster_plots(df_reduced, labels, params['clustering'])
    return score, figs


if __name__ == '__main__':
    with open('config/params.yaml') as f:
        params = yaml.safe_load(f)
    run_pipeline(params)

# Datastore to BigQuery

## Docker image for exporting from Datastore

This dockerimage can be used to e.g schedule DataStore exports through a kubernetes cronjob. Some environment variables need to be set:

- `GCP_BUCKET`: cloud storage bucket to export to 
- `GCP_KEYFILE`: json keyfile for service account to use
- `GCP_PROJECT`: your GCP project

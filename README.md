# Datastore Exporter 

Docker image that triggers Google Datastore exports to a Google cloud storage bucket

## Build
```
docker build -f docker/Dockerfile.export -t datastore-exporter .
```

## Run 

This dockerimage can be used to e.g schedule DataStore exports through a kubernetes cronjob. Some environment variables need to be set:

- `GCP_BUCKET`: cloud storage bucket to export to 
- `GCP_KEYFILE`: json keyfile for service account to use
- `GCP_PROJECT`: your GCP project
- `GCP_DATASTORE_KIND`: the datastore kind in the default namespace that you want to export 

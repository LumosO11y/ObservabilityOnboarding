# Overview
Subjects we will cover:

## Pipeline Basics
- The `.gitlab-ci.yml` file
- Stages and Jobs
- `script`, `before_script`, `after_script`
- Pipeline triggers: push, merge request, schedule, manual, API

## Runners
- Shared, Group, and Project Runners
- Runner executors (shell, docker, kubernetes)
- Tags and runner selection

## Jobs & Workflow Control
- `rules` vs the legacy `only`/`except`
- `needs` (DAG pipelines) vs stage-based ordering
- Artifacts and caching
- Environments and deployments
- Manual jobs and approvals

## Configuration & Reuse
- CI/CD Variables (project, group, instance level) and protected/masked variables
- `include` (local, project, remote, template)
- `extends` and YAML anchors
- Templates

## Security & Access Control
- Protected branches and protected variables
- Merge request pipelines vs branch pipelines
- Secret handling best practices

## Observability
- Pipeline visualization and job logs
- Artifact browsing
- Notifications on pipeline/job failure

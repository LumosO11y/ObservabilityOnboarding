# GitlabCI

## Overview

GitlabCI is our push-based pipeline tool: pipelines run in response to events in the Git repository (a push, a merge request, a schedule) and drive the build/test/deploy stages from there. This part goes deep on how pipelines are configured and run, as the push-based counterpart to ArgoCD's pull-based GitOps model from the previous part.

## Goals

Subjects we will cover:

**Pipeline Basics**
- The `.gitlab-ci.yml` file
- Stages and Jobs
- `script`, `before_script`, `after_script`
- Pipeline triggers: push, merge request, schedule, manual, API

**Runners**
- Shared, Group, and Project Runners
- Runner executors (shell, docker, kubernetes)
- Tags and runner selection

**Jobs & Workflow Control**
- `rules` vs the legacy `only`/`except`
- `needs` (DAG pipelines) vs stage-based ordering
- Artifacts and caching
- Environments and deployments
- Manual jobs and approvals

**Configuration & Reuse**
- CI/CD Variables (project, group, instance level) and protected/masked variables
- `include` (local, project, remote, template)
- `extends` and YAML anchors
- Templates

**Security & Access Control**
- Protected branches and protected variables
- Merge request pipelines vs branch pipelines
- Secret handling best practices

**Observability**
- Pipeline visualization and job logs
- Artifact browsing
- Notifications on pipeline/job failure

## Outcome

<details>
<summary>Questions to test your comprehension of GitlabCI</summary>

### Pipeline Basics
1. What are the required top-level pieces of a `.gitlab-ci.yml` file? How do stages and jobs relate to each other?
2. What's the difference between `script`, `before_script`, and `after_script`? What happens if `before_script` fails?
3. Name the different ways a pipeline can be triggered. When would you use a scheduled pipeline versus a manual one?

### Runners
1. What is the difference between a shared, group, and project runner? When would you provision a dedicated runner instead of using shared ones?
2. What is a runner executor, and how does the `docker` executor differ from the `shell` executor?
3. How do tags control which runner picks up a job?

### Jobs & Workflow Control
1. Why was `rules` introduced to replace `only`/`except`? Give an example `rules` block that only runs a job on merge requests.
2. What does `needs` let you do that stage-based ordering alone doesn't?
3. What's the difference between an artifact and the cache? When does each get cleared?
4. What is a manual job, and how does it interact with approvals in a deployment pipeline?

### Configuration & Reuse
1. What are the three levels CI/CD variables can be defined at, and what does marking one "protected" or "masked" actually do?
2. What's the difference between `include` and `extends`? When would you reach for a YAML anchor instead of either?

### Security & Access Control
1. What is a protected branch, and how does it interact with protected variables?
2. What's the difference between a merge request pipeline and a branch pipeline? Why does that distinction matter for secret handling?

### Observability
1. Where do you go to see why a specific job failed, and what's browsable from a completed pipeline's artifacts?
2. How would you set up a notification for a failed pipeline on a protected branch?

</details>

### Links

- <https://docs.gitlab.com/ee/ci/>
- <https://docs.gitlab.com/ee/ci/yaml/>

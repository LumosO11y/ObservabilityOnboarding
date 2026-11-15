# GitlabCI

## Overview

GitlabCI is our push-based pipeline tool: pipelines run in response to events in the Git repository (a push, a merge request, a schedule) and drive the build/test/deploy stages from there. This part covers how pipelines are configured and run. The next part covers ArgoCD, its pull-based counterpart.

## Goals

Subjects we will cover:

**Pipeline Basics**

- The `.gitlab-ci.yml` file
- Stages and Jobs
- Runners and tags

**Workflow Control**

- `rules`
- Merge request pipelines vs branch pipelines

**Configuration & Reuse**

- CI/CD Variables and protected/masked variables
- `include` and `extends`, and how our internal CI library is consumed

**Observability**

- Pipeline visualization and job logs

## Outcome

<details>
<summary>Questions to test your comprehension of GitlabCI</summary>

### Pipeline Basics

1. What are the required top-level pieces of a `.gitlab-ci.yml` file? How do stages and jobs relate to each other?
2. What is a runner, and how does a job end up running on a specific one?

### Workflow Control

1. What does `rules` control? Give an example `rules` block that only runs a job on merge requests.
2. What's the difference between a merge request pipeline and a branch pipeline? Why does that distinction matter for secret handling?

### Configuration & Reuse

1. At what levels can CI/CD variables be defined? What does marking one "protected" or "masked" actually do, and how do protected variables interact with protected branches?
2. Our pipelines are built on an internal CI library (ask your mentor for it). How does a project pull in shared CI configuration with `include`, and how do you use `extends` to adjust a job you got from it? Find one of our projects that uses the library and explain what its `.gitlab-ci.yml` ends up running.

### Observability

1. Where do you go to see why a specific job failed, and what's browsable from a completed pipeline's artifacts?

</details>

### Links

- <https://docs.gitlab.com/ci/>
- <https://docs.gitlab.com/ci/yaml/>
- <https://docs.gitlab.com/ci/yaml/includes/>
- <https://docs.gitlab.com/ci/variables/>

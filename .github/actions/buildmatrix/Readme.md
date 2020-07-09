# GitHub Action for Git flow process

The GitHub Action for Git flow process enforce the process of Git flow in your repository.
Enforce only pull request head and base.

|base (to)|head (from)|
|--|--|
|develop|feature/, release/, hotfix/|
|master|develop,hotfix|

## Usage

```yaml
- name: Run Git flow enforcer
  uses: ./.github/actions/git/gitflow-process
  env:
    GITHUB_PAYLOAD: ${{ toJson(github) }}
    GITHUB_TOKEN: ${{ secrets.azure_scale_devops_token }}
```

### Environment variables

- `GITHUB_PAYLOAD` – **Required** - Use built in variable from Github Action
- `GITHUB_TOKEN` – **Required** - Github token with validate the pull request
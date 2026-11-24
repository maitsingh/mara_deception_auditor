#!/usr/bin/env bash
# Run this yourself to create a PUBLIC repository and configure GitHub Pages.
# It never force-pushes or replaces an unrelated origin.
set -euo pipefail
cd "$(dirname "$0")/.."
repo_name="${1:-under-observation}"
if [[ ! "$repo_name" =~ ^[A-Za-z0-9._-]+$ ]]; then
  printf 'Use a repository name containing letters, numbers, dots, underscores or hyphens.\n' >&2
  exit 1
fi
command -v git >/dev/null || { printf 'Install Git first.\n' >&2; exit 1; }
command -v gh >/dev/null || { printf 'Install GitHub CLI from https://cli.github.com, or follow docs/GITHUB_SETUP.md.\n' >&2; exit 1; }
gh auth status >/dev/null 2>&1 || gh auth login
owner="$(gh api user --jq .login)"
owner_id="$(gh api user --jq .id)"
profile_name="$(gh api user --jq '.name // .login')"
full_name="$owner/$repo_name"
if [[ ! -d .git ]]; then git init -b main; fi
if ! git config user.name >/dev/null; then git config user.name "$profile_name"; fi
if ! git config user.email >/dev/null; then
  git config user.email "$owner_id+$owner@users.noreply.github.com"
fi
if git remote get-url origin >/dev/null 2>&1; then
  origin_url="$(git remote get-url origin)"
  case "$origin_url" in
    "https://github.com/$full_name"|"https://github.com/$full_name.git"|"git@github.com:$full_name"|"git@github.com:$full_name.git") ;;
    *) printf 'An unrelated origin already exists; leaving it unchanged. Follow docs/GITHUB_SETUP.md.\n' >&2; exit 1 ;;
  esac
fi
git add .
if ! git diff --cached --quiet; then
  git commit -m "Add oversight study, interpretable analysis, site and poster"
fi
if gh repo view "$full_name" --json nameWithOwner >/dev/null 2>&1; then
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/$full_name.git"
  fi
else
  gh repo create "$full_name" --public --source=. --remote=origin
fi
git push -u origin HEAD:main
printf '\nRepository: https://github.com/%s\n' "$full_name"
if ! gh api "repos/$full_name/pages" >/dev/null 2>&1; then
  if ! gh api --method POST "repos/$full_name/pages" \
    --field 'source[branch]=main' --field 'source[path]=/' >/dev/null; then
    printf 'Enable Pages manually: Settings > Pages > Deploy from a branch > main > / (root).\n'
    exit 0
  fi
fi
printf 'Configured Pages URL (deployment may still be pending):\n'
gh api "repos/$full_name/pages" --jq .html_url
printf 'Open the deployed URL and verify the page before submitting it.\n'

#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

# -----------------------------------------------------------------------------
# Helper functions start with _ and aren't listed in this script's help menu.
# -----------------------------------------------------------------------------

function _pipenv_run {
  pipenv run "${@}"
}

function _pipenv_script {
  _pipenv_run python "${@}"
}

# -----------------------------------------------------------------------------

function cmd {
  # Run any command you want in the web container
  _pipenv_run "${@}"
}

function python {
  _pipenv_script "${@}"
}

function lint {
  # Lint Python code
  cmd flake8 "${@}"
}

function format {
  # Format Python code
  cmd black . "${@}"
}

function help {
  printf "%s <task> [args]\n\nTasks:\n" "${0}"

  compgen -A function | grep -v "^_" | cat -n

  printf "\nExtended help:\n  Each task has comments for general usage\n"
}

# This idea is heavily inspired by: https://github.com/adriancooney/Taskfile
TIMEFORMAT=$'\nTask completed in %3lR'
time "${@:-help}"
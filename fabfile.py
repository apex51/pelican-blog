import os
import shutil
import sys
from invoke import task

env = {}
env['deploy_path'] = 'output'
env['github_pages_branch'] = 'gh_pages'
env['PATH'] = os.environ['PATH'] + ':/Users/hao/.gitconfig'

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(env['deploy_path']):
        shutil.rmtree(env['deploy_path'])

@task()
def build(c):
    """Build local version of site"""
    c.run('pelican -s pelicanconf.py', env=env)

@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run('pelican -d -s pelicanconf.py', env=env)

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run('pelican -r -s pelicanconf.py', env=env)

@task
def serve(c):
    """Serve site at http://localhost:8000/"""
    c.run('cd {deploy_path} && python -m pelican.server'.format(**env), env=env)

@task
def reserve(c):
    """`build`, then `serve`"""
    rebuild(c)
    serve(c)

@task
def preview(c):
    """Build production version of site"""
    c.run('pelican -s publishconf.py', env=env)

@task
def deploy(c):
    """Publish to GitHub Pages"""
    rebuild(c)
    c.run('git add .', env=env)
    c.run('git add -u', env=env)
    c.run('git commit -m "deploy by fab"', env=env)
    c.run('ghp-import {deploy_path}'.format(**env), env=env)
    c.run('git push -f --all origin', env=env)

@task
def test(c):
    c.run('echo $PATH', env=env)
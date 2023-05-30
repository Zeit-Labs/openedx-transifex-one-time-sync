# list all transifex projects and their resources

import configparser
import re
import sys
from os import getenv
from os.path import expanduser

from transifex.api import transifex_api


IGNORED_PROJECTS = [
    'open-edx-releases',
    'demox-course',
    'edx101',
    'edx-themes',
]


def get_transifex_organization_projects():
    """
    Get openedx-translations project from Transifex.
    """
    transifex_api_token = getenv('TRANSIFEX_API_TOKEN')
    if not transifex_api_token:
        config = configparser.ConfigParser()
        config.read(expanduser('~/.transifexrc'))
        transifex_api_token = config['https://www.transifex.com']['password']

    if not transifex_api_token:
        raise Exception(
            'Error: No auth token found. '
            'Set transifex API token via TRANSIFEX_API_TOKEN environment variable or via the ~/.transifexrc file.'
        )

    transifex_api.setup(auth=transifex_api_token)

    return transifex_api.Organization.get(slug='open-edx').fetch('projects')


def get_transifex_new_project():
    return get_transifex_organization_projects().get(slug='openedx-translations')


def get_old_projects():
    return [
        project for project in get_transifex_organization_projects()
        if project.slug != 'openedx-translations' and project.slug not in IGNORED_PROJECTS
    ]


def print_all_resources():
    for project in get_old_projects():
        print(f'## {project.slug}')
        for resource in project.fetch('resources'):
            print(f' - slug: "{resource.slug}"')

    print(f'## openedx-translations')
    for resource in get_transifex_new_project().fetch('resources'):
        print(f' - name: "{resource.name}" slug: "{resource.slug}"')


if __name__ == '__main__':
    print_all_resources()

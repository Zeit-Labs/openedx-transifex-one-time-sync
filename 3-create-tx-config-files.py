"""
resources_pairs is generated from 1-projects.md: https://chat.openai.com/share/c832a4b7-c1c5-4628-b702-8a1ade4a813a

below is a list of transifex resources in their projects
print a list of openedx-translations resources with their closest match from other projects
keep only one match at maxi
remove those without a match
print it in python array of dicts with three fields "resource_name", "resource_slug", "pair_slug", "pair_project"

"""

import configparser
from os import getenv
from os.path import expanduser

import requests
from transifex.api import transifex_api


resources_plan = [
    {
        "resource_name": "edx-ora2",
        "resource_slug": "ae518fadaa8a0d0027a1b36c4e6e367a",
        "pair_slug": "openassessment",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "edx-ora2-js",
        "resource_slug": "0b27792ea213cebf5cddad529a8cd442",
        "pair_slug": "openassessment-js",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "edx-proctoring",
        "resource_slug": "66cfa04d24daa4089acf61c5b11ee883",
        "pair_slug": "edx-proctoring",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "studio-frontend",
        "resource_slug": "862137d25aff8ed766d3dec238ce833a",
        "pair_slug": "studio-frontend",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "DoneXBlock",
        "resource_slug": "b8933764bdb3063ca09d6aa20341102f",
        "pair_slug": "xblock-done",
        "pair_project_slug": "xblocks",
    },
    {
        "resource_name": "xblock-drag-and-drop-v2",
        "resource_slug": "bf47016dfec2eaf5710e1890d0ee0188",
        "pair_slug": "drag-and-drop-v2",
        "pair_project_slug": "xblocks",
    },
    {
        "resource_name": "xblock-free-text-response",
        "resource_slug": "f3036886abbc04d70445374bc01e562e",
        "pair_slug": "xblock-free-text-response",
        "pair_project_slug": "xblocks",
    },
    {
        "resource_name": "course-discovery-course-discovery",
        "resource_slug": "translations-course-discovery-course-discovery-conf-locale-en-lc-messages-djangojs-po--main",
        "pair_slug": "course_discovery",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "credentials-credentials",
        "resource_slug": "translations-credentials-credentials-conf-locale-en-lc-messages-djangojs-po--main",
        "pair_slug": "credentials",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-account",
        "resource_slug": "translations-frontend-app-account-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-account",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-authn",
        "resource_slug": "translations-frontend-app-authn-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-authn",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-course-authoring",
        "resource_slug": "translations-frontend-app-course-authoring-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-course-authoring",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-discussions",
        "resource_slug": "translations-frontend-app-discussions-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-discussions",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-ecommerce",
        "resource_slug": "translations-frontend-app-ecommerce-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-ecommerce",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-gradebook",
        "resource_slug": "translations-frontend-app-gradebook-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-gradebook",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-learner-dashboard",
        "resource_slug": "translations-frontend-app-learner-dashboard-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-learner-dashboard",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-learner-record",
        "resource_slug": "translations-frontend-app-learner-record-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-learner-record",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-learning",
        "resource_slug": "translations-frontend-app-learning-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-learning",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-profile",
        "resource_slug": "translations-frontend-app-profile-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-profile",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-app-program-console",
        "resource_slug": "translations-frontend-app-program-console-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-app-program-manager",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-component-footer",
        "resource_slug": "translations-frontend-component-footer-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-component-footer",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "frontend-component-header",
        "resource_slug": "translations-frontend-component-header-src-i18n-transifex-input-json--main",
        "pair_slug": "frontend-component-header",
        "pair_project_slug": "edx-platform",
    },
    {
        "resource_name": "paragon",
        "resource_slug": "translations-paragon-src-i18n-transifex-input-json--main",
        "pair_slug": "paragon",
        "pair_project_slug": "edx-platform",
    },
]


ORGANIZATION_SLUG = 'open-edx'
LANGUAGES = [
    'ar',
    'fr_CA',
    'de',
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

    return transifex_api.Organization.get(slug=ORGANIZATION_SLUG).fetch('projects')


def sync_pair_into_new_resource():
    projects = get_transifex_organization_projects()
    new_project = projects.get(slug='openedx-translations')

    with open('download/.tx/config', 'w') as download_file, open('upload/.tx/config', 'w') as upload_file:
        
        download_file.write(f'[main]\nhost = https://www.transifex.com\n')
        upload_file.write(f'[main]\nhost = https://www.transifex.com\n')

        for plan in resources_plan:
            resource_id = f'o:{ORGANIZATION_SLUG}:p:{new_project.slug}:r:{plan["resource_slug"]}'
            pair_id = f'o:{ORGANIZATION_SLUG}:p:{plan["pair_project_slug"]}:r:{plan["pair_slug"]}'

            download_file.write(f'[{pair_id}]\nfile_filter = resources/<lang>.po\nsource_file = resources/<lang>.po\nsource_lang = en\n')

            upload_file.write(f'[{resource_id}]\nfile_filter = resources/<lang>.po\nsource_file = resources/<lang>.po\nsource_lang = en\n')


if __name__ == '__main__':
    sync_pair_into_new_resource()

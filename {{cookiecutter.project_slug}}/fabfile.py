# -*- coding: utf-8 -*-
"""
fabfile to deploy {{cookiecutter.project_name}} to server

- Requirements:
    fabric==2.0.1
    asn1crypto==0.24.0
    bcrypt==3.1.4
    cffi==1.11.5
    cryptography==2.2.2
    invoke==1.0.0
    paramiko==2.4.1
    pyasn1==0.4.3
    pycparser==2.18
    pynacl==1.2.1

    slackclient==1.2.1
    websocket-client==0.47.0

- Usage:
    fab -H my-server deploy

"""

import traceback
import logging
from slackclient import SlackClient
from fabric import Connection
from invoke import task

# Configuration
# -----------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

WORK_DIR = '/deploy'

# file storage last git commit id
LAST_CID_FILE = "last_commit_id.txt"

# Config slack for notification
SLACK_API_KEY = "xxx-xxx-xxx"
CHANNEL_NAME = "#random"


# Utils functions
# -----------------------------------------
class Slacker:
    COLOR_GOOD = 'good'

    sc = SlackClient(SLACK_API_KEY)

    def send(self, **kargs):
        try:
            self.sc.api_call(
                "chat.postMessage",
                channel=CHANNEL_NAME,
                username='Deployment',
                # as_user=True,
                icon_emoji=":gear:",
                **kargs
            )
        except Exception:
            traceback.print_exc()

    def send_attachment(self, message_text, title, text, color='good'):
        attachments = [
            {
                "color": color,
                "title": title,
                "text": text,
            },
        ]
        self.send(attachments=attachments, text=message_text)


sc = Slacker()


def run(c, command, capture=False):
    result = c.run(command, echo=True)
    if capture:
        return result.stdout.strip()
    return result


def get_current_commit(c):
    return run(c, "git rev-parse HEAD", True)


def save_last_commit(c):
    run(c, "git rev-parse HEAD > {}".format(LAST_CID_FILE))


def get_last_commit(c):
    return run(c, "cat {}".format(LAST_CID_FILE), True)


def get_git_logs(c, last_commit_id, current_commit_id):
    return run(c, "git log {}...{} --oneline --pretty=format:'%s'".format(last_commit_id, current_commit_id), True)


def notify_commit_applied(c):
    last_commit_id = get_last_commit(c)
    current_commit_id = get_current_commit(c)
    commit_applied = get_git_logs(c, last_commit_id, current_commit_id)
    if commit_applied:
        commit_applied = "••• " + commit_applied
        commit_applied = commit_applied.replace("\n", "\n••• ")
    else:
        commit_applied = 'No commit applied!'

    sc.send_attachment("Deploy to *{}* success".format(c.host), "Commit applied:", commit_applied)


def notify_start_deploy(c):
    user = c.local('whoami').stdout
    sc.send(text="Sender ({}) - Started by user {}".format(c.host, user))


@task
def deploy(c):
    notify_start_deploy(c)
    logger.info("Deploying on {}".format(c.host))
    with c.cd(WORK_DIR):
        if c.run('test -f {}'.format(LAST_CID_FILE), warn=True).failed:
            logger.info("Create {} file".format(LAST_CID_FILE))
            save_last_commit(c)
        run(c, 'git pull origin master')
        docker_restart(c)
        notify_commit_applied(c)
        save_last_commit(c)


def docker_restart(c):
    run(c, 'docker-compose restart {{cookiecutter.project_slug}}')

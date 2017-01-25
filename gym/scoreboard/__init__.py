"""
Docs on how to do the markdown formatting:
http://docutils.sourceforge.net/docs/user/rst/quickref.html

Tool for previewing the markdown:
http://rst.ninjs.org/
"""

import os

from gym.scoreboard.client.resource import Algorithm, Evaluation, FileUpload
from gym.scoreboard.registration import registry, add_task, add_group

# Discover API key from the environment. (You should never have to
# change api_base / web_base.)
api_key = os.environ.get('OPENAI_GYM_API_KEY')
api_base = os.environ.get('OPENAI_GYM_API_BASE', 'https://gym-api.openai.com')
web_base = os.environ.get('OPENAI_GYM_WEB_BASE', 'https://gym.openai.com')

# The following controls how various tasks appear on the
# scoreboard. These registrations can differ from what's registered in
# this repository.

# groups

add_group(
    id='classic_control',
    name='Classic control',
    description='Classic control problems from the RL literature.'
)

add_group(
    id='space_fortress',
    name='Space Fortress',
    description="Groups which contains all SF versions."
)

# Space Fortress

add_task(
    id='SF-v0',
    group='space_fortress',
    summary='Simulation game for NLR',
    description="""
Try to blow up the fort while navigating and dodging its attacks.
""",
)

add_task(
    id='SFS-v0',
    group='space_fortress',
)

add_task(
    id='SFC-v0',
    group='space_fortress',
)

add_task(
    id='AIM-v0',
    group='space_fortress',
)

registry.finalize()

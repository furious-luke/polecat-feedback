import time

from polecat_feedback.decorators import feedback
from polecat_feedback.renderer import Renderer


@feedback('Toplevel')
def toplevel(feedback=None):
    feedback.declare_steps('Step 1', 'Step 2', 'Step 3')
    step1(parent_feedback=feedback)
    step2(parent_feedback=feedback)
    step3(parent_feedback=feedback)


@feedback('Step 1')
def step1(feedback=None):
    with feedback('Running operation 1'):
        time.sleep(1)
        feedback.add_warning('Careful ...')
    time.sleep(1)
    with feedback('Running operation 2'):
        time.sleep(1)


@feedback('Step 2')
def step2(feedback=None):
    feedback.add_notice('Hello!')
    time.sleep(1)


@feedback('Step 3')
def step3(feedback=None):
    # substep(parent_feedback=feedback)
    time.sleep(1)


@feedback('Substep')
def substep(feedback=None):
    time.sleep(1)


if __name__ == '__main__':
    renderer = Renderer(max_width=80)
    with feedback(app_name='Example', version='v0.0.0', renderer=renderer) as fb:
        time.sleep(1)  # initialisation line
        toplevel(feedback=fb)

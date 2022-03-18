import pprint

import kfp.compiler
import kfp.dsl as dsl
from kfp.components import create_component_from_func

from robotScoreAggregator import aggregate_scores
from yearProcessor import grab_event_keys_for_year
from matchProcessor import grab_matches_for_events

from google.cloud import storage

client = storage.Client.from_service_account_json('theta-byte-342416-3bb0f4e92c48.json')

kubeflow_storage_bucket = client.get_bucket('theta-byte-342416-kubeflowpipelines-default')

event_op = create_component_from_func(grab_event_keys_for_year, packages_to_install=['google-cloud-storage',
                                                                                     'requests',
                                                                                     'datetime'])
matches_op = create_component_from_func(grab_matches_for_events, packages_to_install=['google-cloud-storage',
                                                                                      'google-api-core',
                                                                                      'requests',
                                                                                      'datetime'])
robot_score_op = create_component_from_func(aggregate_scores, packages_to_install=['google-cloud-storage',
                                                                                   'datetime',
                                                                                   'pandas',
                                                                                   'ast'])


@dsl.pipeline(
    name='The Blue Alliance Preprocessing'

)
def pipeline(years: str):
    get_event_keys_task = event_op(years=years)
    get_matches_task = matches_op(get_event_keys_task.output)
    robot_score_task_2017 = robot_score_op('2017', get_matches_task.output)
    robot_score_task_2018 = robot_score_op('2018', get_matches_task.output)
    robot_score_task_2019 = robot_score_op('2019', get_matches_task.output)


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(pipeline_func=pipeline, package_path='tba_preprocessing.yaml')
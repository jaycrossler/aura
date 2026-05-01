from pathlib import Path

import yaml


def test_build_viewer_workflow_yaml_is_valid():
    workflow = Path('.github/workflows/build-viewer.yml')
    data = yaml.safe_load(workflow.read_text(encoding='utf-8'))
    assert isinstance(data, dict)
    steps = data['jobs']['build']['steps']
    assert any(step.get('uses') == 'actions/upload-artifact@v4' for step in steps if isinstance(step, dict))


def test_all_workflow_files_parse_as_yaml():
    for workflow in Path('.github/workflows').glob('*.yml'):
        yaml.safe_load(workflow.read_text(encoding='utf-8'))

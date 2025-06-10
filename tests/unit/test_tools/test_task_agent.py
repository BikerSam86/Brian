from tsal.tools import task_agent
import subprocess
import yaml
import pytest


def test_run_known_task(tmp_path, monkeypatch):
    tasks = {"tasks": {"repair": "echo repaired"}}
    task_file = tmp_path / "tasks.yaml"
    task_file.write_text(yaml.safe_dump(tasks))

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(task_agent, "TASKS_FILE", task_file)
    monkeypatch.setattr(task_agent, "LOG_FILE", tmp_path / "log.txt")

    calls = []

    def fake_run(cmd, shell, check=False, stdout=None, stderr=None):
        calls.append(cmd)

    monkeypatch.setattr(subprocess, "run", fake_run)
    task_agent.run_task("repair")
    assert calls == ["echo repaired"]
    assert task_agent.LOG_FILE.read_text().startswith("$ echo repaired")


def test_unknown_task(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(task_agent, "TASKS_FILE", tmp_path / "missing.yaml")
    with pytest.raises(SystemExit):
        task_agent.run_task("nope")

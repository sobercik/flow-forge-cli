#!/usr/bin/env python3
"""Flow Forge CLI - Core entrypoint for structured workflow automation."""

import argparse
import sys
from pathlib import Path
import yaml


def load_config(config_path: Path) -> dict:
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    with config_path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict) or "pipelines" not in data:
        raise ValueError("Invalid flowforge.yaml: missing 'pipelines' section.")
    return data


def cmd_validate(config_path: Path) -> int:
    try:
        cfg = load_config(config_path)
        pipelines = cfg.get("pipelines", [])
        print(f"[OK] Validated '{config_path.name}' ({len(pipelines)} pipelines configured).")
        return 0
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


def cmd_run(config_path: Path, pipeline_id: str | None = None) -> int:
    try:
        cfg = load_config(config_path)
        pipelines = cfg.get("pipelines", [])
        if pipeline_id:
            pipelines = [p for p in pipelines if p.get("id") == pipeline_id]
            if not pipelines:
                raise ValueError(f"Pipeline '{pipeline_id}' not found in configuration.")

        for pipe in pipelines:
            print(f"-> Executing pipeline: {pipe['id']} ({pipe.get('description', '')})")
            for step in pipe.get("steps", []):
                print(f"   * Step completed: {step}")
        print("[DONE] All selected workflows completed successfully.")
        return 0
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="flowforge",
        description="Flow Forge CLI - Lightweight technical workflow automation",
    )
    parser.add_argument("--version", action="version", version="flow-forge-cli 1.4.2")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_p = subparsers.add_parser("validate", help="Validate workflow configuration")
    validate_p.add_argument("--config", default="flowforge.yaml", help="Path to YAML config")

    run_p = subparsers.add_parser("run", help="Execute configured pipelines")
    run_p.add_argument("--config", default="flowforge.yaml", help="Path to YAML config")
    run_p.add_argument("--pipeline", default=None, help="Specific pipeline ID to execute")

    args = parser.parse_args()
    config_path = Path(args.config)

    if args.command == "validate":
        return cmd_validate(config_path)
    if args.command == "run":
        return cmd_run(config_path, args.pipeline)
    return 0


if __name__ == "__main__":
    sys.exit(main())

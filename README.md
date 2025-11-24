# Espanso configuration and scripts

This repository contains my personal Espanso configuration and the small helper scripts used by it.

Espanso is a text expander for Linux, macOS and Windows. This repo stores the configuration files that define matches and replacements, and a few scripts used by the configuration.

## Repository structure

- `config/`
	- `default.yml` — main Espanso config file.
	- `match/` — folder containing individual match files used by Espanso:
		- `atl.yml`, `base.yml`, `timestamp.yml`, and `packages/` (additional packaged snippets)

- `python-scripts/`
	- `discord-timestamp.py` — helper script referenced by the config (see notes below).
	- `pyproject.toml` — Python project metadata for the scripts.

- `README.md` — this file.

## Quick start

1. Install Espanso following the official instructions for your OS: https://espanso.org/

2. Install or copy this configuration into your Espanso config directory. By default Espanso uses `~/.config/espanso` on Linux.

	 - To use the configuration directly, clone or copy these files into `~/.config/espanso`.
	 - Alternatively, keep the repo elsewhere and create a symlink from `~/.config/espanso` to this folder.

Note: If you intend to run the Python helper scripts in `python-scripts/`, create a virtual environment inside that directory first. For example, from the repository root:

```bash
cd python-scripts
uv venv   # create a venv using your 'uv' helper
uv sync   # optional: install/sync dependencies into the venv
```

You can also use standard tools instead of `uv`, e.g. `python3 -m venv .venv` and `pip install -r requirements.txt`.

3. (Optional) Restart Espanso only if needed — Espanso typically hot-reloads when it detects configuration changes.

If you prefer to restart manually, you can run:

```bash
# Linux example
espanso restart
```

If you don't have `espanso` in your PATH, follow your distribution or install instructions and ensure the service/daemon is running.

## Scripts

The `python-scripts/` directory contains helper scripts used by the match files. For example, `discord-timestamp.py` is intended to generate or format timestamps for use inside certain snippets.

Run the scripts with Python 3.8+ (adjust the interpreter according to your environment):

```bash
python3 python-scripts/discord-timestamp.py
```

If you plan to run the scripts frequently it is recommended to create a virtual environment and install any dependencies defined in `pyproject.toml`.

## Customizing

- Edit YAML files under `config/` and `config/match/` to add or change matches.
- If you change scripts in `python-scripts/`, ensure any match entries that call them still point to the correct path.

Notes:
- Paths in Espanso config are relative to the Espanso config directory. If you place this repository elsewhere, either update paths or use a symlink so Espanso sees the same layout.

## Contributing

This is a personal configuration but contributions and suggestions are welcome. If you make improvements, please open an issue or pull request describing the change.

## License

No license is specified. If you want to reuse these files, please get permission or add a license to this repository.

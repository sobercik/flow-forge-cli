# Flow Forge CLI ⚡

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI - Installation](https://img.shields.io/badge/install-pip-3776AB.svg?logo=python&logoColor=white)]()
[![Node.js Support](https://img.shields.io/badge/Node.js-18%2B-339933.svg?logo=node.js&logoColor=white)]()
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Version](https://img.shields.io/badge/version-1.4.2-orange.svg)]()

**Flow Forge CLI** is a lightweight, cross-platform command-line tool and automation library built to streamline technical workflow generation and structured data processing—tailored specifically for modern **Node.js** projects without heavy proprietary dependencies.

Designed for JavaScript/TypeScript developers, DevOps engineers, and technical teams, Flow Forge CLI eliminates repetitive formatting, scaffolding, and JSON/YAML schema transformation tasks through fast, scriptable pipelines.

---

## ✨ Key Features

- **Python-Powered Speed, Node.js Native Workflow:** Installed globally via `pip` for zero-bloat execution, while integrating directly into your `package.json` scripts and Node.js build pipelines.
- **Declarative Pipelines:** Define complex data transformations, API payload validations, and code scaffolding using clean YAML or JSON configurations.
- **Extensible Plugin Architecture:** Easily hook custom Node.js scripts or JavaScript modules into your execution lifecycle.
- **CI/CD Ready:** Built-in exit codes, structured JSON logging, and silent modes tailored for automated GitHub Actions and Node.js deployment environments.
- **Strict Schema Validation:** Built-in type checking and structural validation before generating TypeScript definitions, documentation, or config files.

---

## 🚀 Quick Start

### Installation

Install **Flow Forge CLI** globally using `pip` as the primary package manager:

```bash
pip install flow-forge-cli
```

Verify the installation:

```bash
flow-forge --version
```

### Basic CLI Usage

Initialize a new workflow configuration inside your Node.js project root:

```bash
flow-forge init --template node
```

Run a transformation pipeline against your target directory:

```bash
flow-forge run --config ./flowforge.yaml --input ./src/schemas --output ./dist
```

---

## 📦 Node.js Integration

You can integrate **Flow Forge CLI** directly into your `package.json` lifecycle scripts or invoke it programmatically from Node.js:

### 1. `package.json` Scripts

```json
{
  "name": "my-node-service",
  "version": "1.0.0",
  "scripts": {
    "prebuild": "flow-forge run --config ./flowforge.yaml",
    "validate:schemas": "flow-forge validate --strict ./schemas/*.json",
    "docs:generate": "flow-forge run --pipeline docs-builder"
  }
}
```

### 2. Programmatic Execution in Node.js (ESM)

```javascript
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

const execFileAsync = promisify(execFile);

async function runForgePipeline() {
  try {
    const { stdout } = await execFileAsync('flow-forge', [
      'run',
      '--config',
      './flowforge.yaml',
      '--format',
      'json'
    ]);
    const result = JSON.parse(stdout);
    console.log('Pipeline completed successfully:', result.summary);
  } catch (error) {
    console.error('Flow Forge pipeline failed:', error.stderr || error.message);
    process.exit(1);
  }
}

runForgePipeline();
```

---

## 🛠️ Configuration Example

Create a `flowforge.yaml` file in your repository root to automate repetitive Node.js structuring and validation tasks:

```yaml
version: "1.4"
pipeline:
  name: "node-structured-docs-builder"
  target_runtime: "nodejs"
  strict_validation: true

steps:
  - id: parse-schemas
    action: transform
    format: json-to-markdown
    source: "./src/schemas/*.json"

  - id: lint-output
    action: validate
    rules:
      - no-empty-fields
      - enforce-utf8
      - valid-json-schema

  - id: export
    action: write
    destination: "./docs/api/"
```

---

## 🗺️ Roadmap (v2.0)

We are actively working on our next major release focused on performance improvements and plugin extensibility:

- [x] Core CLI engine (`pip` distribution) and YAML/JSON parser
- [x] Native Node.js `package.json` and ESM workflow templates
- [ ] **In Progress:** Asynchronous worker pool for high-volume batch processing
- [ ] **In Progress:** Official Plugin SDK supporting custom Node.js middleware hooks
- [ ] Interactive terminal UI (TUI) for live pipeline debugging

---

## 🤝 Contributing

Contributions are what make the open-source community thrive. Whether you are fixing bugs, improving documentation, or proposing new features, your help is appreciated!

1. Fork the repository.
2. Create your feature branch (`git checkout -b feat/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feat/amazing-feature`).
5. Open a Pull Request.

Please make sure to run the Node.js test suite before submitting a PR:

```bash
npm install
npm test
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

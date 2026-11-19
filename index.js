import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { resolve } from 'node:path';

const execFileAsync = promisify(execFile);

/**
 * Executes a Flow Forge CLI pipeline from Node.js.
 * @param {Object} options
 * @param {string} [options.configPath='flowforge.yaml'] - Path to configuration file.
 * @param {string} [options.pipeline] - Specific pipeline ID to run.
 * @returns {Promise<{ stdout: string, stderr: string }>}
 */
export async function runPipeline({ configPath = 'flowforge.yaml', pipeline } = {}) {
  const args = ['run', '--config', resolve(configPath)];
  if (pipeline) {
    args.push('--pipeline', pipeline);
  }

  try {
    return await execFileAsync('flowforge', args);
  } catch (error) {
    throw new Error(`Flow Forge execution failed: ${error.message}`);
  }
}

/**
 * Validates the local flowforge.yaml configuration file.
 * @param {string} [configPath='flowforge.yaml']
 * @returns {Promise<boolean>}
 */
export async function validateConfig(configPath = 'flowforge.yaml') {
  try {
    await execFileAsync('flowforge', ['validate', '--config', resolve(configPath)]);
    return true;
  } catch {
    return false;
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const isValid = await validateConfig();
  console.log(isValid ? 'Flow Forge configuration verified.' : 'Invalid configuration.');
}

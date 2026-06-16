/**
 * test-utils.js — Basic custom test framework assertions
 */

const suites = [];
let currentSuite = null;

export function describe(name, fn) {
  currentSuite = { name, tests: [] };
  suites.push(currentSuite);
  fn();
  currentSuite = null;
}

export function it(name, fn) {
  if (currentSuite) {
    currentSuite.tests.push({ name, fn });
  }
}

export function expect(actual) {
  return {
    toBe(expected, message = '') {
      if (actual !== expected) {
        throw new Error(message || `Expected ${actual} to be ${expected}`);
      }
    },
    toBeCloseTo(expected, precision = 2, message = '') {
      const diff = Math.abs(actual - expected);
      const limit = Math.pow(10, -precision) / 2;
      if (diff > limit) {
        throw new Error(message || `Expected ${actual} to be close to ${expected} (diff: ${diff}, limit: ${limit})`);
      }
    },
    toBeGreaterThan(expected, message = '') {
      if (actual <= expected) {
        throw new Error(message || `Expected ${actual} to be greater than ${expected}`);
      }
    },
    toBeLessThan(expected, message = '') {
      if (actual >= expected) {
        throw new Error(message || `Expected ${actual} to be less than ${expected}`);
      }
    },
    toBeTruthy(message = '') {
      if (!actual) {
        throw new Error(message || `Expected ${actual} to be truthy`);
      }
    }
  };
}

export async function runTests() {
  const results = [];
  for (const suite of suites) {
    const suiteResult = { name: suite.name, tests: [] };
    for (const test of suite.tests) {
      try {
        await test.fn();
        suiteResult.tests.push({ name: test.name, passed: true });
      } catch (e) {
        suiteResult.tests.push({ name: test.name, passed: false, error: e.message });
      }
    }
    results.push(suiteResult);
  }
  return results;
}

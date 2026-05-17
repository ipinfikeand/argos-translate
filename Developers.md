# Developers
Most active development happens in the `v2` branch, please make pull requests there

## Running unit tests
```
pytest tests
```

## Running a specific test file
```
pytest tests/test_translate.py -v
```

## Running tests with verbose output and stopping on first failure
```
pytest tests -v -x
```

## Formatting
The unit tests in the master branch are deprecated but improved unit tests are being developed in the "v2" branch.
```
./scripts/format.sh
```

## Notes (personal)
- Remember to activate the virtualenv before running tests: `source venv/bin/activate`
- Language packages are downloaded to `~/.local/share/argos-translate/packages` by default
- To list installed packages from Python: `argostranslate.package.get_installed_packages()`
- Useful for debugging: set `ARGOS_TRANSLATE_VERBOSE=1` env var to get more logging output

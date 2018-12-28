# Basic Python Windows + Linux example

This example uses nose2 as the test runner with the junit XML plugin. This is passed to Azure pipelines so the test output is cleanly parsed.

Also, this example assumes:
- Python 3.6 and 3.7 (change Matrix for Linux + Windows to alter)
- Your tests are in a directory called "tests" (change the nose2 line to alter)

```yaml
trigger:
- master

jobs:

- job: 'Test_Linux'
  pool:
    vmImage: 'Ubuntu-16.04'
  strategy:
    matrix:
      Python36:
        python.version: '3.6'
      Python37:
        python.version: '3.7'
    maxParallel: 2

  steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '$(python.version)'
      architecture: 'x64'

  - script: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
    displayName: 'Install dependencies'

  - script: |
      pip install nose2
      nose2 --plugin nose2.plugins.junitxml --junit-xml tests
    displayName: 'Run tests'

  - task: PublishTestResults@2
    inputs:
      testResultsFiles: '**/nose2-junit.xml'
      testRunTitle: 'Python $(python.version)'
    condition: succeededOrFailed()

- job: 'Test_Windows'
  pool:
    vmImage: 'vs2017-win2016'
  strategy:
    matrix:
      Python36:
        python.version: '3.6'
      Python37:
        python.version: '3.7'
    maxParallel: 2

  steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '$(python.version)'
      architecture: 'x64'

  - script: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
    displayName: 'Install dependencies'

  - script: |
      pip install nose2
      nose2 --plugin nose2.plugins.junitxml --junit-xml tests
    displayName: 'Run tests'

  - task: PublishTestResults@2
    inputs:
      testResultsFiles: '**\nose2-junit.xml'
      testRunTitle: 'Python $(python.version)'
    condition: succeededOrFailed()

```

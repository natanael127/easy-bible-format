# Easy Bible Format (EBF)
Version 1.x.y

## Introduction
- **TODO:** why a new format
- **TODO:** why over JSON and not XML
- **TODO:** other formats that this one will be based on

## Versioning
This specification will be versioned according to [semantic versioning](https://semver.org/).

On the header of this document will be displayed the major number associated with the current text.

Only git-tagged versions of the specification are in compliance to semantic version, intermediate commits are not necessarily in compliance too.

## Extension
The suggested extension of file is `.ebx.json`, where x is the major number of the file format.

Example for major 1:
```
bible.ebf1.json
```

## Schema
The JSON schema is stored in this repository within documentation.

To validate your EBF data against the JSON schema:

```
npm install -g ajv-cli
ajv validate -s ebf1-schema.json -d <your-ebf-file.json>
```

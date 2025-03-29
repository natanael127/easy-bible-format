# Easy Bible Format (EBF)
Version 1.x.y

## Introduction
This document specifies the Easy Bible Format (EBF), a new, modern, and developer-friendly format for representing biblical texts. EBF aims to simplify the parsing and manipulation of scripture data by leveraging the widely adopted JSON (JavaScript Object Notation) format.

## Base formats
- **SWORD:** The SWORD Project is a cross-platform Bible software API and toolset. It uses a proprietary file format that, while powerful, can be complex to parse and integrate into modern web and mobile applications.
- **USFM (Unified Scripture Format Markers):** USFM is a markup language designed for representing scripture texts, primarily used in Bible translation projects. It employs a system of markers to denote structural elements like verses, chapters, and paragraphs. While robust, USFM's marker-based syntax can be challenging for developers unfamiliar with it.
- **USFX (Unified Scripture Format XML):** USFX is an XML-based representation of USFM. It aims to provide a more structured and standardized format. However, XML can be verbose and less efficient to parse compared to JSON, particularly in web environments.

## Why a new format?
Why JSON?
- **Simplicity and Readability:** JSON's syntax is significantly simpler and more readable than XML, making it easier for developers to understand and work with. This reduces the learning curve and development time.
- **Lightweight and Efficient:** JSON is a lightweight data-interchange format, resulting in smaller file sizes and faster parsing times, which is especially crucial for web and mobile applications where performance is critical.
- **Native Support in JavaScript:** JSON is natively supported in JavaScript, the language of the web. This seamless integration simplifies data handling in web-based Bible applications.
- **Widespread Adoption:** JSON is a widely adopted standard in modern web development, with excellent support in various programming languages and frameworks. This ensures broad compatibility and ease of integration.
- **Flexibility:** JSON's flexible structure allows for the easy representation of complex data structures, including nested elements and arrays, which are essential for accurately representing biblical texts.
- **Parsing Efficiency:** JSON parsers are generally faster and less resource-intensive than XML parsers.

EBF aims to address the limitations of existing formats by providing a more accessible, efficient, and developer-friendly alternative. By leveraging JSON, EBF simplifies the process of building Bible applications and promotes wider access to scripture data.

## Versioning
This specification will be versioned according to [semantic versioning](https://semver.org/).

The header of this document will display the major version number associated with the current text.

Only git-tagged versions of the specification are in compliance with semantic versioning; intermediate commits are not necessarily compliant.

## Extension
The suggested file extension is `.ebfx.json`, where 'x' represents the major version number of the file format.

Example for major version 1:
```
bible.ebf1.json
```

## Schema
The JSON schema is stored in this repository within the documentation directory.

To validate your EBF data against the JSON schema:

```
npm install -g ajv-cli
ajv validate -s ebf1-schema.json -d <your-ebf-file.json>
```

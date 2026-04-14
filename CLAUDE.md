# Goal

This is a repository designed to support tutorials where students need to do live coding with the instructor (and some practice coding from home) to write a number of test cases. These tests should be for unit tests and integration tests and should cover concepts like assert, parameterisation, and different forms of mocking at increased levels of complexity.

# Structure

We will use the docs folder to store our design of this repository as well as the instructions for the students. The source folder is where all of the source code will go that the students will be tested. The test folder is where all the tests will go and the test folder should have sub folder for solutions (`_solutions`) so that we separate the completed tests from the tests the students will be working on.

# Concept Tutorials Structure

Each "concept tutorial" will be a single markdown file in the docs that touches on a single high-level concept, such as Fixtures in Unit Tests, or Patching in Integration Tests. For each tutorial, we should have 3+ examples, where the first example is the simplest form of example possible for that high-level example. Then, the following examples (at least 3, in total) need to have increasing complexity to challenge the students' understanding of the concept. Where possible, avoid combining high-level concepts in the tutorials (e.g., try to avoid the need for Fixtures when creating a tutorial for Patching).

Each content tutorial will be named as `XX Name_Of_Test_Type - Test_Concept.md`.

# Challenge Tutorials Structure

TBD

# Test Example Creation Instructions

Everytime we add a new test example, you need to do the following:

- Add a src file with the accompanying code to test
- Add a test solution under the correct category under `test/_solutions`
- Update the `docs/00 Tutorial Design.md` file to account for this new example
- Create/Update the appropriate tutorial file

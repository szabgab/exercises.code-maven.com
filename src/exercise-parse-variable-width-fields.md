# Parse variable width fields


<slidecast file="beginner-perl/exercise-parse-variable-width-fields" youtube="6NoHj4sehWc" />

In this log file I got from some company, there are rows in which the first 16 and last 16 characters
describe some kind of an addresses while everything in between describes several commands.

Each command is built up by a leading character (A, B, C, D, etc) and a number
of digits. The number of digits depend on the leading character.

In this exercise we need to split up the data to commands and count how many times
each command type was given.

```ruby
{{#include examples/data/variable_width_fields.log }}
```

## Tools
* 

## Solutions
* [Perl 5: parse variablew width fields](https://perlmaven.com/beginner-perl-maven-solution-parse-variable-width-fields)


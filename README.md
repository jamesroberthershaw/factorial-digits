# Factorial-digits

The program contained in this repository's function is to first calculate the factorial of a given number, then to calculate the sum of the individual digits of that factorial and output the result.

This repository contains a Docker build directory with everything needed to build a docker with this functionality.

To use the program simply start a terminal session, clone the repository using the following command

```sh
git clone https://github.com/jamesroberthershaw/factorial-digits.git
```
then navigate into the direcrory
```sh
cd factorial-digits/
```
and run the following command

```sh
docker run --rm factorial-digits <value>
```
Where value is the number that you wish to know the sum of the factorial digits of. 



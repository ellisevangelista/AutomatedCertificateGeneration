# Automated Certificate Generation
A Python application for automating the generation of any certificate (image format) without being prompted for values.

## Getting Started 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Programming language you need to install:
* [Python](https://www.python.org/downloads/)

Libraries you need to install:
* PIL
```
python -m pip install Pillow
```

## Deployment
After you install the latest Python and the required libraries, you can now open and run the file using Python IDLE which is installed by default upon installation of Python using the installation packages available from the Python website.

### Additional Note
* The certificate should be in an image format.
* Put your certificate image in the same directory as where the generateCertificates.py file is.
* The input of this application is a .csv file format.

### Sample Input (.csv file)  
```
"De la Cruz, Juan P.",GitHub Inc.,March 26, 2018
"Smith, John A.",GitHub Inc.,March 27, 2018
```
### Sample Output 
Sample output is found inside the *generated* folder.

## Authors
* **Ellis Evangelista** -- [ellisevangelista](https://github.com/ellisevangelista)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

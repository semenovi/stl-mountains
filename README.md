# Mountains STL

## Program Description

This program generates a 3D projection of a hypercube (tesseract) as well as a mountainous landscape and saves it in an STL file format. The tesseract is generated as a set of vertices and faces using the numpy library, while the landscape is generated as a set of random points with a height map added to it, triangulated using the Delaunay function from the scipy library, and converted to facets. The facets are then written to an STL file format using a custom function.

## Usage

1. Install python and the required libraries (`numpy`, `scipy`).

2. Run the `generate_stl.py` script in the command line using Python:

   ```
   python generate_stl.py
   ```

3. The script will generate a file called `tesseract_landscape.stl` in the same directory, which can be imported into a 3D modeling software or a 3D printer software.

## Customization

To customize the tesseract or the landscape, you can modify the `generate_tesseract()` and `generate_landscape()` functions in the `generate_stl.py` script respectively. You can also modify the parameters of each function to obtain different forms and shapes.

## Requirements

* Python 3.0 or higher
* NumPy
* SciPy

## Acknowledgments

This program is inspired by similar programs found online, and makes use of the NumPy and SciPy libraries to generate the tesseract and the landscape.

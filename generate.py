import numpy as np

def generate_tesseract():
    # Generate vertices of a tesseract
    vertices = np.array([
        [0,0,0,0],
        [0,0,1,0],
        [0,1,0,0],
        [0,1,1,0],
        [1,0,0,0],
        [1,0,1,0],
        [1,1,0,0],
        [1,1,1,0],
        [0,0,0,1],
        [0,0,1,1],
        [0,1,0,1],
        [0,1,1,1],
        [1,0,0,1],
        [1,0,1,1],
        [1,1,0,1],
        [1,1,1,1]
    ])

    # Generate faces of a tesseract
    faces = np.array([
        [0,1,3,2],
        [4,5,7,6],
        [0,4,6,2],
        [1,5,7,3],
        [0,4,5,1],
        [2,6,7,3],
        [8,9,11,10],
        [12,13,15,14],
        [8,12,14,10],
        [9,13,15,11],
        [8,12,13,9],
        [10,14,15,11],
        [0,8,9,1],
        [2,10,11,3],
        [4,12,13,5],
        [6,14,15,7],
        [0,8,12,4],
        [1,9,13,5],
        [3,11,15,7],
        [2,10,14,6]
    ])

    # Rescale vertices to fit in a sphere with radius 1
    r = np.sqrt(4)
    vertices = vertices / r
    faces = faces[:, :-1]
    vertices = vertices[:, :-1]
    # Generate facets from faces
    print('FACES')
    print(len(faces[0]))
    print(len(faces[1]))
    print(len(faces[2]))
    print('VERTICES')
    print(len(vertices[0]))
    print(len(vertices[1]))
    print(len(vertices[2]))

    print(faces.shape)
    print(vertices.shape)

    facets = []
    for face in faces:
        normal = np.cross(vertices[face[1]] - vertices[face[0]], vertices[face[2]] - vertices[face[0]], )
        normal = normal / np.sqrt(np.sum(normal**2))
        for i in range(2, len(face)):
            facets.append(np.concatenate((normal, vertices[face[i-2]], vertices[face[i-1]], vertices[face[i]])))

    return np.concatenate(facets).reshape(-1, 12)

def generate_landscape(x_range=(-1,1), y_range=(-1,1), z_range=(-1,1), num_points=1000):
    # Generate random points within the given range
    points = np.random.uniform(x_range[0], x_range[1], (num_points, 3))

    # Apply a height map to the points
    h = np.sin(points[:, 0]*5) + np.sin(points[:, 1]*5) + np.sin(points[:, 2]*5)
    points[:, 2] = points[:, 2] + h

    # Triangulate the points to create a mesh
    from scipy.spatial import Delaunay
    tri = Delaunay(points)
    simplices = tri.simplices

    # Generate facets from the triangles
    facets = []
    for face in simplices:
        normal = np.cross(points[face[1]][:3] - points[face[0]][:3], points[face[2]][:3] - points[face[0]][:3])
        normal = normal / np.sqrt(np.sum(normal**2))
        facets.append(np.concatenate((normal, points[face[0]], points[face[1]], points[face[2]])))


    return np.concatenate(facets).reshape(-1, 12)

def write_stl_file(filename, facets):
    # Convert facets to binary STL format
    nfacets = len(facets)
    header = np.zeros(80, dtype=np.uint8)
    np.array([nfacets], dtype=np.uint32).tofile(filename)
    np.concatenate([facets.reshape(-1) for facets in facets]).astype('float32').tofile(filename)

# Generate tesseract and landscape facets
tesseract_facets = generate_tesseract()
landscape_facets = generate_landscape(x_range=(-1,1), y_range=(-1,1), z_range=(-0.5,1), num_points=10000)

# Combine tesseract and landscape facets
facets = np.concatenate([tesseract_facets, landscape_facets], axis=0)

# Write facets to an STL file
write_stl_file('tesseract_landscape.stl', facets)

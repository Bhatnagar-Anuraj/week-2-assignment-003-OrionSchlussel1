"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================
OBJECTIVE:
    Use loops and conditionals to generate a repeating pattern of 3D objects
    in Maya. You will practice nested loops, conditional logic, and
    mathematical positioning.
REQUIREMENTS:
    1. Use a nested loop (a loop inside a loop) to create a grid or pattern
       of objects.
    2. Include at least one conditional (if/elif/else) that changes an
       object's properties (type, size, color, or position offset) based
       on its row, column, or index.
    3. Generate at least 25 objects total (e.g., a 5x5 grid).
    4. Comment every major block of code explaining your logic.
GRADING CRITERIA:
    - [25%] Nested loop correctly generates a grid/pattern of objects.
    - [25%] Conditional logic visibly changes object properties based on
            position or index.
    - [20%] At least 25 objects are generated.
    - [15%] Code is well-commented with clear explanations.
    - [15%] Pattern is visually interesting and intentional.
TIPS:
    - A 5x5 grid gives you 25 objects. A 6x6 grid gives you 36.
    - Use the loop variables (row, col) to calculate X and Z positions.
    - The modulo operator (%) is great for alternating patterns:
          if col % 2 == 0:    # every other column
    - You can vary: primitive type, height, width, position offset, etc.
COMMENT HABITS (practice these throughout the course):
    - Add a comment before each logical section explaining its purpose.
    - Use inline comments sparingly and only when the code is not obvious.
    - Keep comments up to date -- if you change the code, update the comment.
"""
import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)





def generate_pattern():
    """Generate a procedural pattern of objects using nested loops.
    This function should:
        1. Define variables for rows, columns, and spacing.
        2. Use a nested for-loop to iterate over rows and columns.
        3. Inside the loop, use a conditional to vary object properties.
        4. Create and position each object.
    """
    # --- Configuration variables ---
    num_rows = 6        # Number of rows in the pattern.
    num_cols = 6        # Number of columns in the pattern.
    spacing = 3.0       # Distance between object centers.



    # TODO: Create a nested loop that iterates over rows and columns.
    #
    # HINT -- your loop structure should look something like this:
    #
    #   for row in range(num_rows):
    #       for col in range(num_cols):
    #           # Calculate position
    #           x_pos = col * spacing
    #           z_pos = row * spacing
    #
    #           # TODO: Add a conditional here that changes something
    #           # based on row, col, or (row + col).
    #           # For example:
    #           #   if (row + col) % 2 == 0:
    #           #       create a cube
    #           #   else:
    #           #       create a sphere
    #
    #           # TODO: Create the object using cmds.polyCube(), etc.
    #
    #           # TODO: Position the object using cmds.move().
    #
    #           # TODO: (Optional) Vary the scale using cmds.scale().


    #This nested loop will allow me to place my objects in certain rows and colums. This code will make sure that no onjects are created on the same row or colum. 
    for row in range(num_rows):
        for col in range(num_cols):

            x_pos = col * spacing
            z_pos = row * spacing

        
            #This code will name each object by its row and colum,so it will be easier for me to find any object.
            object_name = f"object_{row}_{col}"



            #The why for this code is, so I can create either a cube or a sphere in a checker pattern depending on the row and colum. 
            if (row + col) % 2 == 0:
            
                #The why for this code, is so with each pass over the cube's height will grow. I need this so the cubes will change will each pass over. This will also inturn give me a stair like diagonal pattern. This will also put the cube in the correect position.
                cube_height = 1.0 + row * 0.8
                cmds.polyCube(name=object_name, width=1.5, height=cube_height, depth=1.5)
                cmds.move(x_pos, cube_height / 2.0, z_pos, object_name)

            
            else:
           
                #The why for this code, is so with each pass over the sphere's height will grow. I need this so the spheres will change will each pass over. This will also inturn give me a stair like diagonal pattern.This will also put the sphere in the correct position.
                sphere_radius = 0.4 + col * 0.1
                cmds.polySphere(name=object_name, radius=sphere_radius)
                cmds.move(x_pos, sphere_radius, z_pos, object_name)

    #I have this code here to print out how many objects and have big the grid is. This is very helpful for me when writing and testing because I can see if I accidently created too many objects or messed of the grid. 
    total_objects = num_rows * num_cols
    print(f"Generated {total_objects} objects in a {num_rows}x{num_cols} grid.")

# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
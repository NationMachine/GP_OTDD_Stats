from scipy.io import loadmat
import graphviz
import glob
import os
import re

import pandas as pd
import numpy as np

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]
# Class to define treeNode
class treeNode:
    def __init__(self, treeNode):
        self.op = treeNode
        self.ID = None
        self.children = []

    # Methods to fill TreeNode's attributes    
    def add_children(self, children):
        self.children.append(children)
        
    def add_ID(self, ID):
        self.ID = ID

# Function to create an individual node
def create_node(data):
    
    # Create a treeNode object
    node = treeNode(data['op'].item().item())
    node.add_ID(data['nodeid'].item().item())
    
    return node

# Function to add children to nodes
def add_more_kids(parent_node, data):
    
    # Verify if the node has children
    if data['kids'].item().size > 0:
        for more___kids in data['kids'].item():
            for child_data in more___kids:
                child_node = create_node(child_data)
                parent_node.add_children(child_node)
                add_more_kids(child_node, child_data)

# Function to generate the nodes from .mat file
def get_TreeNodes(mat_contents):
    
    if 'arbol' in mat_contents:
        data = mat_contents['arbol']
        # Adding root node
        node = create_node(data)
        # Add kids to the tree
        ekids = data['kids'].item()
        for more_kids in ekids:
            for more__kids in more_kids:
                current_node = create_node(more__kids)
                node.add_children(current_node)
                # Recursively add children nodes
                add_more_kids(current_node, more__kids)               
    else:
        print("Structure 'arbol' not found in the MATLAB file.")

    return node

# Print using GraphViz .dot file
# Generate a dot file containing the Tree information
# The basic representation is considered as follows: "NodeOperationName_nodeID"
def generate_dot_file(node, filename):
    
    with open(filename, "w") as dot_file:
        # Basic Structure of a .dot file
        dot_file.write("digraph tree_Structure {\n")
        dot_file.write("\tgraph [fontname = \"AvantGarde-Book\"];\n")
        dot_file.write("\tnode [fontname = \"AvantGarde-Book\"];\n")
        dot_file.write("\tedge [fontname = \"AvantGarde-Book\"];\n")
        # Write the Root node 
        dot_file.write(f"\t\"{node.op}_{node.ID}\" [shape = circle, color = \"#D37676\", style = filled];\n")       
        # Change color of the children
        dot_file.write("\tnode [shape = circle, color = \"#EBC49F\", style = filled];\n")
        # Add and Connect all the kids
        connect_children(node, dot_file)
        # Add Label to the graph (the default is centered bottom)
        dot_file.write("}")
        
# Connect Nodes
def connect_children(node, dot_file):
    
    for child in node.children:
        dot_file.write(f"\t\"{node.op}_{node.ID}\" -> \"{child.op}_{child.ID}\" [color = \"#3C3633\"];\n")
        connect_children(child, dot_file)
        
def generate_svg(dot_file_path, svg_file_path):
    graph = graphviz.Source.from_file(dot_file_path)
    graph.format = 'svg'
    graph.render(svg_file_path)

def generate_pdf(dot_file_path, pdf_file_path):
    graph = graphviz.Source.from_file(dot_file_path)
    graph.format = 'pdf'
    graph.render(pdf_file_path)

def generate_png(dot_file_path, pdf_file_path):
    graph = graphviz.Source.from_file(dot_file_path)
    graph.format = 'png'
    graph.render(pdf_file_path)
    
# Load the MATLAB file
archivos_en_directorio_mat = glob.glob(os.getcwd() + "//clas_mats//*.mat")
archivos_en_directorio_csv = glob.glob(os.getcwd() + "//*.csv")
archivos_en_directorio_mat.sort(key=natural_keys)
archivos_en_directorio_csv.sort(key=natural_keys)
csv_df = pd.read_csv(archivos_en_directorio_csv[1])

for p,c in enumerate(archivos_en_directorio_mat):
    
    mat_contents = loadmat(archivos_en_directorio_mat[p])
    base = csv_df['OG'][p]
    nombre = csv_df["Problema"][p]
    # Get the information from the .mat file
    folder = os.getcwd() +'\\'+ nombre     
    isdir = os.path.isdir(folder)
        
    if isdir== False:  
        problema_folder = os.mkdir(folder)
    problema_folder = folder
    treeNodes = get_TreeNodes(mat_contents)
    
    # Generate a GraphViz .dot file to visualization 
    arbol_dot = base + '.dot'
    generate_dot_file(treeNodes, problema_folder + '/' + arbol_dot)

    # Generate output .svg and .pdf files   
    output = os.getcwd()   
    dot_file_path = problema_folder + '/' + arbol_dot   
    pdf_file_path = problema_folder + '/' + arbol_dot
    generate_pdf(dot_file_path, pdf_file_path)

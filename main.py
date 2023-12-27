from flask import Flask, send_file
import pygraphviz as pgv
import io
import os

app = Flask(__name__)

@app.route('/')
def generate_mind_map():
    # Create a new graph
    graph = pgv.AGraph(strict=False, directed=True)

    # Add nodes and edges (customize as needed)
    graph.add_node("Root")
    graph.add_node("Node A")
    graph.add_node("Node B")
    graph.add_edge("Root", "Node A")
    graph.add_edge("Root", "Node B")

    # Generate a PNG image from the graph
    img = graph.draw(format='png', prog='dot')

    # Save the image as a file
    img_path = "static/image.png"  # Replace with the desired file path
    img_io = io.BytesIO(img)
    with open(img_path, "wb") as img_file:
        img_file.write(img_io.getvalue())

    # Return the file path as a response
    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
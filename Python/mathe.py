import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = int(key)

def add_edge_to_tree(root, parent_val, child_val):
    if root is None:
        return False
    
    parent_val = int(parent_val)
    child_val = int(child_val)
    
    if root.val == parent_val:
        if child_val < parent_val:
            root.left = Node(child_val)
        else:
            root.right = Node(child_val)
        return True
    
    return add_edge_to_tree(root.left, parent_val, child_val) or \
           add_edge_to_tree(root.right, parent_val, child_val)

def layout_tree_no_overlap(root, min_x_dist=2.5, y_step=2.5):
    """
    Berechnet die exakten X/Y-Koordinaten stufenweise über Konturen,
    sodass sich Knoten auf JEDER Y-Ebene niemals überschneiden.
    """
    def get_layout(node, y=0):
        if node is None:
            return {}, {}

        # 1. Blattknoten
        if node.left is None and node.right is None:
            p = {node.val: (0.0, y)}
            c = {y: (0.0, 0.0)}
            return p, c

        # 2. Nur 1 Kind (links): Geht genau gerade nach unten
        if node.left is not None and node.right is None:
            sub_p, sub_c = get_layout(node.left, y - y_step)
            p = {node.val: (0.0, y)}
            p.update(sub_p)
            c = {y: (0.0, 0.0)}
            c.update(sub_c)
            return p, c

        # 3. Nur 1 Kind (rechts): Geht genau gerade nach unten
        if node.left is None and node.right is not None:
            sub_p, sub_c = get_layout(node.right, y - y_step)
            p = {node.val: (0.0, y)}
            p.update(sub_p)
            c = {y: (0.0, 0.0)}
            c.update(sub_c)
            return p, c

        # 4. Zwei Kinder: Konturen aller tiefen Ebenen vergleichen
        left_p, left_c = get_layout(node.left, y - y_step)
        right_p, right_c = get_layout(node.right, y - y_step)

        # Maximal benötigte Aufspreizung ermitteln
        required_shift = min_x_dist
        for y_lvl in left_c:
            if y_lvl in right_c:
                overlap = (left_c[y_lvl][1] - right_c[y_lvl][0]) + min_x_dist
                if overlap > required_shift:
                    required_shift = overlap

        shift_left = -required_shift / 2.0
        shift_right = required_shift / 2.0

        p = {node.val: (0.0, y)}
        c = {y: (0.0, 0.0)}

        # Punkte und Konturen verschieben
        for k, (x_val, y_val) in left_p.items():
            p[k] = (x_val + shift_left, y_val)
        for k, (x_val, y_val) in right_p.items():
            p[k] = (x_val + shift_right, y_val)

        for y_lvl, (mn, mx) in left_c.items():
            c[y_lvl] = (mn + shift_left, mx + shift_left)
        for y_lvl, (mn, mx) in right_c.items():
            if y_lvl in c:
                c[y_lvl] = (c[y_lvl][0], mx + shift_right)
            else:
                c[y_lvl] = (mn + shift_right, mx + shift_right)

        return p, c

    pos, _ = get_layout(root, 0)
    
    # In NetworkX-Graph konvertieren
    G = nx.DiGraph()
    def add_nodes_to_nx(n):
        if n.left:
            G.add_edge(n.val, n.left.val)
            add_nodes_to_nx(n.left)
        if n.right:
            G.add_edge(n.val, n.right.val)
            add_nodes_to_nx(n.right)
            
    add_nodes_to_nx(root)
    return G, pos

# --- Baum initialisieren ---
root_val = 1
root = Node(root_val)
add_edge_to_tree(root, 1, 2)
add_edge_to_tree(root, 2, 4)

# --- Automatische Knotenerstellung ---
i = 4
while i < 20000:
    parent = i
    while parent < 100000:
        next_val = parent * 2
        add_edge_to_tree(root, parent, next_val)
        parent = next_val
        
        if (parent - 1) % 3 == 0 and parent > 4:
            next_val = (parent - 1) // 3
            add_edge_to_tree(root, parent, next_val)
            parent = next_val
            
        if parent == 1:
            break
    i += 1
    if i % 1000 == 0:
        print(f"Fortschritt: {i} Knoten hinzugefügt.")

# --- Baum zeichnen ---
G, pos = layout_tree_no_overlap(root, min_x_dist=2.5, y_step=2.5)

plt.figure(figsize=(16, 12))
ax = plt.gca()
ax.set_aspect('auto')
ax.margins(0.1)

nx.draw(
    G, 
    pos, 
    with_labels=True, 
    node_size=600, 
    node_color='skyblue', 
    font_size=7, 
    font_weight='bold', 
    arrows=True,
    arrowsize=8
)

plt.title("Collatz-Baum ohne jegliche Überlappung")
plt.show()
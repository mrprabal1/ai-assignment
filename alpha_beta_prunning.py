import os
import math
from graphviz import Digraph
 
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'
 
 
class TreeNode:
    def __init__(self, name, value=None, is_max=True):
        self.name = name
        self.value = value
        self.is_max = is_max
        self.children = []
        self.visited = False
        self.alpha = -math.inf
        self.beta = math.inf
 
    def add_child(self, child):
        self.children.append(child)
 
 
def alpha_beta(node, alpha, beta, is_max, pruned):
    node.visited = True
 
    # leaf node — just return its value
    if not node.children:
        node.alpha = alpha
        node.beta = beta
        return node.value
 
    if is_max:
        best = -math.inf
        for i, child in enumerate(node.children):
            val = alpha_beta(child, alpha, beta, False, pruned)
            best = max(best, val)
            alpha = max(alpha, best)
 
            if beta <= alpha:
                # prune remaining siblings
                for skip in node.children[i + 1:]:
                    pruned.append((node.name, skip.name))
                break
 
    else:
        best = math.inf
        for i, child in enumerate(node.children):
            val = alpha_beta(child, alpha, beta, True, pruned)
            best = min(best, val)
            beta = min(beta, best)
 
            if beta <= alpha:
                for skip in node.children[i + 1:]:
                    pruned.append((node.name, skip.name))
                break
 
    node.value = best
    node.alpha = alpha
    node.beta = beta
    return best
 
 
def draw_tree(node, graph, pruned):
    inf = math.inf
 
    a = "-∞" if node.alpha == -inf else str(node.alpha)
    b = "∞"  if node.beta  ==  inf else str(node.beta)
    v = str(node.value) if node.value is not None else "?"
 
    if not node.children:
        # leaf — simple box, green tint
        graph.node(
            node.name,
            label=f"{node.name}\n{v}",
            shape="box",
            style="filled,rounded",
            fillcolor="#c8f7c5",
            fontname="Helvetica Bold",
            fontsize="13",
            color="#2ecc71",
            penwidth="2",
        )
    else:
        label = f"{node.name}  ({'MAX' if node.is_max else 'MIN'})\nval: {v}   α:{a}  β:{b}"
 
        if node.is_max:
            # MAX nodes — blue
            graph.node(
                node.name,
                label=label,
                shape="box",
                style="filled,rounded",
                fillcolor="#d6eaf8",
                fontname="Helvetica Bold",
                fontsize="12",
                color="#2980b9",
                penwidth="2.5",
            )
        else:
            # MIN nodes — orange
            graph.node(
                node.name,
                label=label,
                shape="box",
                style="filled,rounded",
                fillcolor="#fdebd0",
                fontname="Helvetica Bold",
                fontsize="12",
                color="#e67e22",
                penwidth="2.5",
            )
 
    for child in node.children:
        draw_tree(child, graph, pruned)
 
        if (node.name, child.name) in pruned:
            graph.edge(
                node.name, child.name,
                style="dashed",
                color="#e74c3c",
                label="pruned",
                fontcolor="#e74c3c",
                fontsize="10",
                penwidth="1.5",
            )
        else:
            graph.edge(
                node.name, child.name,
                style="solid",
                color="#555555",
                penwidth="1.8",
            )
 
 
def build_tree():
    """
    4-level tree (root → B → C → D → leaves).
    Mix of values chosen to guarantee several pruning cuts.
    """
    root = TreeNode("Root", is_max=True)
 
    b1 = TreeNode("B1", is_max=False)
    b2 = TreeNode("B2", is_max=False)
    b3 = TreeNode("B3", is_max=False)
    root.add_child(b1)
    root.add_child(b2)
    root.add_child(b3)
 
    # B1 subtree
    c1 = TreeNode("C1", is_max=True)
    c2 = TreeNode("C2", is_max=True)
    b1.add_child(c1)
    b1.add_child(c2)
 
    c1.add_child(TreeNode("D1", value=8))
    c1.add_child(TreeNode("D2", value=3))
    c1.add_child(TreeNode("D3", value=5))
 
    c2.add_child(TreeNode("D4", value=10))
    c2.add_child(TreeNode("D5", value=2))
 
    # B2 subtree
    c3 = TreeNode("C3", is_max=True)
    c4 = TreeNode("C4", is_max=True)
    b2.add_child(c3)
    b2.add_child(c4)
 
    c3.add_child(TreeNode("D6", value=4))
    c3.add_child(TreeNode("D7", value=7))
 
    c4.add_child(TreeNode("D8", value=1))
    c4.add_child(TreeNode("D9", value=6))
    c4.add_child(TreeNode("D10", value=9))
 
    # B3 subtree
    c5 = TreeNode("C5", is_max=True)
    c6 = TreeNode("C6", is_max=True)
    b3.add_child(c5)
    b3.add_child(c6)
 
    c5.add_child(TreeNode("D11", value=0))
    c5.add_child(TreeNode("D12", value=-3))
 
    c6.add_child(TreeNode("D13", value=11))
    c6.add_child(TreeNode("D14", value=5))
 
    return root
 
 
def main():
    root = build_tree()
 
    graph = Digraph("Alpha-Beta Pruning")
    graph.attr(rankdir="TB", bgcolor="#fafafa", fontname="Helvetica")
    graph.attr("node", margin="0.2")
 
    pruned = []
 
    print("Running alpha-beta search...")
    result = alpha_beta(root, -math.inf, math.inf, True, pruned)
    print(f"Optimal value: {result}")
    print(f"Pruned edges : {pruned}")
 
    draw_tree(root, graph, pruned)
 
    out = "alpha_beta_tree.gv"
    graph.render(out, format="png", cleanup=True)
    print(f"Saved → {out}.png")
 
 
if __name__ == "__main__":
    main()

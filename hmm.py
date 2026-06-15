import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 
 
def viterbi(obs_seq, states, start_p, trans_p, emit_p):
    n_states = len(states)
    n_obs = len(obs_seq)
 
    # prob[s, t] = best probability of being in state s at time t
    prob = np.zeros((n_states, n_obs))
    # back[s, t] = which state we came from to reach state s at time t
    back = np.zeros((n_states, n_obs), dtype=int)
 
    # initialise at t=0
    prob[:, 0] = start_p * emit_p[:, obs_seq[0]]
 
    # fill forward
    for t in range(1, n_obs):
        for s in range(n_states):
            candidates = prob[:, t - 1] * trans_p[:, s] * emit_p[s, obs_seq[t]]
            prob[s, t] = candidates.max()
            back[s, t] = candidates.argmax()
 
    # backtrack
    path = np.zeros(n_obs, dtype=int)
    path[-1] = prob[:, -1].argmax()
    for t in range(n_obs - 2, -1, -1):
        path[t] = back[path[t + 1], t + 1]
 
    return [states[i] for i in path], prob
 
 
def plot(prob_matrix, states, obs_seq, obs_labels, predicted_path):
    n_obs = len(obs_seq)
    time_steps = range(n_obs)
 
    # colour palette — one per state
    palette = ["#2980b9", "#e67e22", "#27ae60", "#8e44ad", "#c0392b"]
    colors = {s: palette[i % len(palette)] for i, s in enumerate(states)}
 
    fig, axes = plt.subplots(2, 1, figsize=(12, 9), gridspec_kw={"height_ratios": [3, 1]})
    fig.patch.set_facecolor("#f5f6fa")
 
    # ── top panel: probability lines ──────────────────────────────────────────
    ax = axes[0]
    ax.set_facecolor("#ffffff")
 
    for state in states:
        i = states.index(state)
        ax.plot(
            time_steps, prob_matrix[i, :],
            marker="o", linewidth=2.2, markersize=7,
            color=colors[state], label=state, zorder=3,
        )
        # annotate each point with its probability
        for t, p in enumerate(prob_matrix[i, :]):
            ax.annotate(
                f"{p:.4f}",
                xy=(t, p), xytext=(0, 9),
                textcoords="offset points",
                ha="center", fontsize=8.5,
                color=colors[state], fontweight="bold",
            )
 
    # highlight the predicted state at each step
    for t, state in enumerate(predicted_path):
        i = states.index(state)
        ax.scatter(t, prob_matrix[i, t], s=160, color=colors[state],
                   edgecolors="white", linewidths=2, zorder=5)
 
    ax.set_title("Hidden Markov Model — Viterbi State Probabilities", fontsize=14,
                 fontweight="bold", pad=12)
    ax.set_ylabel("Probability", fontsize=11)
    ax.set_xticks(time_steps)
    ax.set_xticklabels(
        [f"T{t}  ({obs_labels[obs_seq[t]]})" for t in time_steps],
        fontsize=10,
    )
    ax.legend(fontsize=10, framealpha=0.9)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.set_ylim(bottom=0)
 
    # ── bottom panel: predicted path bar ──────────────────────────────────────
    ax2 = axes[1]
    ax2.set_facecolor("#ffffff")
 
    for t, state in enumerate(predicted_path):
        ax2.barh(0, 1, left=t, color=colors[state], edgecolor="white",
                 linewidth=1.5, height=0.5)
        ax2.text(t + 0.5, 0, state, ha="center", va="center",
                 fontsize=10, fontweight="bold", color="white")
 
    ax2.set_xlim(0, n_obs)
    ax2.set_xticks(time_steps)
    ax2.set_xticklabels(
        [f"T{t}" for t in time_steps], fontsize=10
    )
    ax2.set_yticks([])
    ax2.set_title("Predicted State Sequence", fontsize=11, fontweight="bold", pad=8)
 
    # legend patches for the bottom bar
    patches = [mpatches.Patch(color=colors[s], label=s) for s in states]
    ax2.legend(handles=patches, fontsize=9, loc="upper right", framealpha=0.9)
 
    plt.tight_layout(pad=2.5)
    out = "viterbi_hmm.png"
    plt.savefig(out, dpi=150)
    print(f"Plot saved → {out}")
    plt.close()
 
 
def main():
    # model definition
    states      = ["Sunny", "Cloudy", "Rainy"]
    observations = ["Walk", "Shop", "Clean", "Rest"]
 
    start_p = np.array([0.5, 0.3, 0.2])
 
    # rows = from-state, cols = to-state
    trans_p = np.array([
        [0.6, 0.3, 0.1],   # Sunny  → ...
        [0.2, 0.5, 0.3],   # Cloudy → ...
        [0.1, 0.4, 0.5],   # Rainy  → ...
    ])
 
    # rows = state, cols = observation
    emit_p = np.array([
        [0.5, 0.3, 0.1, 0.1],   # Sunny
        [0.2, 0.3, 0.2, 0.3],   # Cloudy
        [0.1, 0.2, 0.5, 0.2],   # Rainy
    ])
 
    # Walk, Walk, Shop, Rest, Clean, Walk
    obs_seq = [0, 0, 1, 3, 2, 0]
 
    predicted, prob_matrix = viterbi(obs_seq, states, start_p, trans_p, emit_p)
 
    # terminal output
    print("Viterbi Algorithm — Hidden Markov Model\n")
    print(f"{'Time':<8} {'Observation':<12} {'Predicted State'}")
    print("─" * 35)
    for t, (obs, state) in enumerate(zip(obs_seq, predicted)):
        print(f"T={t:<6} {observations[obs]:<12} {state}")
    print("─" * 35)
    print(f"\nFull path: {' → '.join(predicted)}\n")
 
    plot(prob_matrix, states, obs_seq, observations, predicted)
 
 
if __name__ == "__main__":
    main()

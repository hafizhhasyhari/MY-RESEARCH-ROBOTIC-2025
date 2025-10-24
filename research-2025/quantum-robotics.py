def classical_rrt(start, goal, obstacles, max_iterations=100000):
    tree = Tree(start)
    for i in range(max_iterations):
        random_config = sample_random()  # O(1)
        nearest = tree.nearest(random_config)  # O(log N)
        new_config = extend(nearest, random_config)  # O(1)
        if collision_free(new_config, obstacles):  # O(M) untuk M obstacles
            tree.add(new_config)
            if reached(goal):
                return extract_path(tree)
    return None  # failed to find path
```

**Complexity Analysis:**
- Iterations: 100,000
- Per iteration: O(log N + M) = O(log(100K) + 100) ≈ O(100)
- **Total**: O(10^7) operations
- **Time**: 10^7 / 10^9 Hz = **10ms** → seems fast!

**But**: This gives SUBOPTIMAL path! Quality typically 150-200% of optimal.

**Optimal Classical Approach:**

Requires exploring entire configuration space:
- Configurations: 10^30 (as calculated above)
- **Time**: 10^21 years → **completely infeasible**

**Quantum Approach (QAOA):**
```
1. Encode configuration space in quantum state:
   |ψ⟩ = Σᵢ αᵢ|configᵢ⟩
   
2. Apply cost Hamiltonian HC (encodes path length):
   HC = Σᵢⱼ wᵢⱼ |i⟩⟨j|
   
3. Apply mixer Hamiltonian HM (enables exploration):
   HM = Σᵢ (|i⟩⟨i+1| + |i+1⟩⟨i|)
   
4. Alternate HC dan HM p times:
   |ψ(γ,β)⟩ = e^(-iβₚHM) e^(-iγₚHC) ... e^(-iβ₁HM) e^(-iγ₁HC) |ψ₀⟩
   
5. Measure resulting state → gives near-optimal configuration
